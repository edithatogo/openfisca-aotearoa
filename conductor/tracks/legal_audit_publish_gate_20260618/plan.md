# Plan: Legal Audit and Publish Readiness Gates

## Phase 1: Readiness Model

- [x] Task: Inventory completed and active legislation tracks and their current evidence artifacts.
- [x] Task: Define readiness statuses for draft, implemented, tested, legally reviewed, publish-ready, and archived.
- [x] Task: Define a machine-readable readiness manifest schema.
- [ ] Task: Conductor - User Manual Verification 'Readiness model review' [checkpoint: pending].

## Phase 2: Report and Validation Tooling

- [x] Task: Add a script that reads Conductor track metadata, plans, git notes, and validation evidence.
- [x] Task: Generate a Markdown readiness report with citations, test evidence, and unresolved risks.
- [x] Task: Add schema validation tests for readiness manifests.
- [x] Task: Add fixture tests for report generation over representative active and archived tracks.

## Phase 3: Publish Gate Integration

- [x] Task: Add docs explaining archive and publish-readiness criteria.
- [x] Task: Add a non-interactive command that fails when required readiness evidence is missing.
- [x] Task: Run the gate against Tracks 9-14 and record exact residual gaps.
- [ ] Task: Conductor - User Manual Verification 'Publish readiness gate review' [checkpoint: pending].
