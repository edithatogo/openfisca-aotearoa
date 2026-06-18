"""Legal audit and publish readiness gate contracts."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel, Field, computed_field, model_validator

ReadinessStatus = Literal[
    "draft",
    "implemented",
    "tested",
    "legally_reviewed",
    "publish_ready",
    "archived",
]

REQUIRED_EVIDENCE = (
    "traceability",
    "citations",
    "parameters",
    "formulas",
    "situation_tests",
    "manual_verification",
)


class ReadinessGateError(RuntimeError):
    """Raised when one or more manifests fail publish-readiness checks."""


class ManualCheckpoint(BaseModel):
    """Manual Conductor verification checkpoint discovered from a plan."""

    name: str
    status: Literal["work_done", "pending", "unknown"]


class EvidenceItem(BaseModel):
    """One readiness evidence signal found in plan text or track files."""

    kind: str
    source: str
    detail: str


class ReadinessManifest(BaseModel):
    """Machine-readable readiness summary for one Conductor track."""

    track_id: str = Field(min_length=1)
    title: str = Field(min_length=1)
    source_path: str = Field(min_length=1)
    readiness_status: ReadinessStatus
    manual_checkpoints: list[ManualCheckpoint] = Field(default_factory=list)
    required_evidence: list[str] = Field(
        default_factory=lambda: list(REQUIRED_EVIDENCE)
    )
    available_evidence: list[EvidenceItem] = Field(default_factory=list)
    missing_evidence: list[str] = Field(default_factory=list)
    unresolved_risks: list[str] = Field(default_factory=list)
    git_commits: list[str] = Field(default_factory=list)
    git_notes_present: list[str] = Field(default_factory=list)

    @computed_field
    @property
    def publish_ready(self) -> bool:
        """Return whether this manifest passes the local publish gate."""
        return (
            self.readiness_status == "publish_ready"
            and not self.missing_evidence
            and not self.unresolved_risks
        )

    @model_validator(mode="after")
    def require_clean_publish_ready_manifest(self) -> "ReadinessManifest":
        """Reject publish-ready manifests that still declare gaps."""
        if self.readiness_status == "publish_ready":
            if self.missing_evidence:
                raise ValueError("publish_ready requires no missing_evidence")
            if self.unresolved_risks:
                raise ValueError("publish_ready requires no unresolved_risks")
        return self


def build_readiness_manifest(
    track_path: str | Path,
    *,
    archived: bool = False,
    git_notes: dict[str, str] | None = None,
) -> ReadinessManifest:
    """Build a readiness manifest from a Conductor track directory."""
    path = Path(track_path)
    metadata = _read_metadata(path)
    plan_text = _read_text(path / "plan.md")
    track_id = str(metadata.get("track_id") or path.name)
    title = _title(plan_text, track_id)
    checkpoints = _manual_checkpoints(plan_text)
    available = _available_evidence(path, plan_text)
    missing = [
        evidence
        for evidence in REQUIRED_EVIDENCE
        if evidence not in {item.kind for item in available}
    ]
    commits = _commit_refs(plan_text)
    notes_present = sorted(
        commit for commit in commits if git_notes and commit in git_notes
    )
    risks = _risks(plan_text, checkpoints, missing, commits, notes_present)
    status = _readiness_status(
        archived=archived,
        plan_text=plan_text,
        checkpoints=checkpoints,
        missing=missing,
        risks=risks,
    )
    if status == "publish_ready":
        risks = []

    return ReadinessManifest(
        track_id=track_id,
        title=title,
        source_path=path.as_posix(),
        readiness_status=status,
        manual_checkpoints=checkpoints,
        available_evidence=available,
        missing_evidence=[] if status == "publish_ready" else missing,
        unresolved_risks=risks,
        git_commits=commits,
        git_notes_present=notes_present,
    )


def render_readiness_report(manifests: list[ReadinessManifest]) -> str:
    """Render a Markdown readiness report for policy/legal reviewers."""
    lines = [
        "# Legal Audit and Publish Readiness Report",
        "",
        "| Track | Status | Publish Ready | Missing Evidence | Risks |",
        "| --- | --- | --- | --- | --- |",
    ]
    for manifest in manifests:
        missing = ", ".join(manifest.missing_evidence) or "none"
        risks = "; ".join(manifest.unresolved_risks) or "none"
        lines.append(
            "| "
            f"{manifest.track_id} | {manifest.readiness_status} | "
            f"{manifest.publish_ready} | {missing} | {risks} |",
        )

    lines.extend(["", "## Evidence Detail", ""])
    for manifest in manifests:
        lines.extend([f"### {manifest.track_id}", ""])
        if manifest.available_evidence:
            for item in manifest.available_evidence:
                lines.append(f"- `{item.kind}`: {item.detail} ({item.source})")
        else:
            lines.append("- No readiness evidence found.")
        if manifest.unresolved_risks:
            lines.append("")
            lines.append("Unresolved risks:")
            for risk in manifest.unresolved_risks:
                lines.append(f"- {risk}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def require_publish_ready(manifests: list[ReadinessManifest]) -> None:
    """Fail when any manifest is not publish-ready."""
    failures = [
        manifest.track_id
        for manifest in manifests
        if not manifest.publish_ready
    ]
    if failures:
        raise ReadinessGateError(
            "Track(s) not publish-ready: " + ", ".join(failures),
        )


def _read_metadata(path: Path) -> dict[str, Any]:
    metadata_path = path / "metadata.json"
    if not metadata_path.exists():
        return {}
    return json.loads(metadata_path.read_text(encoding="utf-8"))


def _read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def _title(plan_text: str, fallback: str) -> str:
    for line in plan_text.splitlines():
        if line.startswith("# "):
            return line.removeprefix("# ").strip()
    return fallback


def _manual_checkpoints(plan_text: str) -> list[ManualCheckpoint]:
    checkpoints: list[ManualCheckpoint] = []
    pattern = re.compile(
        r"Conductor - User Manual Verification '([^']+)'.*"
        r"\[checkpoint: ([^\]]+)\]",
    )
    for line in plan_text.splitlines():
        match = pattern.search(line)
        if match:
            name, status = match.groups()
            checkpoint_status = (
                status if status in {"work_done", "pending"} else "unknown"
            )
            checkpoints.append(
                ManualCheckpoint(name=name, status=checkpoint_status),
            )
    return checkpoints


def _available_evidence(path: Path, plan_text: str) -> list[EvidenceItem]:
    evidence: list[EvidenceItem] = []
    lower = plan_text.lower()
    if "legislation.govt.nz" in lower or "citation" in lower:
        evidence.append(
            EvidenceItem(
                kind="citations",
                source="plan.md",
                detail="Plan references citations or legislation sources.",
            ),
        )
    if "parameter" in lower:
        evidence.append(
            EvidenceItem(
                kind="parameters",
                source="plan.md",
                detail="Plan references parameter work.",
            ),
        )
    if "variable" in lower or "formula" in lower:
        evidence.append(
            EvidenceItem(
                kind="formulas",
                source="plan.md",
                detail="Plan references variable or formula work.",
            ),
        )
    if "test" in lower or "situation" in lower:
        evidence.append(
            EvidenceItem(
                kind="situation_tests",
                source="plan.md",
                detail="Plan references situation or test evidence.",
            ),
        )
    if "work_done" in lower:
        evidence.append(
            EvidenceItem(
                kind="manual_verification",
                source="plan.md",
                detail="Plan contains completed manual verification.",
            ),
        )

    evidence_files = [
        candidate
        for candidate in path.iterdir()
        if candidate.is_file()
        and candidate.suffix.lower() in {".md", ".json"}
        and candidate.name not in {"plan.md", "metadata.json", "spec.md"}
    ]
    if evidence_files:
        evidence.append(
            EvidenceItem(
                kind="traceability",
                source=", ".join(sorted(file.name for file in evidence_files)),
                detail="Track has supporting evidence artifacts.",
            ),
        )
    return evidence


def _commit_refs(plan_text: str) -> list[str]:
    return sorted(set(re.findall(r"\b[0-9a-f]{7,8}\b", plan_text)))


def _risks(
    plan_text: str,
    checkpoints: list[ManualCheckpoint],
    missing: list[str],
    commits: list[str],
    notes_present: list[str],
) -> list[str]:
    risks: list[str] = []
    if "[ ]" in plan_text:
        risks.append("Plan has incomplete tasks.")
    for checkpoint in checkpoints:
        if checkpoint.status != "work_done":
            risks.append(f"Manual checkpoint pending: {checkpoint.name}")
    for evidence in missing:
        risks.append(f"Missing required evidence: {evidence}")
    missing_notes = sorted(set(commits) - set(notes_present))
    for commit in missing_notes:
        risks.append(f"Git note not found for commit: {commit}")
    return risks


def _readiness_status(
    *,
    archived: bool,
    plan_text: str,
    checkpoints: list[ManualCheckpoint],
    missing: list[str],
    risks: list[str],
) -> ReadinessStatus:
    if archived:
        return "archived"
    if not plan_text or "[x]" not in plan_text:
        return "draft"
    if "test" in plan_text.lower() or "situation" in plan_text.lower():
        base_status: ReadinessStatus = "tested"
    else:
        base_status = "implemented"
    if checkpoints and all(
        checkpoint.status == "work_done" for checkpoint in checkpoints
    ):
        base_status = "legally_reviewed"
    if not missing and not risks:
        return "publish_ready"
    return base_status
