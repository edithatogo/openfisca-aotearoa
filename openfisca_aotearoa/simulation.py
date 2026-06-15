"""Batch simulation module for OpenFisca Aotearoa."""

from typing import Any, Dict, List
import polars as pl
from openfisca_aotearoa.aotearoa_legislationmodel import AotearoaLegislationModel


class BatchSimulator:
    """Helper to run batch microsimulations on cohort data."""

    def __init__(self) -> None:
        self.system = AotearoaLegislationModel()

    def run(
        self,
        cohort_data: List[Dict[str, Any]],
        period: str,
        output_variables: List[str]
    ) -> pl.DataFrame:
        """Run batch simulation on a cohort of individuals.

        Args:
            cohort_data: List of dicts representing individuals (e.g. [{"id": "ind1", "income_tax__annual_gross_income": 50000}])
            period: The target year or month (e.g. "2025")
            output_variables: Variables to calculate (e.g. ["income_tax__individual_income_tax"])

        Returns:
            A Polars DataFrame containing the calculated variables for the cohort.
        """
        # Map input data to OpenFisca simulation format
        persons = {}
        for idx, ind in enumerate(cohort_data):
            person_id = ind.get("id", f"person_{idx}")
            person_data: Dict[str, Any] = {}
            for k, v in ind.items():
                if k != "id":
                    person_data[k] = {period: v}
            persons[person_id] = person_data

        situation = {
            "persons": persons,
            "families": {
                "family_0": {
                    "principal": list(persons.keys())[0] if persons else None,
                    "children": list(persons.keys())[1:] if len(persons) > 1 else []
                }
            }
        }

        # Run OpenFisca Simulation
        from openfisca_core.simulations import Simulation
        sim = Simulation(self.system, situation)
        
        result_data: Dict[str, List[Any]] = {"id": list(persons.keys())}
        for var in output_variables:
            result_data[var] = sim.calculate(var, period).tolist()

        return pl.DataFrame(result_data)
