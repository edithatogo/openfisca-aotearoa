# Plan: Legal Audit and Publish Readiness Gates

## Phase 1: Readiness Model

- [ ] Task: Inventory completed and active legislation tracks and their current evidence artifacts.
- [ ] Task: Define readiness statuses for draft, implemented, tested, legally reviewed, publish-ready, and archived.
- [ ] Task: Define a machine-readable readiness manifest schema.
- [ ] Task: Conductor - User Manual Verification 'Readiness model review' [checkpoint: pending].

## Phase 2: Report and Validation Tooling

- [ ] Task: Add a script that reads Conductor track metadata, plans, git notes, and validation evidence.
- [ ] Task: Generate a Markdown readiness report with citations, test evidence, and unresolved risks.
- [ ] Task: Add schema validation tests for readiness manifests.
- [ ] Task: Add fixture tests for report generation over representative active and archived tracks.

## Phase 3: Publish Gate Integration

- [ ] Task: Add docs explaining archive and publish-readiness criteria.
- [ ] Task: Add a non-interactive command that fails when required readiness evidence is missing.
- [ ] Task: Run the gate against Tracks 9-14 and record exact residual gaps.
- [ ] Task: Conductor - User Manual Verification 'Publish readiness gate review' [checkpoint: pending].
