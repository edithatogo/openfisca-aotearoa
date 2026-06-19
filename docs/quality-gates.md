# Quality Gates

This repository uses `uv` for local and CI quality gates.

## Default Gate

```text
make quality
```

The default gate runs:

- `uv run ruff check .`
- `uv run basedpyright openfisca_aotearoa`
- `uv run python scripts/run_complexity_gate.py`
- `uv run pytest --cov=openfisca_aotearoa --cov-report=term-missing`
- `uv run python scripts/run_openfisca_yaml_tests.py` against the focused
  OpenFisca Core v44 compatibility YAML fixtures.

## OpenFisca YAML Tests

Use the project wrapper rather than calling the OpenFisca YAML runner directly
on Windows:

```text
uv run python scripts/run_openfisca_yaml_tests.py path/to/test.yaml
```

The wrapper sets `PYTHONUTF8=1` and `PYTHONIOENCODING=utf-8` for the child
process so fixtures containing macrons are decoded consistently.

The full legacy YAML suite remains available with:

```text
uv run python scripts/run_openfisca_yaml_tests.py openfisca_aotearoa/tests
```

As of 2026-06-19, the focused v44 compatibility YAML gate passes and the full
legacy YAML suite still has unrelated accommodation supplement fixture failures.
Those failures should be handled as a separate formula/test-data remediation
track rather than hidden inside the OpenFisca Core compatibility gate.

## Type-Checking Boundary

`basedpyright` is enforced for the package outside
`openfisca_aotearoa/variables`. The variable tree remains explicitly excluded
because the legacy OpenFisca formula style needs a separate typed-formula
migration. This keeps the gate strict for the newer API, evidence,
microsimulation, simulation, and readiness modules while preserving a clear
debt boundary.
