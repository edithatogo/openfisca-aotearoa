# Standalone Validation

Generated: 2026-06-18
Updated: 2026-06-19

## Commands

- `uv sync --extra dev --locked`
- `uv run --extra dev python scripts/smoke_workspace.py`
- `uv run pytest openfisca_aotearoa/tests/test_simulation.py openfisca_aotearoa/tests/test_api.py --strict-markers --strict-config -W error`
- `uv build`

## Result

All commands passed.

The workspace smoke command was rerun on 2026-06-19 and passed:

- `uv lock --check`
- `uv run --extra dev una --help`
- local package import and `una` version check
- parent-style `uv --directory openfisca-aotearoa ...` checks

The focused pytest run collected five tests:

- `openfisca_aotearoa/tests/test_simulation.py`: four passed.
- `openfisca_aotearoa/tests/test_api.py`: one skipped.

The build command produced both source distribution and wheel artifacts under
ignored `dist/` output.
