# Plan: AI-Assisted Test Automation

## Phase 1: Tool and Safety Audit

- [ ] Task: Evaluate TestSprite installation, configuration, local execution, and CI compatibility.
- [ ] Task: Define generated-test storage locations, metadata requirements, and review gates.
- [ ] Task: Identify candidate source documents for first generated tests.
- [ ] Task: Conductor - User Manual Verification 'AI test workflow safety review' [checkpoint: pending].

## Phase 2: Candidate Generation Workflow

- [ ] Task: Add a script or documented command to generate candidate test scenarios into a quarantine folder.
- [ ] Task: Add metadata sidecars with source track, source document, prompt, generation timestamp, and reviewer.
- [ ] Task: Add review checklist for accepting, editing, or rejecting generated tests.
- [ ] Task: Add fixture-based tests for the candidate metadata format.

## Phase 3: Accepted Test Integration

- [ ] Task: Promote a small reviewed candidate set into the normal OpenFisca test suite.
- [ ] Task: Add deterministic CI checks for accepted generated tests.
- [ ] Task: Document when generated tests should be regenerated or retired.
- [ ] Task: Conductor - User Manual Verification 'Accepted AI-generated tests pass' [checkpoint: pending].
