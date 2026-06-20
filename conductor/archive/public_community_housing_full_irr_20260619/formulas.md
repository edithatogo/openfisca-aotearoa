# Formulas

Implemented variables are in:

- `openfisca_aotearoa/variables/acts/housing_restructuring/social_housing.py`

Current-law weekly formula from 2 March 2026:

1. Check `housing_restructuring__social_housing_eligible`; ineligible people
   receive zero.
2. If required information is insufficient, or an income-related rent
   discrepancy remains unresolved, return the market-rent notice amount once,
   capped at market rent even when both notice flags are true.
3. Compute the income formula:
   - 25% of household assessable income up to the applicable threshold.
   - 50% of household assessable income above the threshold.
   - 25% of the lesser of weekly family tax credit entitlement and the cap.
   - 62% of additional-resident or boarder contributions.
4. Compute the benefit-floor formula:
   - 25% of the appropriate Jobseeker Support floor.
   - the same family-tax-credit component.
   - the same additional-resident contribution component.
5. Use the higher of the income formula and benefit-floor formula.
6. Apply any supplied minimum rent.
7. Cap the result at market rent where market rent is supplied.
8. Round down to the nearest dollar.

The existing public monthly variable
`housing_restructuring__income_related_rent` is preserved as a monthly
equivalent wrapper around the weekly calculation. Before 2 March 2026, the
weekly variable keeps the previous 25% assessable-income scaffold so historical
or transitional scenarios do not try to resolve current-law parameters.
