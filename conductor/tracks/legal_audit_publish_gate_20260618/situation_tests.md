# Situation-Test Evidence

Focused validation rerun on 2026-06-19:

```text
uv run pytest openfisca_aotearoa\tests\test_readiness.py --strict-markers --strict-config -W error
```

Result:

```text
8 passed
```

Static validation rerun on 2026-06-19:

```text
uv run ruff check openfisca_aotearoa\readiness.py openfisca_aotearoa\tests\test_readiness.py scripts\check_publish_readiness.py
uv run basedpyright openfisca_aotearoa\readiness.py openfisca_aotearoa\tests\test_readiness.py scripts\check_publish_readiness.py
```

Results:

```text
Ruff: All checks passed.
Basedpyright: 0 errors, 0 warnings, 0 notes.
```
