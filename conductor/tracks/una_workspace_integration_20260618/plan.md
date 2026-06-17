# Plan: Una and UV Workspace Integration

## Phase 1: Workspace Boundary Audit

- [x] Task: Inspect current package metadata, lockfiles, `.python-version`, Make targets, and CI install commands. (0f370f6)
- [~] Task: Inspect parent `legal-nz` workspace expectations without modifying parent files from this nested repo.
- [ ] Task: Decide the minimum safe `una` integration surface for this repository.
- [ ] Task: Conductor - User Manual Verification 'Workspace boundary and Una design review' [checkpoint: pending].

## Phase 2: Metadata and Command Implementation

- [ ] Task: Add or update workspace metadata for `uv` and `una` while preserving package build metadata.
- [ ] Task: Add documented commands for standalone and parent-workspace install, lint, tests, docs, and build.
- [ ] Task: Add smoke validation for local path resolution and workspace command execution.
- [ ] Task: Keep generated or machine-local workspace artifacts out of version control unless required.

## Phase 3: Validation and Documentation

- [ ] Task: Run standalone `uv sync`, focused tests, and package build checks.
- [ ] Task: Run parent-workspace command checks where safe and document any parent-repo-only follow-up.
- [ ] Task: Update README or developer docs with supported workspace workflows.
- [ ] Task: Conductor - User Manual Verification 'Una workspace commands pass' [checkpoint: pending].
