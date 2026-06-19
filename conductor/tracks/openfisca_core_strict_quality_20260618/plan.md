# Plan: OpenFisca Core Upgrade and Strict Quality Gates

## Phase 1: Audit and Baseline

- [x] Task: Inventory current dependency pins, OpenFisca Core version, and API usage across variables, parameters, tests, and docs. (94b5ec8)
- [x] Task: Run the current quality gate set and capture baseline failures for `ruff`, `basedpyright`, `complexipy`, coverage, and OpenFisca YAML tests. (41aa259)
- [x] Task: Compare current OpenFisca Core usage against v44+ migration requirements and list required code changes. (3b852f3)
- [x] Task: Conductor - User Manual Verification 'Core upgrade and quality baseline review' [checkpoint: work_done].

## Phase 2: Compatibility Implementation

- [x] Task: Add compatibility shims or code updates needed for the selected OpenFisca Core upgrade path.
- [x] Task: Update dependency metadata and lockfiles using `uv` without introducing unrelated dependency churn.
- [x] Task: Add focused regression tests for upgraded variable period handling, parameter loading, and YAML test execution.
- [x] Task: Run targeted OpenFisca test suites and record pass/fail evidence.

## Phase 3: Strict Quality Gates

- [x] Task: Tighten `basedpyright` settings one module group at a time, with scoped excludes for unresolved legacy debt.
- [x] Task: Ensure `ruff`, `basedpyright`, `complexipy`, and coverage commands are available via documented scripts or Make targets.
- [x] Task: Wire the tightened quality gates into CI without blocking on unrelated external services.
- [x] Task: Conductor - User Manual Verification 'Strict quality gates load and pass' [checkpoint: work_done].
