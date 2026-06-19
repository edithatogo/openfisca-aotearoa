# Citations Evidence: Income Tax Act 2007 Core Rules

Track 14 implementation is tied to Income Tax Act 2007 references embedded in
the variable and parameter surfaces.

## Primary Act Coverage

- Income Tax Act 2007, Part C income concepts:
  `openfisca_aotearoa/variables/acts/income_tax/individual.py` defines gross
  income component variables with legislation.govt.nz references for
  employment, business, investment, and other income.
- Income Tax Act 2007, Part D deduction concepts:
  `openfisca_aotearoa/variables/acts/income_tax/individual.py` defines
  deduction component variables with legislation.govt.nz references for
  employment-related, business, charitable donation, and other deductions.
- Income Tax Act 2007, individual income tax and family scheme rules:
  `openfisca_aotearoa/variables/acts/income_tax/individual.py` and
  `openfisca_aotearoa/variables/acts/income_tax/family_scheme/` contain
  Income Tax Act 2007 references for individual tax, family tax credit, Working
  for Families, and related credits.

## Traceability Reports

- `gap_analysis.md` maps the existing model against core Income Tax Act 2007
  individual tax, family scheme, Working for Families, and credit surfaces.
