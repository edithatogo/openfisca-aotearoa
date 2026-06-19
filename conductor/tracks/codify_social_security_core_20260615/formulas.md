# Formula Evidence: Social Security Act 2018 Core Rules

Track 13 formula changes are implemented in the Social Security Act variable
modules and covered by focused YAML situation tests.

## Implemented Formula Surfaces

- Jobseeker Support s 26 ineligibility:
  `openfisca_aotearoa/variables/acts/social_security/jobseeker_support/jobseeker_support__ineligibility.py`
  defines `jobseeker_support__full_time_student`,
  `jobseeker_support__strike_action`, and
  `jobseeker_support__employment_training`; `jobseeker_support__entitled`
  applies those ineligibility checks.
- Sole Parent Support s 33 expiry:
  `sole_parent_support__expired` now derives expiry from absence of dependent
  children or the youngest child reaching the configured age threshold.
- Social Security Act 2018 Schedule 4 Part 2:
  `schedule_4__part2_1` now covers single people with dependent children who
  are principal caregivers or parent/principal family-role members.
- Social Security Act 2018 Schedule 4 Parts 4, 5, 6, 7, and 8:
  rate selector variables are implemented under
  `openfisca_aotearoa/variables/acts/social_security/schedule_4/`.

## Implementation Commit

- `817ccda4` records the core Schedule 4 and Sole Parent expiry test coverage
  update used to close Phase 2.
