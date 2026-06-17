# Workspace Metadata Audit

Generated: 2026-06-18

## Scope

This audit covers the current nested package state before adding `uv` workspace
or `una` integration. It intentionally inspects parent workspace files as
read-only context only; parent repository edits belong in a separate parent-repo
commit.

## Package Metadata

- `pyproject.toml` uses Hatchling with `hatch-vcs`:
  `build-backend = "hatchling.build"`.
- Project name is `openfisca-aotearoa`.
- Python requirement is `>=3.11`.
- Runtime dependencies include `openfisca-core[web-api] >=44.6.0`, `pandas`,
  `polars`, `pydantic`, `loguru`, `orjson`, `numpy`, `safetensors`, and `ty`.
- Development dependencies are declared under `[project.optional-dependencies]`
  as the `dev` extra.
- `scalene` is already guarded with `sys_platform != 'win32'`, so Windows
  `uv sync --extra dev` can install quality-gate tooling without native build
  tools.
- There is currently no `[tool.uv]`, `[tool.uv.workspace]`, `[tool.una]`, or
  `una` dependency declaration in this repository.

## Lockfiles And Python Version

- `uv.lock` is present and resolves the package with
  `requires-python = ">=3.11"`.
- No `.python-version` file is present in the nested repository.
- `.gitignore` currently ignores `.python-version`, so a project-local Python
  pin would not be versioned unless that ignore rule changes.
- Local tool versions observed during audit:
  - `uv 0.11.21`.
  - `python 3.11.15`.

## Make Targets

`Makefile` is present but remains legacy-oriented:

- `install` uses `pip install --editable .[dev] --upgrade`.
- `build` uses `python -m build` and reinstalls from `dist`.
- `format` uses `isort`, `autopep8`, and `pyupgrade`.
- `lint` uses `flake8`, `pylint`, and `yamllint`.
- `qtest` uses `openfisca test` directly.
- `serve` uses `openfisca serve`.

These targets do not match the modern `uv`, Ruff, Basedpyright, and Complexipy
quality gate path used by `ci.yml`.

## GitHub Actions Install And Command Paths

### `ci.yml`

The current quality workflow is already `uv`-based:

- Installs `uv` with `astral-sh/setup-uv@v3`.
- Installs Python with `uv python install 3.11`.
- Installs dependencies with `uv sync --extra dev`.
- Runs Ruff through `astral-sh/ruff-action@v1`.
- Runs Basedpyright with `uv run basedpyright openfisca_aotearoa`.
- Runs Complexipy with
  `uv run complexipy openfisca_aotearoa --max-complexity-allowed 15`.
- Runs pytest coverage with
  `uv run pytest --cov=openfisca_aotearoa --cov-report=xml --strict-markers --strict-config -W error`.

### Legacy validation and deployment workflows

The reusable workflows still use `actions/setup-python`, cache the interpreter
environment, and call Make targets:

- `build.yml` runs `make build`.
- `validate.yml` runs `make check-syntax-errors`, `make lint`, and `make test`.
- `deploy.yml` depends on `validate.yml` and restores the cached build
  environment before uploading with `twine`.

These workflows are outside the minimum safe workspace metadata audit but should
be considered when later wiring workspace-aware commands.

### Documentation workflow

`docs.yml` is mostly Node-based and uses `python -m pip install PyYAML` only for
the parameter catalog generator. It does not currently consume `uv` workspace
metadata.

## Current Workspace Gaps

- The README says "UV Workspaces" but the nested package does not currently
  declare `uv` workspace metadata.
- There is no local `una` configuration or documented `una` command path.
- The Makefile and reusable validation workflows still encode older
  pip/flake8/pylint/yamllint assumptions.
- `.python-version` is ignored, so Python version pinning must either stay in
  CI/docs or be made explicit through a deliberate ignore-rule change.
- Parent-workspace integration cannot be inferred from this nested repository
  alone; it needs a read-only parent audit before deciding where `una` belongs.

## Next Task Inputs

The next Track 16 task should inspect the parent `legal-nz` workspace for:

- Existing `pyproject.toml`, `uv.lock`, `uv.toml`, `una` config, or workspace
  catalog files.
- Whether `openfisca-aotearoa` is listed as a workspace member, submodule, or
  managed package.
- Existing parent commands for install, lint, tests, docs, and build.
- Any parent-level generated artifacts that this nested repo should avoid
  owning.
