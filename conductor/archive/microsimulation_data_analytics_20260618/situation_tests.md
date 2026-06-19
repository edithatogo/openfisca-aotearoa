# Situation-Test Evidence

Focused validation rerun on 2026-06-19:

```text
uv run pytest openfisca_aotearoa/tests/test_microsimulation_adapters.py openfisca_aotearoa/tests/test_microsimulation_contract.py openfisca_aotearoa/tests/test_microsimulation_runner.py --strict-markers --strict-config -W error
```

Result:

```text
19 passed
```

Static validation rerun on 2026-06-19:

```text
uv run ruff check openfisca_aotearoa\microsimulation.py openfisca_aotearoa\tests\test_microsimulation_adapters.py openfisca_aotearoa\tests\test_microsimulation_contract.py openfisca_aotearoa\tests\test_microsimulation_runner.py
uv run basedpyright openfisca_aotearoa\microsimulation.py
```

Results:

```text
Ruff: All checks passed.
Basedpyright: 0 errors, 0 warnings, 0 notes.
```
