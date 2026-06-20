# Manual Verification

Track 23 was manually checked against the official Act, regulations, and Work
and Income calculation guidance on 20 June 2026.

Verification decisions:

- The implemented weekly formula follows the current post-2 March 2026 higher
  of income formula and benefit-floor formula.
- The old monthly public variable is retained as a compatibility wrapper.
- Current-law thresholds, family-tax-credit cap, minimum rents, and examples
  are sourced from Work and Income guidance because the regulations define the
  source rule while the guidance publishes the operational amounts.
- Agency judgment areas are not silently inferred. They are exposed as inputs:
  assessable income, Jobseeker floor, market rent, minimum rent, discrepancy
  status, information sufficiency, and transitional exclusion status.
- The implementation does not perform live authenticated information requests,
  provider notifications, or external submissions.

Focused validation passed:

```text
uv run openfisca test openfisca_aotearoa\tests\housing_restructuring\social_housing.yaml
12 passed
```
