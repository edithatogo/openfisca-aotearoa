# Plan: Microsimulation Data and Analytics Integrations

## Phase 1: Data Contract and Dependency Audit

- [x] Task: Audit existing simulation helper code and Track 8 artifacts. (`4d54361`)
- [x] Task: Define canonical JSON schema for people, families, periods, variables, and outputs. (`1c56017`)
- [x] Task: Audit availability and import paths for `open_social_data`, `voiage`, `mars`, and `innovate`. (`e5e27dd`)
- [x] Task: Conductor - User Manual Verification 'Microsimulation contract review' [checkpoint: work_done]. (4d54361, 1c56017, e5e27dd)

## Phase 2: Batch Simulation Runner

- [ ] Task: Implement or extend a batch simulation runner for bounded cohort inputs.
- [ ] Task: Add validation and clear errors for missing variables, malformed entities, and unsupported periods.
- [ ] Task: Add deterministic JSON and CSV export paths.
- [ ] Task: Add small offline fixture cohorts that do not require large external datasets.

## Phase 3: Analytics Adapter Boundaries

- [ ] Task: Add optional adapter interfaces for value-of-information analysis.
- [ ] Task: Add optional adapter interfaces for spline-regression summaries.
- [ ] Task: Add optional adapter interfaces for policy-diffusion modelling.
- [ ] Task: Add tests that prove graceful skip or degradation when optional packages are absent.
- [ ] Task: Conductor - User Manual Verification 'Analytics adapters smoke test' [checkpoint: pending].
