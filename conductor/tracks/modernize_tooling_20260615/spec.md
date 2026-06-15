# Specification: Modernize Tooling & Type Safety

## Purpose
Modernize Python tooling by migrating configuration to UV workspaces/Una monorepo manager, consolidating formatting/linting under Ruff, and setting up strict type checking using basedpyright.

## Requirements
- Link the package to the root workspace using UV workspaces.
- Set up Hatch/Hatch-VCS for packaging.
- Enable strict Ruff checks and automatic code formatting.
- Enforce strict type checking in Basedpyright.
- Enforce cognitive complexity checks (max complexity 15) via Complexipy.
