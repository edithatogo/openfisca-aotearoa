# Parent Workspace Audit

Generated: 2026-06-18

## Scope

This audit inspects the parent `legal-nz` workspace as read-only context for
Track 16. No parent files were modified.

Parent workspace root:
`C:/Users/60217257/OneDrive - Flinders/repos/legal-nz`

Nested repository:
`openfisca-aotearoa`

## Parent Git State

The parent repository is on branch `main` and already has unrelated modified
submodule state:

- `corpus-law-nz` is untracked or not fully registered in parent status.
- `open_social_data` is modified.
- `openfisca-aotearoa` is modified because this nested repository has new Track
  16 commits.
- `sm-govt-nz` is modified.
- `sourceright` is modified.

Track 16 should not try to normalize parent status from this nested repository.

## Parent Metadata Files

The parent root currently has:

- `.gitignore`.
- `.gitmodules`.
- `README.md`.
- `pytest.ini`.
- `QUALITY_STANDARDS.md`.
- `subagents.yaml`.
- `swarm-workspaces.yaml`.
- `workspace-catalog.md`.

The parent root does not currently have:

- `pyproject.toml`.
- `uv.lock`.
- `uv.toml`.
- `.python-version`.
- `una` configuration files found by filename search.

## Submodule Boundary

Parent `.gitmodules` registers this repository as a submodule:

```ini
[submodule "openfisca-aotearoa"]
    path = openfisca-aotearoa
    url = https://github.com/edithatogo/openfisca-aotearoa.git
    branch = main
```

This means nested commits should be made inside `openfisca-aotearoa`, while the
parent repository should only record a submodule pointer update in a separate
parent-level commit when the user asks for parent cleanup or integration.

## Parent Swarm Inventory

`swarm-workspaces.yaml` lists `openfisca-aotearoa` as:

- `path: openfisca-aotearoa`.
- `conductor: unknown`.
- `swarm_config: inherited:root`.
- `subagents: inherited:root`.
- `task_plan: generated:root`.
- Approved submodule on 2026-06-15.

The parent inventory has not yet been refreshed to recognize the nested
repository's Conductor surface.

## Parent Workspace Catalog

`workspace-catalog.md` documents a broader workspace standard around Python
`>=3.11`, `uv`, Ruff, type checking, and coverage, but the visible summary does
not currently include `openfisca-aotearoa` in the Python version/package-manager
comparison table. This repository was promoted to an approved submodule later
than some of the catalog entries.

## Parent Test Configuration

Parent `pytest.ini` explicitly excludes submodule directories from root pytest
collection, including:

- `openfisca-aotearoa`.
- `open_social_data`.
- `sm-govt-nz`.
- `sourceright`.

Parent-level pytest is therefore not expected to run this package's tests.

## Parent Expectations For Track 16

The safe nested-repo implementation surface is:

1. Keep this repository independently installable with `uv sync` and
   `uv sync --extra dev`.
2. Add local metadata/docs that make the submodule usable from a parent working
   directory without requiring parent repo edits.
3. Document parent commands as examples using `uv --project openfisca-aotearoa`
   or `cd openfisca-aotearoa`, not as parent-owned workflows.
4. Avoid adding parent `pyproject.toml`, parent `uv.lock`, or parent `una`
   config from this nested repository.

## Parent Follow-Up Candidates

These are parent-repo follow-ups, not Track 16 nested-repo edits:

- Refresh `swarm-workspaces.yaml` so `openfisca-aotearoa` points at
  `openfisca-aotearoa/conductor/tracks.md`.
- Add `openfisca-aotearoa` to `workspace-catalog.md` if the catalog remains the
  source of truth for workspace package-manager status.
- Decide whether the parent `legal-nz` root should gain a workspace-level
  `pyproject.toml`, `uv.lock`, or `una` config. That decision affects multiple
  submodules and should not be made inside this nested repository alone.
