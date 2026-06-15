# Specification: Integrate nztaxmicrosim Rules

## Purpose

Codify historical and current New Zealand tax brackets and rules into OpenFisca Aotearoa variables and parameters, importing references from the `nztaxmicrosim` repository and current Inland Revenue rate tables where newer tax years require updates.

## Requirements

- Reference the tax brackets, income thresholds, and tax rates mapped in `nztaxmicrosim`.
- Codify historical rates inside OpenFisca parameter files under `openfisca_aotearoa/parameters/taxes/`.
- Keep the implementation compatible with the current project typing baseline documented in `conductor/tech-stack.md`.
- Implement tests verifying calculations against known `nztaxmicrosim` validation outputs and current Inland Revenue rate tables.
