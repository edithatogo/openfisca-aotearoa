# Specification: Integrate nztaxmicrosim Rules

## Purpose
Codify historical and current New Zealand tax brackets and rules into OpenFisca Aotearoa variables and parameters, importing references from the `nztaxmicrosim` repository.

## Requirements
- Reference the tax brackets, income thresholds, and tax rates mapped in `nztaxmicrosim`.
- Codify historical rates inside OpenFisca parameter files (`openfisca_aotearoa/parameters/tax/`).
- Enforce strict validation using `pydantic v2` and strict `basedpyright` typing.
- Implement tests verifying calculations against known `nztaxmicrosim` validation outputs.
