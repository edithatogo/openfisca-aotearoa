# Specification: Decisional Simulation Analytics & Policy Diffusion

## Purpose
Integrate OpenFisca Aotearoa with local simulation engines, enabling policy analysts to execute large-scale population simulations, apply regression models, and model policy diffusion over `open_social_data`.

## Requirements
- Provide a robust Python simulation module (`simulation.py`) in OpenFisca Aotearoa.
- Utilize fast data frames (`polars`/`pandas`) to construct cohort-level situations.
- Allow running batch OpenFisca simulations to output individual net incomes, tax liabilities, and benefit entitlements.
- Enable export of simulation outcomes to standard data formats (JSON, CSV) to feed external regressors (`mars`, `voiage`, `innovate`).
- Accept list, Polars, and pandas cohort inputs and return either Polars or pandas results without optional undeclared dependencies.
