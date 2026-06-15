# Plan: Integrate nztaxmicrosim Rules

## Phase 1: Reference Ingestion and Mapping
- [x] Task: Extract tax parameters and rules from `nztaxmicrosim` repository
- [x] Task: Map historical tax bracket parameters and thresholds to OpenFisca parameters YAML
- [x] Task: Conductor - User Manual Verification 'Verify tax parameters mapped' [checkpoint: work_done]

## Phase 2: Python Rules Coding (TDD)
- [x] Task: Write failing situation tests in `openfisca_aotearoa/tests/` verifying calculation accuracy against historical tax years
- [x] Task: Codify the Python tax calculations under `openfisca_aotearoa/variables/` to pass the tests
- [x] Task: Conductor - User Manual Verification 'Verify tax calculations pass' (Protocol in workflow.md) [checkpoint: work_done]
