# Manual Verification

Manual checkpoints completed on 2026-06-19:

- Core upgrade and quality baseline review.
- Strict quality gates load and pass.

The implemented gate boundary is explicit:

- Passing: Ruff, Basedpyright over the non-variable package, Complexipy,
  Python pytest with coverage, and focused OpenFisca Core v44 YAML fixtures.
- Deferred: full legacy OpenFisca YAML suite remediation outside the focused
  v44 compatibility fixtures.
