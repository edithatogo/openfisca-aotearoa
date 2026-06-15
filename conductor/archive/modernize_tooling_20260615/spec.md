# Specification: Modernize Project Tooling

## Purpose
This track modernizes the OpenFisca Aotearoa repository's toolchain to use bleeding-edge Rust-based tools, enhancing developer productivity, linting speed, type safety, and package reproducibility.

## Requirements
1. **Dependency & Environment Management (`uv`/Hatch):**
   - Modernize project metadata in `pyproject.toml` for UV-compatible
     environments.
   - Configure development and testing dependencies.
   - Declare dependencies including `openfisca-core`, `pandas`, `polars`, `pydantic`, `loguru`, `orjson`.
2. **Linting & Formatting (`ruff`):**
   - Configure Ruff in `pyproject.toml` (or `pixi.toml` / `ruff.toml`).
   - Remove/replace references to `autopep8`, `flake8`, `isort`, `pylint`, and `pyupgrade`.
3. **Static Type Checking (`basedpyright`):**
   - Configure `basedpyright` configuration file or settings.
   - Establish a passable baseline that can be tightened as legacy modules are
     annotated.
4. **Validation Tests:**
   - Verify project metadata parses, Ruff passes, Basedpyright passes, and tests
     execute correctly from the configured Python environment.
