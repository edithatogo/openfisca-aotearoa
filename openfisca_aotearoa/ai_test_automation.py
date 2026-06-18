"""AI-assisted test candidate contracts and review gates."""

from __future__ import annotations

import json
import shutil
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel, Field, model_validator

ReviewStatus = Literal["quarantined", "accepted", "rejected", "needs_changes"]


class ReviewGateError(ValueError):
    """Raised when a generated candidate fails the review gate."""


class ToolEvaluation(BaseModel):
    """Local evaluation of an optional AI test generation tool."""

    name: str
    available: bool
    command_path: str | None = None
    default_ci_mode: Literal["disabled", "fixture_only", "enabled"]
    notes: list[str] = Field(default_factory=list)

    @classmethod
    def from_command(
        cls,
        name: str,
        *,
        command_path: str | None = None,
    ) -> "ToolEvaluation":
        """Evaluate a command without invoking network or AI services."""
        resolved = command_path or shutil.which(name)
        return cls(
            name=name,
            available=resolved is not None,
            command_path=resolved,
            default_ci_mode="fixture_only" if resolved else "disabled",
            notes=[
                "AI generation is optional; default CI uses reviewed fixtures "
                "and never calls a network-only service.",
            ],
        )


class CandidateMetadata(BaseModel):
    """Metadata sidecar for an AI-generated test candidate."""

    candidate_id: str = Field(min_length=1)
    source_track: str = Field(min_length=1)
    source_document: str = Field(min_length=1)
    prompt: str = Field(min_length=1)
    generator: str = Field(min_length=1)
    generated_at: datetime
    review_status: ReviewStatus = "quarantined"
    reviewer: str | None = None
    reviewed_at: datetime | None = None
    notes: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def require_reviewer_for_final_status(self) -> "CandidateMetadata":
        """Require reviewer metadata before a candidate leaves quarantine."""
        if self.review_status in {"accepted", "rejected", "needs_changes"}:
            if not self.reviewer:
                raise ValueError(
                    "reviewer is required when review_status is final",
                )
            if self.reviewed_at is None:
                raise ValueError(
                    "reviewed_at is required when review_status is final",
                )
        return self


class TestScenario(BaseModel):
    """Deterministic test scenario generated into quarantine or accepted sets."""

    scenario_id: str = Field(min_length=1)
    title: str = Field(min_length=1)
    period: str = Field(min_length=1)
    inputs: list[dict[str, Any]] = Field(min_length=1)
    output_variables: list[str] = Field(min_length=1)
    expected_results: list[dict[str, Any]] = Field(min_length=1)
    source_reference: str | None = None


class GeneratedTestCandidate(BaseModel):
    """A scenario plus its review metadata sidecar."""

    scenario: TestScenario
    metadata: CandidateMetadata

    @model_validator(mode="after")
    def require_matching_ids(self) -> "GeneratedTestCandidate":
        """Keep scenario and sidecar identifiers aligned."""
        if self.scenario.scenario_id != self.metadata.candidate_id:
            raise ValueError("scenario_id must match metadata candidate_id")
        return self


def load_candidate(
    scenario_path: str | Path,
    metadata_path: str | Path,
) -> GeneratedTestCandidate:
    """Load a generated candidate and its metadata sidecar from JSON."""
    return GeneratedTestCandidate(
        scenario=TestScenario.model_validate(_read_json(scenario_path)),
        metadata=CandidateMetadata.model_validate(_read_json(metadata_path)),
    )


def require_accepted_candidate(
    candidate: GeneratedTestCandidate,
) -> GeneratedTestCandidate:
    """Return an accepted candidate or raise a review-gate error."""
    if candidate.metadata.review_status != "accepted":
        raise ReviewGateError(
            f"candidate {candidate.metadata.candidate_id!r} is not accepted",
        )
    return candidate


def generate_offline_candidate(
    *,
    candidate_id: str,
    source_track: str,
    source_document: str,
    prompt: str,
    generated_at: datetime | None = None,
) -> GeneratedTestCandidate:
    """Generate a deterministic review candidate without calling an AI service."""
    timestamp = generated_at or datetime.now(UTC)
    return GeneratedTestCandidate(
        scenario=TestScenario(
            scenario_id=candidate_id,
            title="Candidate age boundary scenario",
            period="2025-01-01",
            inputs=[
                {
                    "id": "person_a",
                    "date_of_birth": {"ETERNITY": "1995-01-01"},
                },
            ],
            output_variables=["age"],
            expected_results=[{"id": "person_a", "age": 30}],
            source_reference=source_document,
        ),
        metadata=CandidateMetadata(
            candidate_id=candidate_id,
            source_track=source_track,
            source_document=source_document,
            prompt=prompt,
            generator="offline-template",
            generated_at=timestamp,
            review_status="quarantined",
            notes=[
                "Generated by deterministic offline template pending review.",
            ],
        ),
    )


def write_candidate(
    candidate: GeneratedTestCandidate,
    output_dir: str | Path,
) -> tuple[Path, Path]:
    """Write a candidate scenario and metadata sidecar to a directory."""
    destination = Path(output_dir)
    destination.mkdir(parents=True, exist_ok=True)
    scenario_path = (
        destination / f"{candidate.metadata.candidate_id}.scenario.json"
    )
    metadata_path = (
        destination / f"{candidate.metadata.candidate_id}.metadata.json"
    )
    scenario_path.write_text(
        candidate.scenario.model_dump_json(indent=2) + "\n",
        encoding="utf-8",
    )
    metadata_path.write_text(
        candidate.metadata.model_dump_json(indent=2) + "\n",
        encoding="utf-8",
    )
    return scenario_path, metadata_path


def _read_json(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))
