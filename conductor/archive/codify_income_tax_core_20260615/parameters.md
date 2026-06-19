# Parameters Evidence: Income Tax Act 2007 Core Rules

Track 14 uses existing income tax parameter trees and updated individual tax
rate parameters.

## Parameter Paths Exercised

- `parameters.taxes.income_tax.individual_income_tax_rate` supports progressive
  individual income tax calculation, including the 2024 transitional rates and
  2025 bracket activation.
- `parameters.taxes.income_tax.family_tax_credit.prescribed_amount` supports
  Income Tax Act 2007 family tax credit base calculations.
- `parameters.entitlements.income_tax.family_scheme.family_tax_credit.*`
  supports family tax credit entitlement, abatement thresholds, rates, and child
  amounts.
- `parameters.entitlements.income_tax.family_scheme.best_start.*` and
  `parameters.entitlements.income_tax.working_for_families.*` support the
  existing Working for Families situation tests used in Track 14 verification.

## Evidence Files

- `openfisca_aotearoa/parameters/taxes/income_tax/individual_income_tax_rate.yaml`
- `openfisca_aotearoa/parameters/taxes/income_tax/family_tax_credit/prescribed_amount.yaml`
- `openfisca_aotearoa/parameters/entitlements/income_tax/family_scheme/family_tax_credit/`
- `openfisca_aotearoa/parameters/entitlements/income_tax/family_scheme/best_start/`
- `openfisca_aotearoa/parameters/entitlements/income_tax/working_for_families/`
