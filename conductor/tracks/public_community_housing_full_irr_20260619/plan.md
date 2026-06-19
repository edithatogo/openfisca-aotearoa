# Plan: Public and Community Housing Full Income-Related Rent Coverage

## Phase 1: Evidence Refresh and Gap Closure Design

- [ ] Task: Build a housing-specific source manifest for current Act sections, regulations, official guidance, market-rent caps, and transitional provisions.
- [ ] Task: Convert Track 22's partial-coverage notes into a traceability matrix with implemented, pending, no-model-impact, and out-of-scope decisions.
- [ ] Task: Identify existing housing variables, parameters, tests, and evidence artifacts that need to be extended rather than replaced.

## Phase 2: Parameters and Formula Design

- [ ] Task: Add or update effective-dated parameters for prescribed proportions, transition dates, caps, thresholds, and market-rent boundaries.
- [ ] Task: Design formula branches for assessment persons, household composition, weekly income, additional residents, higher-rent tests, and market-rent capping.
- [ ] Task: Document backwards-compatibility decisions for existing variable names, labels, and public API outputs.

## Phase 3: Test-First Implementation

- [ ] Task: Add failing YAML situation tests for base income-related rent, higher-rent, market-rent cap, additional-resident, and transition scenarios.
- [ ] Task: Implement the minimum formulas and parameters required to pass the housing situation tests.
- [ ] Task: Add unit tests or evidence checks for formula traceability and parameter citation completeness.

## Phase 4: Readiness and Currentness Gates

- [ ] Task: Update housing evidence artifacts for traceability, citations, parameters, formulas, and tests.
- [ ] Task: Run focused housing tests and readiness/currentness checks.
- [ ] Task: Run the broad CI-equivalent suite: uv run pytest --cov=openfisca_aotearoa --cov-report=xml --strict-markers --strict-config -W error.
- [ ] Task: Conductor - User Manual Verification 'Confirm full housing IRR coverage decisions and any remaining legal-currentness risks' [checkpoint: work_done]
