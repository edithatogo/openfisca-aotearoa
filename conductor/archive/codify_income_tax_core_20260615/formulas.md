# Formula Evidence: Income Tax Act 2007 Core Rules

Track 14 formula changes are implemented in the Income Tax Act variable modules
and covered by focused YAML situation tests.

## Implemented Formula Surfaces

- Core individual income flow:
  `openfisca_aotearoa/variables/acts/income_tax/individual.py` calculates annual
  gross income, annual total deductions, net income, net loss, taxable income,
  and individual income tax.
- Core income components:
  `income_tax__employment_income`, `income_tax__business_income`,
  `income_tax__investment_income`, and `income_tax__other_income` are explicit
  annual components of gross income.
- Core deduction components:
  `income_tax__employment_related_deduction`,
  `income_tax__business_deduction`,
  `income_tax__charitable_donation_deduction`, and
  `income_tax__other_deduction` are explicit annual deduction inputs.
- Family tax credit yearly aggregation:
  `openfisca_aotearoa/variables/acts/income_tax/family_scheme/family_tax_credit.py`
  now uses `[populations.ADD]` for day-to-year aggregation, matching the current
  OpenFisca option API.

## Implementation Commits

- `a518c75` records the core individual income tax component and parameter
  implementation.
- Track 14 closure records the family tax credit aggregation compatibility fix.
