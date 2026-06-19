# Situation-Test Evidence

Focused evidence pipeline validation rerun on 2026-06-19:

```text
uv run pytest openfisca_aotearoa\tests\test_evidence.py --strict-markers --strict-config -W error
```

Result:

```text
6 passed
```

Static validation rerun on 2026-06-19:

```text
uv run ruff check openfisca_aotearoa\evidence.py openfisca_aotearoa\tests\test_evidence.py
uv run basedpyright openfisca_aotearoa\evidence.py
```

Results:

```text
Ruff: All checks passed.
Basedpyright: 0 errors, 0 warnings, 0 notes.
```
