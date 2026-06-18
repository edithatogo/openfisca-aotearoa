"""Batch simulation helpers for OpenFisca Aotearoa."""

from pathlib import Path
from typing import Any, Literal

import pandas as pd
import polars as pl
from openfisca_core.simulation_builder import SimulationBuilder

from openfisca_aotearoa.aotearoa_legislationmodel import AotearoaLegislationModel

CohortData = list[dict[str, Any]] | pl.DataFrame | pd.DataFrame
FamilyData = list[dict[str, Any]] | None
OutputFormat = Literal["polars", "pandas"]
ExportFormat = Literal["csv", "json"]


class BatchSimulator:
    """Helper to run batch microsimulations on cohort data."""

    def __init__(self) -> None:
        self.system = AotearoaLegislationModel()

    def run(
        self,
        cohort_data: CohortData,
        period: str,
        output_variables: list[str],
        output_format: OutputFormat = "polars",
        families: FamilyData = None,
    ) -> pl.DataFrame | pd.DataFrame:
        """Run batch simulation on a cohort of individuals.

        Args:
            cohort_data: A list of dictionaries, Polars DataFrame, or pandas
                DataFrame where each row represents one person.
            period: The target period, such as ``"2025"`` or
                ``"2025-01-01"``.
            output_variables: OpenFisca person variables to calculate.
            output_format: Return ``"polars"`` or ``"pandas"`` dataframes.
            families: Optional OpenFisca family entity records.

        Returns:
            A dataframe containing person IDs and calculated variables.
        """
        records = self._normalise_cohort(cohort_data)
        if not records:
            raise ValueError("cohort_data must contain at least one person")

        if output_format not in ("polars", "pandas"):
            raise ValueError("output_format must be 'polars' or 'pandas'")

        situation = self._build_situation(records, period, families)
        simulation = SimulationBuilder().build_from_entities(
            self.system,
            situation,
        )

        person_ids = list(situation["persons"].keys())
        result_data: dict[str, list[Any]] = {"id": person_ids}
        for variable in output_variables:
            values = simulation.calculate(variable, period).tolist()
            if len(values) != len(person_ids):
                raise ValueError(
                    f"Variable {variable!r} did not return one value per person"
                )
            result_data[variable] = values

        if output_format == "pandas":
            return pd.DataFrame(result_data)
        return pl.DataFrame(result_data)

    @staticmethod
    def export(
        results: pl.DataFrame | pd.DataFrame,
        path: str | Path,
        file_format: ExportFormat | None = None,
    ) -> Path:
        """Export simulation results to CSV or JSON.

        Args:
            results: Polars or pandas dataframe returned by ``run``.
            path: Destination file path.
            file_format: Optional explicit format. When omitted, the suffix of
                ``path`` is used.

        Returns:
            The destination path.
        """
        destination = Path(path)
        selected_format = file_format or destination.suffix.lstrip(".")
        if selected_format not in ("csv", "json"):
            raise ValueError("file_format must be 'csv' or 'json'")

        if isinstance(results, pd.DataFrame):
            if selected_format == "csv":
                results.to_csv(destination, index=False)
            else:
                results.to_json(destination, orient="records")
            return destination

        if selected_format == "csv":
            results.write_csv(destination)
        else:
            results.write_json(destination)
        return destination

    def _normalise_cohort(self, cohort_data: CohortData) -> list[dict[str, Any]]:
        """Convert supported cohort inputs to row dictionaries."""
        if isinstance(cohort_data, pl.DataFrame):
            return cohort_data.to_dicts()
        if isinstance(cohort_data, pd.DataFrame):
            return cohort_data.to_dict(orient="records")
        return list(cohort_data)

    def _build_situation(
        self,
        records: list[dict[str, Any]],
        period: str,
        families: FamilyData = None,
    ) -> dict[str, dict[str, Any]]:
        """Build a fully specified OpenFisca entity situation."""
        persons = {}
        for index, individual in enumerate(records):
            person_id = individual.get("id", f"person_{index}")
            person_data: dict[str, Any] = {}
            for variable, value in individual.items():
                if variable == "id":
                    continue
                if isinstance(value, dict):
                    person_data[variable] = value
                else:
                    person_data[variable] = {period: value}
            persons[person_id] = person_data

        if families:
            family_entities = {
                family["id"]: {
                    key: value
                    for key, value in family.items()
                    if key != "id"
                }
                for family in families
            }
        else:
            family_entities = {
                "family_0": {
                    "principal": [next(iter(persons))],
                    "children": list(persons.keys())[1:],
                },
            }

        return {"persons": persons, "families": family_entities}
