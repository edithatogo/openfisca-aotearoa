# Parent-Root Validation

Generated: 2026-06-18
Updated: 2026-06-19

## Commands run from `legal-nz`

- `uv --directory openfisca-aotearoa sync --extra dev --locked`
- `uv --directory openfisca-aotearoa run --extra dev python scripts/smoke_workspace.py`
- `npm --prefix openfisca-aotearoa run docs:check`
- `uv --directory openfisca-aotearoa build`

## Result

All parent-root commands passed.

`uv run --extra dev python scripts/smoke_workspace.py` was rerun from the nested
repository on 2026-06-19 and again verified the parent-style
`uv --directory openfisca-aotearoa ...` command path.

The smoke script verified that `uv --directory openfisca-aotearoa` changes the
working directory into the submodule before running path-sensitive tools.

## Parent-owned follow-up

The parent `legal-nz` repository still has no root `pyproject.toml` or
parent-owned `uv.lock`. A true parent uv workspace remains a separate
parent-repository decision.

Read-only parent status during validation showed existing parent-level changes:

- `? corpus-law-nz`
- `M open_social_data`
- `M openfisca-aotearoa`
- `M sm-govt-nz`
- `M sourceright`

Only `openfisca-aotearoa` is in scope for this Track 16 implementation. The
parent repository will need a separate commit if it should record the updated
submodule pointer.
