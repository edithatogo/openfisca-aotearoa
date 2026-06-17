"""Tests for high-performance API Pydantic models."""

import pytest
from pydantic import ValidationError

from openfisca_aotearoa.api.models import (
    CalculationRequest,
    ErrorEnvelope,
    ErrorPayload,
    ParametersResponse,
)


def test_calculation_request_accepts_person_variables() -> None:
    request = CalculationRequest.model_validate(
        {
            "period": "2025-01-01",
            "variables": ["age"],
            "persons": [
                {
                    "id": "person_a",
                    "date_of_birth": {"ETERNITY": "1995-01-01"},
                },
            ],
        },
    )

    assert request.period == "2025-01-01"
    assert request.variables == ["age"]
    assert request.persons[0].id == "person_a"
    assert request.persons[0].variables["date_of_birth"] == {
        "ETERNITY": "1995-01-01",
    }


def test_calculation_request_rejects_empty_variables() -> None:
    with pytest.raises(ValidationError):
        CalculationRequest.model_validate(
            {
                "period": "2025",
                "variables": [],
                "persons": [{"id": "person_a"}],
            },
        )


def test_calculation_request_rejects_empty_persons() -> None:
    with pytest.raises(ValidationError):
        CalculationRequest.model_validate(
            {
                "period": "2025",
                "variables": ["age"],
                "persons": [],
            },
        )


def test_error_envelope_serialises_error_payload() -> None:
    envelope = ErrorEnvelope(
        error=ErrorPayload(
            code="validation_error",
            message="Request body is invalid.",
            details=[{"field": "variables"}],
        ),
    )

    assert envelope.model_dump() == {
        "error": {
            "code": "validation_error",
            "message": "Request body is invalid.",
            "details": [{"field": "variables"}],
        },
    }


def test_parameters_response_defaults_to_not_truncated() -> None:
    response = ParametersResponse(path="root", children=["taxes"])

    assert response.truncated is False
