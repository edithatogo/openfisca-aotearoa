"""Tests for batch simulation helpers."""

import json

import pandas as pd
import polars as pl

from openfisca_aotearoa.simulation import BatchSimulator


def test_batch_simulator_runs_person_calculations() -> None:
    simulator = BatchSimulator()

    result = simulator.run(
        [
            {
                "id": "person_a",
                "date_of_birth": {"ETERNITY": "1995-01-01"},
            },
        ],
        "2025-01-01",
        ["age"],
    )

    assert result.to_dicts() == [{"id": "person_a", "age": 30}]


def test_batch_simulator_accepts_pandas_and_returns_pandas() -> None:
    simulator = BatchSimulator()
    cohort = pd.DataFrame(
        [
            {
                "id": "person_a",
                "income_tax__annual_gross_income": 50000.0,
            },
        ],
    )

    result = simulator.run(
        cohort,
        "2025",
        ["income_tax__net_income"],
        output_format="pandas",
    )

    assert isinstance(result, pd.DataFrame)
    assert result.to_dict(orient="records") == [
        {
            "id": "person_a",
            "income_tax__net_income": 50000.0,
        },
    ]


def test_batch_simulator_accepts_polars() -> None:
    simulator = BatchSimulator()
    cohort = pl.DataFrame(
        [
            {
                "id": "person_a",
                "income_tax__annual_gross_income": 50000.0,
            },
        ],
    )

    result = simulator.run(cohort, "2025", ["income_tax__net_income"])

    assert result.to_dicts() == [
        {
            "id": "person_a",
            "income_tax__net_income": 50000.0,
        },
    ]


def test_batch_simulator_exports_csv_and_json(tmp_path) -> None:
    result = pl.DataFrame(
        [
            {
                "id": "person_a",
                "income_tax__net_income": 50000.0,
            },
        ],
    )
    csv_path = tmp_path / "simulation.csv"
    json_path = tmp_path / "simulation.json"

    BatchSimulator.export(result, csv_path)
    BatchSimulator.export(result, json_path)

    assert "income_tax__net_income" in csv_path.read_text()
    assert json.loads(json_path.read_text()) == [
        {
            "id": "person_a",
            "income_tax__net_income": 50000.0,
        },
    ]
