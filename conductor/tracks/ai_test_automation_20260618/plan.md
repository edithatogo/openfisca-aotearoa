# Plan: AI-Assisted Test Automation

## Phase 1: Tool and Safety Audit

- [x] Task: Evaluate TestSprite installation, configuration, local execution, and CI compatibility. (0bed806)
- [x] Task: Define generated-test storage locations, metadata requirements, and review gates. (0bed806)
- [x] Task: Identify candidate source documents for first generated tests. (0bed806)
- [x] Task: Conductor - User Manual Verification 'AI test workflow safety review' [checkpoint: work_done].

## Phase 2: Candidate Generation Workflow

- [x] Task: Add a script or documented command to generate candidate test scenarios into a quarantine folder. (0bed806)
- [x] Task: Add metadata sidecars with source track, source document, prompt, generation timestamp, and reviewer. (0bed806)
- [x] Task: Add review checklist for accepting, editing, or rejecting generated tests. (0bed806)
- [x] Task: Add fixture-based tests for the candidate metadata format. (0bed806)

## Phase 3: Accepted Test Integration

- [x] Task: Promote a small reviewed candidate set into the normal OpenFisca test suite. (0bed806)
- [x] Task: Add deterministic CI checks for accepted generated tests. (0bed806)
- [x] Task: Document when generated tests should be regenerated or retired. (0bed806)
- [x] Task: Conductor - User Manual Verification 'Accepted AI-generated tests pass' [checkpoint: work_done].
