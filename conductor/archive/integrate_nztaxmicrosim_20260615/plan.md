# Plan: Integrate nztaxmicrosim Rules

## Phase 1: Reference Ingestion and Mapping

- [x] Task: Extract tax parameters and rules from `nztaxmicrosim` repository.
- [x] Task: Map historical tax bracket parameters and thresholds to OpenFisca parameters YAML.
- [x] Task: Review fix - correct the 2024 transitional individual income tax brackets to match current IRD bands.
- [x] Task: Conductor - User Manual Verification 'Verify tax parameters mapped' [checkpoint: work_done].

## Phase 2: Python Rules Coding

- [x] Task: Write situation tests in `openfisca_aotearoa/tests/` verifying calculation accuracy against historical and current tax years.
- [x] Task: Codify the Python tax calculations under `openfisca_aotearoa/variables/` to pass the tests.
- [x] Task: Review fix - add 2024 transitional-rate situation coverage for affected bands.
- [x] Task: Conductor - User Manual Verification 'Verify tax calculations pass' (Protocol in workflow.md) [checkpoint: work_done].

## Audit Note

No task commit SHA is recorded in this archived track because the Conductor workspace is currently uncommitted and contains concurrent unrelated changes.
