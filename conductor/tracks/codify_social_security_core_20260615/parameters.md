# Parameters Evidence: Social Security Act 2018 Core Rules

Track 13 uses existing Social Security parameter trees and confirms the new
rules bind to those parameter paths rather than introducing untracked constants.

## Parameter Paths Exercised

- `parameters.social_security.sole_parent_support.child_age_threshold`
  supports Social Security Act 2018 s 33 expiry logic in
  `sole_parent_support__expired`.
- `parameters.entitlements.social_security.sole_parent_support.age_threshold`
  supports Sole Parent Support age eligibility in
  `sole_parent_support__age_threshold`.
- `parameters.entitlements.social_security.jobseeker_support.age_threshold_without_dependent_child`
  and `parameters.entitlements.social_security.jobseeker_support.age_threshold_other`
  support Jobseeker Support age eligibility.
- `parameters.social_security.jobseeker_support.base.clauses` and
  `parameters.social_security.supported_living_payment.base.clauses` are
  exercised by existing base-rate calculations.

## Evidence Files

- `openfisca_aotearoa/parameters/social_security/jobseeker_support/base.yaml`
- `openfisca_aotearoa/parameters/social_security/sole_parent_support/base.yaml`
- `openfisca_aotearoa/parameters/social_security/sole_parent_support/child_age_threshold.yaml`
- `openfisca_aotearoa/parameters/social_security/supported_living_payment/base.yaml`
- `openfisca_aotearoa/parameters/entitlements/social_security/jobseeker_support/`
- `openfisca_aotearoa/parameters/entitlements/social_security/sole_parent_support/`
