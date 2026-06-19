# Legislative Currentness Report

Date: 2026-06-19

## Outcome

Track 22 closes the freshness review by separating incorporated model changes from explicit no-impact, out-of-scope, and partial-coverage decisions.

## Implemented Changes

- ACC earners levy parameters now include official rates and maximum liable earnings for 2024/25, 2025/26, 2026/27, and 2027/28 and later.
- ACC YAML tests cover below-cap and capped calculations across those refreshed years using the repository's annual-period tax-year convention.

## Decisions Without Code Changes

- Pae Ora section 46A is a ministerial strategy duty and does not affect the current primary-care copayment subsidy model.
- Tax Administration Deposit Takers Act and unincorporated amendment issues do not affect the current automatic-assessment or filing-deadline variables.

## Accepted Partial Coverage

- Public and Community Housing Management income-related rent remains intentionally partial. The existing variable is a simplified monthly scaffold and must not be represented as full coverage of the current weekly calculation under sections 106, 107, 109, and Schedule 4 transitional clauses.
- ACC self-employed low-earner and purchased-weekly-compensation formulas are outside the current employee-style earners levy model.

## Validation

- PASS: .venv\Scripts\python.exe scripts\run_openfisca_yaml_tests.py openfisca_aotearoa\tests\acc\earners_levy.yaml
- BLOCKED: uv-based validation could not run in this managed session because uv cache writes failed with Access is denied errors. The repo virtualenv runner was used for focused YAML validation.

## Release Risk

Readiness evidence exists for Tracks 9-12, and Track 22 now records currentness decisions. Remaining legal risk is limited to surfaces explicitly marked partial or out-of-scope above.
