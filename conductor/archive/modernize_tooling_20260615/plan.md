# Plan: Modernize Project Tooling

## Phase 1: Environment and Dependency Migration to UV Workspaces & Hatch

- [x] Task: Initialize UV Workspace (`pyproject.toml`) in the root monorepo directory
- [x] Task: Configure Python >=3.11 target and dynamic versioning using Hatch/VCS
- [x] Task: Migrate core and development dependencies to `openfisca-aotearoa/pyproject.toml`
- [x] Task: Conductor - User Manual Verification 'Environment and Dependency Migration to UV Workspaces' [checkpoint: work_done]

## Phase 2: Linting and Formatting Migration to Ruff

- [x] Task: Configure Ruff settings inside `pyproject.toml`
- [x] Task: Deprecate old configurations (`.flake8`)
- [x] Task: Conductor - User Manual Verification 'Linting and Formatting Migration to Ruff' [checkpoint: work_done]

## Phase 3: Typing, Cognitive Complexity & Static Analysis

- [x] Task: Configure baseline `basedpyright` and `Complexipy` in `pyproject.toml`
- [x] Task: Conductor - User Manual Verification 'Typing and Static Analysis' [checkpoint: work_done]
