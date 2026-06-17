# Plan: Codify Income Tax Act 2007 Core Rules

## Phase 1: Audit and Mapping

- [x] Task: Map existing income tax variables and parameters to Income Tax Act 2007 Parts and Subparts. (6929e0f)
- [x] Task: Identify missing core individual tax, family scheme, Working for Families, and credit rules not covered by Tax Administration Act compliance work. (6929e0f)
- [x] Task: Conductor - User Manual Verification 'Income Tax Act gap map review' [checkpoint: work_done]. (6929e0f)

## Phase 2: Implementation

- [x] Task: Add or update variables and parameters with explicit legislation.govt.nz citations. (a518c75)
  - Implemented: core Part C income component variables, Part D deduction component variables, and corrected Schedule 1 individual tax bracket activation.
- [x] Task: Add situation tests for representative tax, credit, and family scheme calculations. (a518c75)
  - Verified: individual tax component-to-tax flow plus existing Working for Families entitlement scenarios.
- [ ] Task: Conductor - User Manual Verification 'Income Tax Act rules load and test' [checkpoint: pending].
  - Pending: full `tests/income_tax/family_scheme` collection is blocked on Windows by existing UTF-8 YAML decoded as cp1252; focused Track 14 verification passed 14 tests.
