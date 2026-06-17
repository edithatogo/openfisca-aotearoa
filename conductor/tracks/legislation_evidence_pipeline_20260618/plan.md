# Plan: Legislation Evidence Pipeline Integrations

## Phase 1: Evidence Contract

- [ ] Task: Inventory current citations in variables, parameters, specs, and roadmap documents.
- [ ] Task: Define an evidence manifest schema for legislation references, source documents, retrieval dates, and verification status.
- [ ] Task: Define tool boundaries for `nz-legislation`, `sourceright`, `nlp-policy-nz`, and `fyi-cli`.
- [ ] Task: Conductor - User Manual Verification 'Evidence manifest schema review' [checkpoint: pending].

## Phase 2: Citation and Legislation Retrieval

- [ ] Task: Add a script or module that extracts citations from variables and parameters.
- [ ] Task: Add `sourceright` validation/report integration with machine-readable output.
- [ ] Task: Add `nz-legislation` retrieval integration or documented fixture mode.
- [ ] Task: Add tests for citation extraction and fixture-based validation.

## Phase 3: Policy Intent and OIA Evidence

- [ ] Task: Add optional `nlp-policy-nz` search adapter with offline fixture tests.
- [ ] Task: Add optional `fyi-cli` evidence adapter with credential-safe boundaries.
- [ ] Task: Generate a combined evidence report for a representative Act track.
- [ ] Task: Document manual review steps for evidence that cannot be verified locally.
- [ ] Task: Conductor - User Manual Verification 'Evidence pipeline smoke test' [checkpoint: pending].
