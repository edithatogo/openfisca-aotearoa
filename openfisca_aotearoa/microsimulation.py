"""Microsimulation cohort contracts and analytics adapter boundaries."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd
import polars as pl
from pydantic import BaseModel, Field, ValidationError, model_validator

from openfisca_aotearoa.simulation import BatchSimulator


class PersonRecord(BaseModel):
    """Canonical person input record for microsimulation cohorts."""

    id: str = Field(min_length=1)
    variables: dict[str, Any] = Field(default_factory=dict)

    def to_batch_record(self) -> dict[str, Any]:
        """Return a record accepted by `BatchSimulator.run`."""
        return {"id": self.id, **self.variables}


class FamilyRecord(BaseModel):
    """Canonical family relationship record for OpenFisca entities."""

    id: str = Field(min_length=1)
    principal: str = Field(min_length=1)
    children: list[str] = Field(default_factory=list)

    def to_openfisca_entity(self) -> dict[str, list[str]]:
        """Return OpenFisca family roles for this family."""
        return {
            "principal": [self.principal],
            "children": self.children,
        }


class CohortInput(BaseModel):
    """Canonical JSON input for bounded microsimulation runs."""

    period: str = Field(min_length=1)
    variables: list[str] = Field(min_length=1)
    people: list[PersonRecord] = Field(min_length=1)
    families: list[FamilyRecord] = Field(default_factory=list)
    source: str | None = None

    @model_validator(mode="after")
    def validate_references(self) -> "CohortInput":
        """Validate person uniqueness and family references."""
        person_ids = [person.id for person in self.people]
        if len(person_ids) != len(set(person_ids)):
            raise ValueError("person ids must be unique")

        known_people = set(person_ids)
        family_ids = [family.id for family in self.families]
        if len(family_ids) != len(set(family_ids)):
            raise ValueError("family ids must be unique")

        for family in self.families:
            references = [family.principal, *family.children]
            unknown = [person_id for person_id in references
                       if person_id not in known_people]
            if unknown:
                raise ValueError(
                    f"unknown person id in family {family.id!r}: {unknown[0]}",
                )
        return self

    def to_batch_records(self) -> list[dict[str, Any]]:
        """Return people as `BatchSimulator` row dictionaries."""
        return [person.to_batch_record() for person in self.people]

    def to_openfisca_families(self) -> list[dict[str, Any]]:
        """Return family records for OpenFisca entity construction."""
        return [
            {"id": family.id, **family.to_openfisca_entity()}
            for family in self.families
        ]


class SimulationOutput(BaseModel):
    """Canonical JSON output from a microsimulation run."""

    period: str
    variables: list[str]
    records: list[dict[str, Any]]


class MicrosimulationError(ValueError):
    """Raised when a bounded microsimulation request is invalid."""


class BoundedBatchRunner:
    """Run validated microsimulation cohorts with explicit row bounds."""

    def __init__(
        self,
        max_records: int = 10000,
        simulator: BatchSimulator | None = None,
    ) -> None:
        if max_records < 1:
            raise ValueError("max_records must be at least 1")
        self.max_records = max_records
        self.simulator = simulator or BatchSimulator()

    def run(self, cohort: CohortInput | dict[str, Any]) -> SimulationOutput:
        """Run a validated cohort and return canonical output records."""
        validated = self._cohort(cohort)
        if len(validated.people) > self.max_records:
            raise MicrosimulationError(
                "cohort size exceeds max_records "
                f"({len(validated.people)} > {self.max_records})",
            )

        try:
            result = self.simulator.run(
                validated.to_batch_records(),
                validated.period,
                validated.variables,
                families=validated.to_openfisca_families() or None,
            )
        except Exception as error:
            raise MicrosimulationError(
                f"calculation failed: {error}",
            ) from error
        return SimulationOutput(
            period=validated.period,
            variables=validated.variables,
            records=self._records(result),
        )

    def export(self, output: SimulationOutput, path: str | Path) -> Path:
        """Export canonical output records to JSON or CSV."""
        dataframe = pl.DataFrame(output.records)
        return BatchSimulator.export(dataframe, path)

    def _cohort(self, cohort: CohortInput | dict[str, Any]) -> CohortInput:
        """Validate or return an existing cohort contract."""
        if isinstance(cohort, CohortInput):
            return cohort
        try:
            return CohortInput.model_validate(cohort)
        except ValidationError as error:
            raise MicrosimulationError(f"invalid cohort: {error}") from error

    def _records(
        self,
        dataframe: pl.DataFrame | pd.DataFrame,
    ) -> list[dict[str, Any]]:
        """Convert supported dataframe outputs to record dictionaries."""
        if isinstance(dataframe, pd.DataFrame):
            return dataframe.to_dict(orient="records")
        return dataframe.to_dicts()
