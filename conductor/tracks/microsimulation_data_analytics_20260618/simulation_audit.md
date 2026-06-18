# Simulation Helper Audit

Generated: 2026-06-18

## Existing Track 8 Surface

Track 8 is archived at `conductor/archive/simulation_analytics_20260615/`.
It delivered `openfisca_aotearoa/simulation.py` with:

- `BatchSimulator.run(...)` for list, Polars, and pandas person cohorts.
- OpenFisca execution through `SimulationBuilder`.
- Polars and pandas output formats.
- JSON and CSV export through `BatchSimulator.export(...)`.
- Offline tests in `openfisca_aotearoa/tests/test_simulation.py`.

## Current Capabilities

- Person-level records can be run without external datasets.
- Scalar inputs are wrapped as `{period: value}`.
- Existing period-shaped dictionaries are passed through unchanged.
- A default synthetic family is created when only person records are supplied.
- JSON and CSV exports are deterministic for the same dataframe row order.

## Gaps for Track 18

- No canonical JSON contract for dataset-derived cohorts.
- No explicit validation for duplicate person IDs before OpenFisca execution.
- No bounded runner to prevent accidentally loading large survey extracts.
- No household or family relationship contract beyond the helper's default
  synthetic family.
- No optional adapter boundaries for `open_social_data`, `voiage`, `mars`, or
  `innovate`.
- No tests that prove optional analytics integrations degrade clearly when
  packages are absent.

## Implementation Direction

Track 18 should preserve `BatchSimulator` compatibility while adding:

- Pydantic v2 models for canonical cohort JSON.
- A bounded runner that converts the contract into the existing simulator input.
- Explicit family-reference validation.
- Fixture-sized cohort examples for offline testing.
- Thin optional adapters that expose dependency status and raise actionable
  errors when external packages are unavailable.
