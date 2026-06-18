"""Legislation evidence manifests and optional tool adapter boundaries."""

from __future__ import annotations

import json
import re
import shutil
from datetime import UTC, datetime
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field


def _now_utc() -> datetime:
    return datetime.now(UTC)


VerificationStatus = Literal[
    "unverified",
    "verified",
    "failed",
    "manual_review",
    "tool_unavailable",
]

SourceType = Literal[
    "legislation",
    "citation_report",
    "policy_intent",
    "oia",
    "manual",
]


class EvidenceToolUnavailable(RuntimeError):
    """Raised when an optional evidence tool is required but unavailable."""


class EvidenceReference(BaseModel):
    """One auditable source reference used by an OpenFisca model artifact."""

    reference_id: str = Field(min_length=1)
    source_path: str = Field(min_length=1)
    line_number: int | None = Field(default=None, ge=1)
    source_type: SourceType
    title: str | None = None
    citation: str | None = None
    url: str | None = None
    retrieved_at: datetime | None = None
    verification_status: VerificationStatus = "unverified"
    notes: list[str] = Field(default_factory=list)


class ToolBoundary(BaseModel):
    """Operational boundary for an optional evidence integration."""

    name: str
    command: str
    purpose: str
    available: bool
    machine_readable_output: bool
    live_operations: Literal["disabled", "optional", "manual"]
    requires_credentials: bool = False
    notes: list[str] = Field(default_factory=list)


class EvidenceManifest(BaseModel):
    """Machine-readable evidence contract for one implementation track."""

    track: str = Field(min_length=1)
    generated_at: datetime = Field(default_factory=_now_utc)
    references: list[EvidenceReference] = Field(default_factory=list)
    tool_boundaries: list[ToolBoundary] = Field(default_factory=list)
    summary: str | None = None

    def to_markdown(self) -> str:
        """Render a compact human-readable evidence report."""
        lines = [
            f"# Evidence Report: {self.track}",
            "",
            f"- Generated at: {self.generated_at.isoformat()}",
            f"- References: {len(self.references)}",
            f"- Tool boundaries: {len(self.tool_boundaries)}",
        ]
        if self.summary:
            lines.extend(["", self.summary])
        if self.tool_boundaries:
            lines.extend(["", "## Tool Boundaries", ""])
            lines.append("| Tool | Available | Live operations | Credentials |")
            lines.append("| --- | --- | --- | --- |")
            for boundary in self.tool_boundaries:
                lines.append(
                    "| "
                    f"{boundary.name} | {boundary.available} | "
                    f"{boundary.live_operations} | "
                    f"{boundary.requires_credentials} |",
                )
        if self.references:
            lines.extend(["", "## References", ""])
            lines.append("| Source | Line | Status | URL |")
            lines.append("| --- | ---: | --- | --- |")
            for reference in self.references:
                line = reference.line_number or ""
                url = reference.url or ""
                lines.append(
                    "| "
                    f"{reference.source_path} | {line} | "
                    f"{reference.verification_status} | {url} |",
                )
        return "\n".join(lines) + "\n"


class SourcerightReport(BaseModel):
    """Machine-readable citation validation report."""

    tool: str = "sourceright"
    status: Literal["pass", "fail", "manual_review", "tool_unavailable"]
    checked_references: int = Field(ge=0)
    failures: list[str] = Field(default_factory=list)


class OptionalCliAdapter:
    """Base adapter for optional local command-line evidence tools."""

    def __init__(self, command: str) -> None:
        self.command = command

    def available(self) -> bool:
        """Return whether the configured command is present on PATH."""
        return shutil.which(self.command) is not None

    def require_available(self) -> None:
        """Raise a clear error if this optional command is unavailable."""
        if not self.available():
            raise EvidenceToolUnavailable(
                f"Optional evidence tool {self.command!r} is not available.",
            )


class SourcerightAdapter(OptionalCliAdapter):
    """Boundary for sourceright citation validation reports."""

    def __init__(self, command: str = "sourceright") -> None:
        super().__init__(command)

    @staticmethod
    def from_report_file(path: str | Path) -> SourcerightReport:
        """Parse a sourceright JSON report fixture or exported report."""
        return SourcerightReport.model_validate(_read_json(path))


