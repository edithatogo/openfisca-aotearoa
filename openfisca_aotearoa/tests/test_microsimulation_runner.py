"""Tests for bounded microsimulation runner behavior."""

import json
from pathlib import Path

import pytest

from openfisca_aotearoa.microsimulation import (
    BoundedBatchRunner,
    CohortInput,
    MicrosimulationError,
)

FIXTURES = Path(__file__).parent / "fixtures"


def fixture_cohort() -> dict:
    """Return a small offline cohort fixture."""
    return {
        "period": "2025-01-01",
        "variables": ["age"],
        "people": [
            {
                "id": "person_a",
                "variables": {
                    "date_of_birth": {"ETERNITY": "1995-01-01"},
                },
            },
        ],
        "families": [
            {
                "id": "family_a",
                "principal": "person_a",
                "children": [],
            },
        ],
        "source": "fixture",
    }


def test_bounded_runner_executes_contract_cohort() -> None:
    runner = BoundedBatchRunner(max_records=2)

    output = runner.run(fixture_cohort())

    assert output.model_dump() == {
        "period": "2025-01-01",
        "variables": ["age"],
        "records": [{"id": "person_a", "age": 30}],
    }


def test_bounded_runner_accepts_validated_cohort() -> None:
    runner = BoundedBatchRunner(max_records=2)
    cohort = CohortInput.model_validate(fixture_cohort())

    output = runner.run(cohort)

    assert output.records == [{"id": "person_a", "age": 30}]


def test_bounded_runner_rejects_oversized_cohort() -> None:
    runner = BoundedBatchRunner(max_records=1)
    cohort = fixture_cohort()
    cohort["people"].append({"id": "person_b", "variables": {}})

    with pytest.raises(MicrosimulationError, match="exceeds max_records"):
        runner.run(cohort)


def test_bounded_runner_wraps_malformed_cohort_errors() -> None:
    runner = BoundedBatchRunner(max_records=2)

    with pytest.raises(MicrosimulationError, match="invalid cohort"):
        runner.run(
            {
                "period": "2025",
                "variables": ["age"],
                "people": [],
            },
        )


def test_bounded_runner_wraps_unknown_variable_errors() -> None:
    runner = BoundedBatchRunner(max_records=2)
    cohort = fixture_cohort()
    cohort["variables"] = ["missing_variable"]

    with pytest.raises(MicrosimulationError, match="calculation failed"):
        runner.run(cohort)


def test_bounded_runner_wraps_unsupported_period_errors() -> None:
    runner = BoundedBatchRunner(max_records=2)
    cohort = fixture_cohort()
    cohort["period"] = "not-a-period"

    with pytest.raises(MicrosimulationError, match="calculation failed"):
        runner.run(cohort)


def test_bounded_runner_exports_json_and_csv(tmp_path) -> None:
    runner = BoundedBatchRunner(max_records=2)
    output = runner.run(fixture_cohort())
    json_path = tmp_path / "output.json"
    csv_path = tmp_path / "output.csv"

    runner.export(output, json_path)
    runner.export(output, csv_path)

    assert json.loads(json_path.read_text()) == output.records
    assert csv_path.read_text().splitlines() == ["id,age", "person_a,30"]


def test_bounded_runner_loads_offline_fixture_cohort() -> None:
    runner = BoundedBatchRunner(max_records=10)
    fixture_path = FIXTURES / "microsimulation_cohort.json"

    output = runner.run(json.loads(fixture_path.read_text()))

    assert output.records == [
        {"id": "person_a", "age": 30},
        {"id": "person_b", "age": 15},
    ]
