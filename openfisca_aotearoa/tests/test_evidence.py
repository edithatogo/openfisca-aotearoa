"""Tests for legislation evidence manifest and adapter boundaries."""

from pathlib import Path

import pytest

from openfisca_aotearoa.evidence import (
    CitationExtractor,
    EvidenceManifest,
    EvidenceReference,
    EvidenceToolUnavailable,
    FixtureEvidenceAdapter,
    SourcerightAdapter,
    default_tool_boundaries,
)


FIXTURE_DIR = Path(__file__).parent / "fixtures" / "evidence"


def test_citation_extractor_finds_legislation_references() -> None:
    references = CitationExtractor().scan_paths(
        [FIXTURE_DIR / "representative_variable.py"],
    )

    assert [reference.url for reference in references] == [
        "https://www.legislation.govt.nz/act/public/2018/0032/latest/DLM6784850.html",
    ]
    assert references[0].source_path.endswith("representative_variable.py")
    assert references[0].line_number == 8
    assert references[0].verification_status == "unverified"


def test_evidence_manifest_serialises_machine_readable_contract() -> None:
    manifest = EvidenceManifest(
        track="legislation_evidence_pipeline_20260618",
        references=[
            EvidenceReference(
                reference_id="representative_variable.py:8:1",
                source_path="representative_variable.py",
                line_number=8,
                source_type="legislation",
                title="Social Security Act 2018",
                citation="Social Security Act 2018, schedule 4",
                url=(
                    "https://www.legislation.govt.nz/act/public/2018/0032/"
                    "latest/DLM6784850.html"
                ),
                verification_status="verified",
            ),
        ],
    )

    payload = manifest.model_dump(mode="json")

    assert payload["track"] == "legislation_evidence_pipeline_20260618"
    assert payload["references"][0]["verification_status"] == "verified"
    assert "generated_at" in payload


def test_sourceright_adapter_parses_fixture_report() -> None:
    report = SourcerightAdapter.from_report_file(
        FIXTURE_DIR / "sourceright_report.json",
    )

    assert report.tool == "sourceright"
    assert report.status == "pass"
    assert report.checked_references == 1
    assert report.failures == []


def test_fixture_adapter_loads_nz_legislation_document() -> None:
    document = FixtureEvidenceAdapter(
        "nz-legislation",
        FIXTURE_DIR / "nz_legislation_document.json",
    ).load()

    assert document["source"] == "nz-legislation"
    assert document["jurisdiction"] == "NZ"
    assert document["title"] == "Social Security Act 2018"


def test_tool_boundaries_are_explicit_and_do_not_require_live_access() -> None:
    statuses = {status.name: status for status in default_tool_boundaries()}

    assert statuses["fyi-cli"].requires_credentials is True
    assert statuses["fyi-cli"].live_operations == "manual"
    assert statuses["nlp-policy-nz"].live_operations == "optional"
    assert statuses["sourceright"].machine_readable_output is True


def test_missing_optional_tool_raises_clear_error() -> None:
    missing = SourcerightAdapter(command="definitely-missing-sourceright")

    with pytest.raises(EvidenceToolUnavailable, match="not available"):
        missing.require_available()
