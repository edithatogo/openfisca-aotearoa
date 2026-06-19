# Situation Test Evidence: Income Tax Act 2007 Core Rules

Focused Income Tax situation tests cover the Track 14 implementation surfaces
and were rerun during closure.

## Focused Test Files

- `openfisca_aotearoa/tests/individual_income_tax_rate.yaml` covers net income,
  net loss, taxable income, progressive individual tax rates, 2024 transitional
  rates, 2025 rates, and component-to-tax flow.
- `openfisca_aotearoa/tests/income_tax/family_scheme/eligibility.yaml` covers
  family scheme qualification and residence/caregiver eligibility cases.
- `openfisca_aotearoa/tests/income_tax/family_scheme/family_tax_credit.yaml`
  covers family tax credit base, eldest-child, non-eldest-child, income
  threshold, and family qualification behavior.
- `openfisca_aotearoa/tests/income_tax/family_scheme/working_for_families_entitlement.yaml`
  covers Working for Families entitlement composition.

## Gates

Run focused Track 14 tests with:

```cmd
set PYTHONUTF8=1&& set PYTHONIOENCODING=utf-8&& .venv\Scripts\openfisca-run-test.exe openfisca_aotearoa\tests\individual_income_tax_rate.yaml openfisca_aotearoa\tests\income_tax\family_scheme\eligibility.yaml openfisca_aotearoa\tests\income_tax\family_scheme\working_for_families_entitlement.yaml openfisca_aotearoa\tests\income_tax\family_scheme\family_tax_credit.yaml
```

Run the full family scheme collection with:

```cmd
set PYTHONUTF8=1&& set PYTHONIOENCODING=utf-8&& .venv\Scripts\openfisca-run-test.exe openfisca_aotearoa\tests\income_tax\family_scheme
```
