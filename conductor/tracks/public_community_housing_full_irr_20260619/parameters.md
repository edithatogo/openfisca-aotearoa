# Parameters

Implemented parameter files:

- `openfisca_aotearoa/parameters/housing_restructuring/income_related_rent/proportions.yaml`
  - 25% of income up to threshold.
  - 50% of income above threshold.
  - 25% of family tax credit entitlement, capped.
  - 25% of the Jobseeker Support benefit floor.
  - 62% of additional-resident or boarder contributions from 2 March 2026.
- `openfisca_aotearoa/parameters/housing_restructuring/income_related_rent/thresholds.yaml`
  - $555.15 for sole tenants without children where that threshold applies.
  - $854.08 for other current guidance categories.
- `openfisca_aotearoa/parameters/housing_restructuring/income_related_rent/family_tax_credit_cap.yaml`
  - $151.88 weekly cap amount before applying the 25% family-tax-credit
    proportion, producing the $37.97 guidance cap.
- `openfisca_aotearoa/parameters/housing_restructuring/income_related_rent/minimum_weekly_rent.yaml`
  - Guidance minimum weekly rent amounts for the listed household categories.
- `openfisca_aotearoa/parameters/housing_restructuring/income_related_rent/transition_date.yaml`
  - 2 March 2026 amendment start date.

Threshold and minimum-rent amounts are guidance parameters, not independent
derivations of the NZ Super threshold rule. The regulatory source rule remains
cited; the current numeric values come from the official Work and Income
guidance page retrieved on 20 June 2026.
