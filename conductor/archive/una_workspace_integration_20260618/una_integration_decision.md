# Una Integration Decision

Generated: 2026-06-18

## Sources Checked

- Una documentation: <https://una.rdrn.me/>
- Una quickstart: <https://una.rdrn.me/quickstart/>
- Una installation notes: <https://una.rdrn.me/install/>
- Una build notes: <https://una.rdrn.me/build/>
- uv workspace documentation:
  <https://docs.astral.sh/uv/concepts/projects/workspaces/>

## Decision

Do not make this nested repository the parent `legal-nz` uv workspace root.

Do add minimal, standalone-safe workspace metadata and documentation inside this
repository so it can:

1. Continue to behave as an independent package with its own `uv.lock`.
2. Be invoked from the parent workspace with explicit `uv --directory
   openfisca-aotearoa ...` commands.
3. Be ready for a later parent-owned `legal-nz` uv workspace or Una rollout
   without forcing parent files to change from this nested repository.

## Rationale

The uv documentation says a workspace root is declared with
`[tool.uv.workspace]`, that workspace members share one lockfile, and that
`uv run` / `uv sync` operate on the workspace root by default. The parent
`legal-nz` repository does not currently have a root `pyproject.toml` or
`uv.lock`, and it contains multiple submodules with their own package-management
states. Creating a parent workspace from inside this nested repository would
cross repository ownership boundaries.

Una's documentation says it is intended for Python monorepos that already have a
functional uv workspace. It also says the CLI is added with `uv add --dev una`,
while `hatch-una` is a build-time plugin for monorepo wheel builds. This package
is currently a single standalone Hatchling package with no local workspace
member dependencies. Adding `hatch-una` to the build backend now would add build
complexity without a local dependency graph for Una to resolve.

## Minimum Safe Surface

Track 16 should implement the following nested-repo changes:

- Add a self-workspace declaration:

  ```toml
  [tool.uv.workspace]
  members = ["."]
  ```

  This makes the repository's `uv` workspace boundary explicit without adding
  parent members or changing standalone install behaviour.

- Add `una` to the `dev` extra only, not to runtime dependencies.

- Do not add `hatch-una` to `[build-system]` until this package has local
  workspace-member dependencies or the parent repository owns a monorepo build
  decision.

- Add developer docs for:
  - Standalone commands from this repository.
  - Parent-invoked commands using `uv --directory openfisca-aotearoa`.
  - Explicit parent follow-up items.

- Add smoke validation that checks:
  - `uv lock --check`.
  - `uv run --extra dev una --help`.
  - A parent-style `uv --directory openfisca-aotearoa ...` path-resolution
    command from the parent repository root.

`una==0.7.0` package graph commands (`una tree` and `una sync`) are not enabled
for the current flat package layout because they expect workspace members to be
package directories. This track installs and configures the CLI for future local
member integration while keeping uv responsible for the current self-workspace
workflow.

## Deferred Parent-Owned Decisions

The parent `legal-nz` repository should separately decide whether to:

- Add a parent `pyproject.toml` and parent `uv.lock`.
- Register submodules as uv workspace members.
- Add `una` as a parent development tool.
- Use `hatch-una` for cross-submodule wheel builds.

Those decisions affect multiple repositories and should be committed at the
parent root, not inside `openfisca-aotearoa`.