class FixtureEvidenceAdapter:
    """Load offline fixture output for tools that may be absent locally."""

    def __init__(self, source: str, fixture_path: str | Path) -> None:
        self.source = source
        self.fixture_path = Path(fixture_path)

    def load(self) -> dict[str, object]:
        """Return the fixture payload after checking its source identity."""
        payload = _read_json(self.fixture_path)
        if payload.get("source") != self.source:
            raise ValueError(
                f"fixture source {payload.get('source')!r} does not match "
                f"{self.source!r}",
            )
        return payload


class CitationExtractor:
    """Extract legislation references from source and parameter files."""

    _url_pattern = re.compile(
        r"https?://(?:www\.)?legislation\.govt\.nz/[^\s\"'<>),]+",
    )

    def scan_paths(self, paths: list[str | Path]) -> list[EvidenceReference]:
        """Scan files or directories for legislation.govt.nz references."""
        references: list[EvidenceReference] = []
        for path in paths:
            for file_path in self._files(Path(path)):
                references.extend(self.scan_file(file_path))
        return references

    def scan_file(self, path: str | Path) -> list[EvidenceReference]:
        """Scan one text file for legislation.govt.nz URLs."""
        file_path = Path(path)
        references: list[EvidenceReference] = []
        for line_number, line in enumerate(
            file_path.read_text(encoding="utf-8").splitlines(),
            start=1,
        ):
            for index, match in enumerate(
                self._url_pattern.finditer(line), start=1
            ):
                url = _normalise_url(match.group(0))
                references.append(
                    EvidenceReference(
                        reference_id=f"{file_path.as_posix()}:{line_number}:{index}",
                        source_path=file_path.as_posix(),
                        line_number=line_number,
                        source_type="legislation",
                        title=_title_from_url(url),
                        citation=_citation_from_line(line),
                        url=url,
                    ),
                )
        return references

    def _files(self, path: Path) -> list[Path]:
        if path.is_file():
            return [path]
        suffixes = {".py", ".yaml", ".yml", ".md"}
        return sorted(
            candidate
            for candidate in path.rglob("*")
            if candidate.is_file() and candidate.suffix.lower() in suffixes
        )


def default_tool_boundaries() -> list[ToolBoundary]:
    """Return the supported Track 19 optional tool boundaries."""
    definitions = [
        {
            "name": "nz-legislation",
            "command": "nz-legislation",
            "purpose": "retrieve New Zealand Act and regulation text",
            "machine_readable_output": True,
            "live_operations": "optional",
            "requires_credentials": False,
        },
        {
            "name": "sourceright",
            "command": "sourceright",
            "purpose": "validate and report citation metadata",
            "machine_readable_output": True,
            "live_operations": "optional",
            "requires_credentials": False,
        },
        {
            "name": "nlp-policy-nz",
            "command": "nlp-policy-nz",
            "purpose": "search Hansard and policy-intent corpora",
            "machine_readable_output": True,
            "live_operations": "optional",
            "requires_credentials": False,
        },
        {
            "name": "fyi-cli",
            "command": "fyi-cli",
            "purpose": "look up OIA and disclosure evidence",
            "machine_readable_output": True,
            "live_operations": "manual",
            "requires_credentials": True,
            "notes": [
                "Live OIA requests and authenticated lookups must be "
                "operator-initiated.",
            ],
        },
    ]
    return [
        ToolBoundary(
            available=shutil.which(definition["command"]) is not None,
            notes=definition.get("notes", []),
            **{
                key: value
                for key, value in definition.items()
                if key != "notes"
            },
        )
        for definition in definitions
    ]


def build_manifest(
    track: str,
    paths: list[str | Path],
    *,
    include_tool_boundaries: bool = True,
) -> EvidenceManifest:
    """Build an offline evidence manifest from local files."""
    return EvidenceManifest(
        track=track,
        references=CitationExtractor().scan_paths(paths),
        tool_boundaries=(
            default_tool_boundaries() if include_tool_boundaries else []
        ),
        summary=(
            "Offline manifest generated from local variables, parameters, "
            "specifications, and roadmap documents."
        ),
    )


def _read_json(path: str | Path) -> dict[str, object]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _normalise_url(url: str) -> str:
    return url.rstrip(".,;")


def _title_from_url(url: str) -> str | None:
    match = re.search(r"/(act|regulation)/public/(\d{4})/(\d{4})/", url)
    if not match:
        return None
    kind, year, number = match.groups()
    noun = "Act" if kind == "act" else "Regulation"
    return f"New Zealand {noun} {year}/{number}"


def _citation_from_line(line: str) -> str | None:
    cleaned = line.strip().strip("#").strip()
    return cleaned or None
