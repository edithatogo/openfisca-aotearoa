"""Tests for AI-assisted test candidate review gates."""

from pathlib import Path

import pytest
from pydantic import ValidationError

from openfisca_aotearoa.ai_test_automation import (
    CandidateMetadata,
    GeneratedTestCandidate,
    ReviewGateError,
    TestScenario as CandidateScenario,
    ToolEvaluation,
    load_candidate,
    require_accepted_candidate,
)
from openfisca_aotearoa.simulation import BatchSimulator


FIXTURE_DIR = Path(__file__).parent / "fixtures" / "ai_test_automation"
ACCEPTED_DIR = Path(__file__).parent / "ai_generated" / "accepted"


def test_candidate_metadata_requires_traceable_source_and_prompt() -> None:
    metadata = CandidateMetadata.model_validate(
        {
            "candidate_id": "age_boundary_2025",
            "source_track": "codify_social_security_core_20260615",
            "source_document": "conductor/tracks/example/spec.md",
            "prompt": "Generate boundary tests for age calculation.",
            "generator": "offline-template",
            "generated_at": "2026-06-18T00:00:00Z",
            "review_status": "quarantined",
        },
    )

    assert metadata.reviewer is None
    assert metadata.review_status == "quarantined"


def test_accepted_metadata_requires_reviewer() -> None:
    with pytest.raises(ValidationError, match="reviewer is required"):
        CandidateMetadata.model_validate(
            {
                "candidate_id": "age_boundary_2025",
                "source_track": "codify_social_security_core_20260615",
                "source_document": "conductor/tracks/example/spec.md",
                "prompt": "Generate boundary tests for age calculation.",
                "generator": "offline-template",
                "generated_at": "2026-06-18T00:00:00Z",
                "review_status": "accepted",
            },
        )


def test_quarantined_candidate_cannot_enter_accepted_suite() -> None:
    candidate = load_candidate(
        FIXTURE_DIR / "age_boundary.scenario.json",
        FIXTURE_DIR / "age_boundary.metadata.json",
    )

    with pytest.raises(ReviewGateError, match="not accepted"):
        require_accepted_candidate(candidate)


def test_accepted_generated_test_runs_deterministically() -> None:
    candidate = require_accepted_candidate(
        load_candidate(
            ACCEPTED_DIR / "age_boundary.scenario.json",
            ACCEPTED_DIR / "age_boundary.metadata.json",
        ),
    )

    result = BatchSimulator().run(
        candidate.scenario.inputs,
        candidate.scenario.period,
        candidate.scenario.output_variables,
    )

    assert result.to_dicts() == candidate.scenario.expected_results


def test_tool_evaluation_marks_testsprite_unavailable_without_network(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("shutil.which", lambda _: None)

    evaluation = ToolEvaluation.from_command("testsprite", command_path=None)

    assert evaluation.available is False
    assert evaluation.default_ci_mode == "disabled"
    assert "optional" in evaluation.notes[0]


def test_candidate_fixture_contract_round_trips() -> None:
    candidate = GeneratedTestCandidate(
        scenario=CandidateScenario.model_validate_json(
            (FIXTURE_DIR / "age_boundary.scenario.json").read_text(),
        ),
        metadata=CandidateMetadata.model_validate_json(
            (FIXTURE_DIR / "age_boundary.metadata.json").read_text(),
        ),
    )

    assert candidate.scenario.scenario_id == candidate.metadata.candidate_id
