# Standalone Validation

Generated: 2026-06-18

## Commands

- `uv sync --extra dev --locked`
- `uv run --extra dev python scripts/smoke_workspace.py`
- `uv run pytest openfisca_aotearoa/tests/test_simulation.py openfisca_aotearoa/tests/test_api.py --strict-markers --strict-config -W error`
- `uv build`

## Result

All commands passed.

The focused pytest run collected five tests:

- `openfisca_aotearoa/tests/test_simulation.py`: four passed.
- `openfisca_aotearoa/tests/test_api.py`: one skipped.

The build command produced both source distribution and wheel artifacts under
ignored `dist/` output.
