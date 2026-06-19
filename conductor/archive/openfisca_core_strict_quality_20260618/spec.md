# Specification: OpenFisca Core Upgrade and Strict Quality Gates

## Purpose

Bring the project closer to the roadmap's must-have quality baseline by auditing
OpenFisca Core compatibility, tightening static typing, and making quality gates
explicit and reproducible in local and CI workflows.

## Requirements

- Audit the current OpenFisca Core dependency and runtime API usage against the
  roadmap target of OpenFisca Core v44+.
- Identify compatibility changes needed before upgrading, including variable
  period handling, test runner behaviour, and parameter loading.
- Move `basedpyright` from the current permissive baseline toward stricter
  checks without blocking legacy modules all at once.
- Ensure `ruff`, `basedpyright`, `complexipy`, and coverage commands have clear
  local and CI entry points.
- Add narrow regression tests or smoke checks for compatibility changes.
- Document any intentional deferrals with exact blockers.

## Non-Goals

- Rewriting all legacy OpenFisca variables in one pass.
- Replacing OpenFisca Core with another rules engine.
- Changing legislative formulas except where required for compatibility.
