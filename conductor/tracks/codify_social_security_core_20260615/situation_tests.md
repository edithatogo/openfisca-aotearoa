# Situation Test Evidence: Social Security Act 2018 Core Rules

Focused Social Security situation tests cover the Phase 2 implementation
surfaces and were rerun during Track 13 closure.

## Focused Test Files

- `openfisca_aotearoa/tests/social_security/jobseeker_support/ineligibility.yaml`
  covers s 26 no-ineligibility, full-time student, strike action, and
  employment-training scenarios.
- `openfisca_aotearoa/tests/social_security/sole_parent_support/sole_parent_support__expired.yaml`
  covers s 33 expiry based on dependent-child and youngest-child-age cases.
- `openfisca_aotearoa/tests/social_security/sole_parent_support/sole_parent_support__entitled.yaml`
  covers Sole Parent Support relationship, dependent-child, split-care, age,
  and residential eligibility composition.
- `openfisca_aotearoa/tests/social_security/supported_living_payment/entitled.yaml`
  covers Supported Living Payment entitlement branches for disability,
  blindness, self-inflicted disability exclusion, and caring for another person.
- `openfisca_aotearoa/tests/social_security/schedule4/core_parts.yaml`
  covers Schedule 4 Parts 4, 5, 6, 7, and 8 selector behavior.

## Gate

Run focused Track 13 Social Security tests with:

```cmd
.venv\Scripts\openfisca-run-test.exe openfisca_aotearoa\tests\social_security\jobseeker_support\ineligibility.yaml openfisca_aotearoa\tests\social_security\sole_parent_support\sole_parent_support__expired.yaml openfisca_aotearoa\tests\social_security\sole_parent_support\sole_parent_support__entitled.yaml openfisca_aotearoa\tests\social_security\supported_living_payment\entitled.yaml openfisca_aotearoa\tests\social_security\schedule4\core_parts.yaml
```
