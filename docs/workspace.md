# UV and una workspace commands

OpenFisca Aotearoa is a standalone Python package that can also be checked out as
the `openfisca-aotearoa` submodule inside the parent `legal-nz` repository. The
package owns its Python environment, lockfile, and workspace metadata. The parent
repository can invoke those commands, but it does not own this package's
`uv.lock`.

The local workspace is intentionally self-contained:

```toml
[tool.uv.workspace]
members = ["."]

[tool.una]
namespace = "openfisca_aotearoa"
```

`una` is installed as a development tool through the `dev` extra. The package
does not enable the `hatch-una` build hook because there are no local package
members to rewrite for publication.

`una tree` and `una sync` are not part of the current flat-package workflow.
With `una==0.7.0`, those commands expect workspace members to be package
directories. This repository deliberately uses the uv self-workspace member
pattern (`members = ["."]`) to preserve standalone package behavior.

## Standalone package workflow

Run these commands from the `openfisca-aotearoa` repository root.

### Install dependencies

```sh
uv sync --extra dev --locked
```

Use `uv sync --extra dev` when intentionally updating the lockfile.

### Check una availability

```sh
uv run --extra dev una --help
```

Use una package-management commands only after introducing real local package
member directories and updating `[tool.uv.workspace].members` accordingly.

### Smoke validation

```sh
uv run --extra dev python scripts/smoke_workspace.py
```

### Lint and type-check

```sh
uv run ruff check .
uv run basedpyright
uv run complexipy openfisca_aotearoa --max-complexity 15
```

### Test

```sh
uv run pytest
uv run openfisca test openfisca_aotearoa/tests
```

### Docs

```sh
npm install --prefix docs-site --no-audit --no-fund
npm run docs:check
npm run docs:build
```

### Build

```sh
uv build
```

## Parent repository workflow

Run these commands from the parent `legal-nz` repository root. They change into
the submodule before running so path-sensitive tools read this package's
environment, workspace metadata, and lockfile.

### Install dependencies

```sh
uv --directory openfisca-aotearoa sync --extra dev --locked
```

### Check una availability

```sh
uv --directory openfisca-aotearoa run --extra dev una --help
```

### Lint and type-check

```sh
uv --directory openfisca-aotearoa run ruff check .
uv --directory openfisca-aotearoa run basedpyright
uv --directory openfisca-aotearoa run complexipy openfisca_aotearoa --max-complexity 15
```

### Test

```sh
uv --directory openfisca-aotearoa run pytest
uv --directory openfisca-aotearoa run openfisca test openfisca_aotearoa/tests
```

### Docs

```sh
npm install --prefix openfisca-aotearoa/docs-site --no-audit --no-fund
npm --prefix openfisca-aotearoa run docs:check
npm --prefix openfisca-aotearoa run docs:build
```

### Build

```sh
uv --directory openfisca-aotearoa build
```

## Version-control boundary

Commit changes to `pyproject.toml`, `uv.lock`, and source files in this
repository. Do not commit local virtual environments, caches, parent-level
workspace experiments, or generated machine-local output.
