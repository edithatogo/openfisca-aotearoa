# Plan: Legislation Evidence Pipeline Integrations

## Phase 1: Evidence Contract

- [x] Task: Inventory current citations in variables, parameters, specs, and roadmap documents.
- [x] Task: Define an evidence manifest schema for legislation references, source documents, retrieval dates, and verification status.
- [x] Task: Define tool boundaries for `nz-legislation`, `sourceright`, `nlp-policy-nz`, and `fyi-cli`.
- [x] Task: Conductor - User Manual Verification 'Evidence manifest schema review' [checkpoint: work_done].

## Phase 2: Citation and Legislation Retrieval

- [x] Task: Add a script or module that extracts citations from variables and parameters.
- [x] Task: Add `sourceright` validation/report integration with machine-readable output.
- [x] Task: Add `nz-legislation` retrieval integration or documented fixture mode.
- [x] Task: Add tests for citation extraction and fixture-based validation.

## Phase 3: Policy Intent and OIA Evidence

- [x] Task: Add optional `nlp-policy-nz` search adapter with offline fixture tests.
- [x] Task: Add optional `fyi-cli` evidence adapter with credential-safe boundaries.
- [x] Task: Generate a combined evidence report for a representative Act track.
- [x] Task: Document manual review steps for evidence that cannot be verified locally.
- [x] Task: Conductor - User Manual Verification 'Evidence pipeline smoke test' [checkpoint: work_done].
