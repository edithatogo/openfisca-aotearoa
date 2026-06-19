# Quality Gate Baseline

Generated: 2026-06-18
Updated: 2026-06-19

## Summary

This baseline captures the Track 15 quality gate state after applying the v44
compatibility fix and stable gate wrappers:

- `scalene` is no longer installed on Windows as part of the `dev` extra, so
  unrelated dev tools can install without requiring Microsoft C++ Build Tools.
- CI now invokes Complexipy with its current flag,
  `--max-complexity-allowed`.
- The OpenFisca Web API smoke test is skipped on Windows because the current
  OpenFisca web API path imports Gunicorn's Unix-only `grp` module.
- `scripts/run_openfisca_yaml_tests.py` runs OpenFisca YAML fixtures with
  UTF-8 process encoding.
- `scripts/run_complexity_gate.py` runs Complexipy with UTF-8 process encoding
  so Rich output does not fail on Windows `cp1252` consoles.

## Gate Results

| Gate | Command | Result |
| --- | --- | --- |
| Ruff | `uv run ruff check .` | Pass: `All checks passed!` |
| Basedpyright | `uv run basedpyright openfisca_aotearoa` | Pass: `0 errors, 0 warnings, 0 notes` |
| Complexipy | `uv run python scripts/run_complexity_gate.py` | Pass: all functions within allowed complexity |
| Python pytest with coverage | `uv run pytest --cov=openfisca_aotearoa --cov-report=term-missing` | Pass on Windows: 59 passed, 1 skipped, total coverage 79% |
| Focused OpenFisca v44 YAML tests | `uv run python scripts/run_openfisca_yaml_tests.py openfisca_aotearoa/tests/social_security/accommodation_supplement/2018/situation.yaml openfisca_aotearoa/tests/income_tax/family_scheme/family_tax_credit.yaml` | Pass on Windows: 9 passed |
| OpenFisca YAML tests, default Windows encoding | `uv --no-cache run --extra dev openfisca test openfisca_aotearoa/tests -c openfisca_aotearoa` | Fail during collection: 6 family-scheme YAML files raise `UnicodeDecodeError` under `cp1252` |
| OpenFisca YAML tests, forced UTF-8 | `$env:PYTHONUTF8='1'; uv --no-cache run --extra dev openfisca test openfisca_aotearoa/tests -c openfisca_aotearoa` | Fail after collection: 25 YAML failures, 325 passed, 1 Python API-test error when the runner includes Python tests |

## Baseline Fixes Applied

### Windows dev-extra install

Plain `uv --no-cache run --extra dev ...` initially failed before executing
Complexipy or pytest-cov because `scalene==2.3.0` attempted a Windows native
build and required Microsoft C++ Build Tools. `scalene` is a profiling tool, not
a strict quality-gate dependency, so the `dev` extra now marks it as
non-Windows:

```toml
"scalene>=1.5.0; sys_platform != 'win32'"
```

### Complexipy CLI

The configured CI command used `--max-complexity`, but Complexipy now accepts
`--max-complexity-allowed`. The CI workflow now uses the accepted flag.

On Windows, Complexipy also needs UTF-8 console output because Rich prints pass
markers that cannot be encoded by `cp1252`. The project wrapper now owns this
environment setup.

### Focused v44 YAML compatibility

The focused compatibility YAML gate passes after:

- `accommodation_supplement__situation` was changed to return integer enum
  indices consistently.
- `family_tax_credit.yaml` is run through the UTF-8 wrapper and the current
  branch's `populations.ADD` aggregation fix.

### Web API smoke test on Windows

The OpenFisca web API executable imports Gunicorn, which imports the Unix-only
`grp` module. The API smoke test remains active on non-Windows platforms and is
skipped on Windows.

## Remaining Legacy Failures

### OpenFisca YAML encoding

Without UTF-8 mode, the OpenFisca YAML runner opens YAML files using the default
Windows `cp1252` encoding. Six family-scheme YAML files fail during collection:

- `openfisca_aotearoa/tests/income_tax/family_scheme/best_start.yaml`
- `openfisca_aotearoa/tests/income_tax/family_scheme/eligibility.yaml`
- `openfisca_aotearoa/tests/income_tax/family_scheme/family_scheme.yaml`
- `openfisca_aotearoa/tests/income_tax/family_scheme/family_tax_credit.yaml`
- `openfisca_aotearoa/tests/income_tax/family_scheme/in_work_tax_credit.yaml`
- `openfisca_aotearoa/tests/income_tax/family_scheme/minimum_family_tax_credit.yaml`

The stable UTF-8 entry point is now `scripts/run_openfisca_yaml_tests.py`.
Direct use of the upstream runner without UTF-8 mode still fails on Windows and
is intentionally not the documented project gate.

### OpenFisca YAML behaviour under UTF-8

With `PYTHONUTF8=1`, collection succeeds but the full OpenFisca suite still
fails:

- 25 YAML tests fail.
- 325 YAML/Python-collected tests pass.
- The OpenFisca runner also collects Python tests, so it hits the Windows web
  API limitation unless Python tests are excluded or the runner target is
  narrowed to YAML files only.

Historical representative failure classes:

- `family_tax_credit__eldest` receives invalid option `a`.
- Accommodation supplement situation formulas return object arrays that
  OpenFisca Core v44.7.0 cannot encode as enum arrays.

Both representative v44 compatibility failures are fixed in the focused gate.
The remaining full-suite failures are broader accommodation supplement
formula/test-data mismatches and should be remediated separately.

These are compatibility issues, not just test-runner setup issues.

## Coverage Baseline

The local Python pytest coverage gate executes successfully on Windows. The
current total coverage is 79%, with the Web API smoke skipped on Windows. The
project does not currently enforce a coverage threshold in `pyproject.toml` or
CI, so this is a measured baseline rather than a failing threshold.

## Commands To Preserve

```text
uv run ruff check .
uv run basedpyright openfisca_aotearoa
uv run python scripts/run_complexity_gate.py
uv run pytest --cov=openfisca_aotearoa --cov-report=term-missing
uv run python scripts/run_openfisca_yaml_tests.py openfisca_aotearoa/tests/social_security/accommodation_supplement/2018/situation.yaml openfisca_aotearoa/tests/income_tax/family_scheme/family_tax_credit.yaml
```
