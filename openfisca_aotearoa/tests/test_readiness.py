"""Tests for legal audit and publish readiness gates."""

from pathlib import Path

import pytest
from pydantic import ValidationError

from openfisca_aotearoa.readiness import (
    ReadinessGateError,
    ReadinessManifest,
    build_readiness_manifest,
    render_readiness_report,
    require_publish_ready,
)


FIXTURE_DIR = Path(__file__).parent / "fixtures" / "readiness"


def test_publish_ready_manifest_requires_no_unresolved_risks() -> None:
    with pytest.raises(ValidationError, match="unresolved_risks"):
        ReadinessManifest.model_validate(
            {
                "track_id": "example_track",
                "title": "Example Track",
                "source_path": "conductor/tracks/example",
                "readiness_status": "publish_ready",
                "manual_checkpoints": [],
                "required_evidence": [],
                "available_evidence": [],
                "missing_evidence": [],
                "unresolved_risks": ["manual checkpoint pending"],
            },
        )


def test_completed_fixture_track_is_publish_ready() -> None:
    manifest = build_readiness_manifest(
        FIXTURE_DIR / "completed_track",
        git_notes={"abc1234": "Implemented and reviewed."},
    )

    assert manifest.readiness_status == "publish_ready"
    assert manifest.publish_ready is True
    assert manifest.missing_evidence == []


def test_non_completed_metadata_blocks_publish_ready() -> None:
    manifest = build_readiness_manifest(
        FIXTURE_DIR / "phase1_track",
        registry_status=" ",
        git_notes={"abc1234": "Implemented and reviewed."},
    )

    assert manifest.readiness_status == "legally_reviewed"
    assert manifest.publish_ready is False
    assert "Track metadata status is phase1_done, not completed." in (
        manifest.unresolved_risks
    )
    assert "Track registry status is  , not x." in manifest.unresolved_risks


def test_plan_keywords_do_not_satisfy_artifact_evidence() -> None:
    manifest = build_readiness_manifest(
        FIXTURE_DIR / "plan_only_track",
        git_notes={"abc1234": "Implemented and reviewed."},
    )

    assert manifest.readiness_status == "legally_reviewed"
    assert manifest.publish_ready is False
    assert "citations" in manifest.missing_evidence
    assert "situation_tests" in manifest.missing_evidence


def test_pending_manual_checkpoint_blocks_publish_ready() -> None:
    manifest = build_readiness_manifest(FIXTURE_DIR / "pending_track")

    assert manifest.readiness_status == "tested"
    assert manifest.publish_ready is False
    assert "Manual checkpoint pending: Rules load" in manifest.unresolved_risks


def test_archived_fixture_track_is_archived_not_publish_ready() -> None:
    manifest = build_readiness_manifest(
        FIXTURE_DIR / "archived_track",
        archived=True,
    )

    assert manifest.readiness_status == "archived"
    assert manifest.publish_ready is False


def test_readiness_report_includes_risks_and_evidence() -> None:
    manifests = [
        build_readiness_manifest(FIXTURE_DIR / "completed_track"),
        build_readiness_manifest(FIXTURE_DIR / "pending_track"),
    ]

    report = render_readiness_report(manifests)

    assert "# Legal Audit and Publish Readiness Report" in report
    assert "completed_track" in report
    assert "Manual checkpoint pending: Rules load" in report


def test_publish_gate_fails_when_required_evidence_missing() -> None:
    manifest = build_readiness_manifest(FIXTURE_DIR / "pending_track")

    with pytest.raises(ReadinessGateError, match="not publish-ready"):
        require_publish_ready([manifest])
