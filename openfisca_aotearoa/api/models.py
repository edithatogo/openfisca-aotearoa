"""Pydantic models for the high-performance API."""

from typing import Any

from pydantic import BaseModel, ConfigDict, Field, model_validator


class PersonInput(BaseModel):
    """Input variables for one person in a calculation request."""

    model_config = ConfigDict(extra="allow")

    id: str = Field(min_length=1)

    @property
    def variables(self) -> dict[str, Any]:
        """Return OpenFisca variable inputs, excluding the person identifier."""
        return dict(self.model_extra or {})


class CalculationRequest(BaseModel):
    """Request body for `POST /calculate`."""

    period: str = Field(min_length=1)
    variables: list[str] = Field(min_length=1)
    persons: list[PersonInput] = Field(min_length=1)

    @model_validator(mode="after")
    def require_unique_person_ids(self) -> "CalculationRequest":
        """Reject duplicate person IDs before building an OpenFisca situation."""
        person_ids = [person.id for person in self.persons]
        if len(person_ids) != len(set(person_ids)):
            raise ValueError("person ids must be unique")
        return self


class CalculationResponse(BaseModel):
    """Response body for successful calculations."""

    period: str
    results: list[dict[str, Any]]


class HealthResponse(BaseModel):
    """Response body for `GET /health`."""

    status: str = "ok"
    service: str = "openfisca-aotearoa-api"


class MetadataResponse(BaseModel):
    """Response body for `GET /metadata`."""

    country_package: str
    model: str
    openfisca_core_version: str
    api_version: str = "1"


class ParametersResponse(BaseModel):
    """Response body for `GET /parameters`."""

    path: str
    children: list[str]
    truncated: bool = False


class ErrorPayload(BaseModel):
    """Structured API error payload."""

    code: str
    message: str
    details: list[Any] = Field(default_factory=list)


class ErrorEnvelope(BaseModel):
    """Shared non-2xx API error envelope."""

    error: ErrorPayload
