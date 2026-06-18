"""Tests for canonical microsimulation cohort contracts."""

import pytest
from pydantic import ValidationError

from openfisca_aotearoa.microsimulation import (
    CohortInput,
    FamilyRecord,
    PersonRecord,
    SimulationOutput,
)


def test_cohort_contract_accepts_people_and_families() -> None:
    cohort = CohortInput.model_validate(
        {
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
        },
    )

    assert cohort.period == "2025-01-01"
    assert cohort.variables == ["age"]
    assert cohort.people[0].id == "person_a"
    assert cohort.families[0].principal == "person_a"
    assert cohort.source == "fixture"


def test_cohort_contract_rejects_duplicate_people() -> None:
    with pytest.raises(ValidationError, match="person ids must be unique"):
        CohortInput.model_validate(
            {
                "period": "2025",
                "variables": ["age"],
                "people": [
                    {"id": "person_a", "variables": {}},
                    {"id": "person_a", "variables": {}},
                ],
            },
        )


def test_cohort_contract_rejects_unknown_family_references() -> None:
    with pytest.raises(ValidationError, match="unknown person id"):
        CohortInput.model_validate(
            {
                "period": "2025",
                "variables": ["age"],
                "people": [{"id": "person_a", "variables": {}}],
                "families": [
                    {
                        "id": "family_a",
                        "principal": "missing",
                        "children": ["person_a"],
                    },
                ],
            },
        )


def test_person_record_exports_batch_variables() -> None:
    person = PersonRecord(
        id="person_a",
        variables={"income_tax__annual_gross_income": 50000.0},
    )

    assert person.to_batch_record() == {
        "id": "person_a",
        "income_tax__annual_gross_income": 50000.0,
    }


def test_family_record_exports_openfisca_roles() -> None:
    family = FamilyRecord(
        id="family_a",
        principal="person_a",
        children=["person_b"],
    )

    assert family.to_openfisca_entity() == {
        "principal": ["person_a"],
        "children": ["person_b"],
    }


def test_simulation_output_serialises_records() -> None:
    output = SimulationOutput(
        period="2025",
        variables=["age"],
        records=[{"id": "person_a", "age": 30}],
    )

    assert output.model_dump() == {
        "period": "2025",
        "variables": ["age"],
        "records": [{"id": "person_a", "age": 30}],
    }
