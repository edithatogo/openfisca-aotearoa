# Situation Tests

Focused housing tests are in:

- `openfisca_aotearoa/tests/housing_restructuring/social_housing.yaml`

Covered branches:

- 25% below-threshold rent.
- 25% plus 50% above-threshold rent.
- sole-without-children threshold branch.
- family tax credit cap.
- additional-resident contribution at 62%.
- Jobseeker Support benefit-floor higher-rent test.
- market-rent cap.
- minimum-rent floor.
- insufficient-information market-rent notice.
- pre-2026 transitional old-scaffold calculation.
- monthly public-variable compatibility wrapper.
- ineligible applicant zero result.

Focused command run:

```text
uv run openfisca test openfisca_aotearoa\tests\housing_restructuring\social_housing.yaml
```

Result:

```text
12 passed
```
