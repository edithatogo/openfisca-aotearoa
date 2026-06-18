# Plan: Legal Audit and Publish Readiness Gates

## Phase 1: Readiness Model

- [x] Task: Inventory completed and active legislation tracks and their current evidence artifacts. (96cef49)
- [x] Task: Define readiness statuses for draft, implemented, tested, legally reviewed, publish-ready, and archived. (96cef49)
- [x] Task: Define a machine-readable readiness manifest schema. (96cef49)
- [ ] Task: Conductor - User Manual Verification 'Readiness model review' [checkpoint: pending].

## Phase 2: Report and Validation Tooling

- [x] Task: Add a script that reads Conductor track metadata, plans, git notes, and validation evidence. (96cef49)
- [x] Task: Generate a Markdown readiness report with citations, test evidence, and unresolved risks. (96cef49)
- [x] Task: Add schema validation tests for readiness manifests. (96cef49)
- [x] Task: Add fixture tests for report generation over representative active and archived tracks. (96cef49)

## Phase 3: Publish Gate Integration

- [x] Task: Add docs explaining archive and publish-readiness criteria. (96cef49)
- [x] Task: Add a non-interactive command that fails when required readiness evidence is missing. (96cef49)
- [x] Task: Run the gate against Tracks 9-14 and record exact residual gaps. (96cef49)
- [ ] Task: Conductor - User Manual Verification 'Publish readiness gate review' [checkpoint: pending].
