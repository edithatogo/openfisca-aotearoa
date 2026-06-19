# Situation-Test Evidence

Focused OpenFisca Core v44 compatibility gate:

```text
uv run python scripts/run_openfisca_yaml_tests.py openfisca_aotearoa/tests/social_security/accommodation_supplement/2018/situation.yaml openfisca_aotearoa/tests/income_tax/family_scheme/family_tax_credit.yaml
```

Result on 2026-06-19:

```text
9 passed in 1.49s
```

Python quality gate:

```text
uv run pytest --cov=openfisca_aotearoa --cov-report=term-missing
```

Result on 2026-06-19:

```text
59 passed, 1 skipped, total coverage 79%
```

Static quality gates:

```text
uv run ruff check .
uv run basedpyright openfisca_aotearoa
uv run python scripts/run_complexity_gate.py
```

Results on 2026-06-19:

```text
Ruff: All checks passed.
Basedpyright: 0 errors, 0 warnings, 0 notes.
Complexipy: All functions are within the allowed complexity.
```
