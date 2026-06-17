# Quality Gate Baseline

Generated: 2026-06-18

## Summary

This baseline captures the current Track 15 quality gate state after applying
two local gate fixes:

- `scalene` is no longer installed on Windows as part of the `dev` extra, so
  unrelated dev tools can install without requiring Microsoft C++ Build Tools.
- CI now invokes Complexipy with its current flag,
  `--max-complexity-allowed`.
- The OpenFisca Web API smoke test is skipped on Windows because the current
  OpenFisca web API path imports Gunicorn's Unix-only `grp` module.

## Gate Results

| Gate | Command | Result |
| --- | --- | --- |
| Ruff | `uv --no-cache run ruff check .` | Pass: `All checks passed!` |
| Basedpyright | `uv --no-cache run basedpyright openfisca_aotearoa` | Pass: `0 errors, 0 warnings, 0 notes` |
| Complexipy | `$env:PYTHONIOENCODING='utf-8'; uv --no-cache run --extra dev complexipy openfisca_aotearoa --max-complexity-allowed 15` | Pass: all functions within allowed complexity |
| Python pytest with coverage | `uv --no-cache run --extra dev pytest --cov=openfisca_aotearoa --cov-report=term-missing --strict-markers --strict-config -W error` | Pass on Windows: 5 passed, 1 skipped, total coverage 76% |
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
markers that cannot be encoded by `cp1252`.

### Web API smoke test on Windows

The OpenFisca web API executable imports Gunicorn, which imports the Unix-only
`grp` module. The API smoke test remains active on non-Windows platforms and is
skipped on Windows.

## Remaining Failures

### OpenFisca YAML encoding

Without UTF-8 mode, the OpenFisca YAML runner opens YAML files using the default
Windows `cp1252` encoding. Six family-scheme YAML files fail during collection:

- `openfisca_aotearoa/tests/income_tax/family_scheme/best_start.yaml`
- `openfisca_aotearoa/tests/income_tax/family_scheme/eligibility.yaml`
- `openfisca_aotearoa/tests/income_tax/family_scheme/family_scheme.yaml`
- `openfisca_aotearoa/tests/income_tax/family_scheme/family_tax_credit.yaml`
- `openfisca_aotearoa/tests/income_tax/family_scheme/in_work_tax_credit.yaml`
- `openfisca_aotearoa/tests/income_tax/family_scheme/minimum_family_tax_credit.yaml`

The next implementation step should provide a stable UTF-8 entry point for
Windows YAML test execution instead of relying on an interactive shell variable.

### OpenFisca YAML behaviour under UTF-8

With `PYTHONUTF8=1`, collection succeeds but the full OpenFisca suite still
fails:

- 25 YAML tests fail.
- 325 YAML/Python-collected tests pass.
- The OpenFisca runner also collects Python tests, so it hits the Windows web
  API limitation unless Python tests are excluded or the runner target is
  narrowed to YAML files only.

Representative failure classes:

- `family_tax_credit__eldest` receives invalid option `a`.
- Accommodation supplement situation formulas return object arrays that
  OpenFisca Core v44.7.0 cannot encode as enum arrays.

These are compatibility issues, not just test-runner setup issues.

## Coverage Baseline

The local Python pytest coverage gate now executes successfully on Windows. The
current total coverage is 76%, with the Web API smoke skipped on Windows. The
project does not currently enforce a coverage threshold in `pyproject.toml` or
CI, so this is a measured baseline rather than a failing threshold.

## Commands To Preserve

```text
uv --no-cache run ruff check .
uv --no-cache run basedpyright openfisca_aotearoa
$env:PYTHONIOENCODING='utf-8'; uv --no-cache run --extra dev complexipy openfisca_aotearoa --max-complexity-allowed 15
uv --no-cache run --extra dev pytest --cov=openfisca_aotearoa --cov-report=term-missing --strict-markers --strict-config -W error
$env:PYTHONUTF8='1'; uv --no-cache run --extra dev openfisca test openfisca_aotearoa/tests -c openfisca_aotearoa
```
