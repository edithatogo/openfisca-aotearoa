# OpenFisca Core and Quality Gate Inventory

Generated: 2026-06-18

## Scope

This inventory covers the first Track 15 implementation task: current
dependency pins, resolved OpenFisca Core version, and direct OpenFisca API usage
across variables, parameters, tests, and docs. It is based on live repository
state, not prior roadmap assumptions.

## Dependency State

- `pyproject.toml` declares `openfisca-core[web-api] >=44.6.0`.
- `uv.lock` resolves `openfisca-core` to `44.7.0`.
- Runtime package metadata also reports `44.7.0` via
  `importlib.metadata.version("openfisca-core")`.
- The import package does not expose `openfisca_core.__version__`; version
  checks should use package metadata rather than module attributes.

## Direct OpenFisca API Usage

The codebase uses OpenFisca Core APIs in three broad layers.

### Tax-benefit system and entities

- `openfisca_aotearoa/aotearoa_legislationmodel.py` subclasses
  `openfisca_core.taxbenefitsystems.TaxBenefitSystem`.
- `openfisca_aotearoa/entities.py` builds core entities with
  `openfisca_core.entities.build_entity`.
- `openfisca_aotearoa/__init__.py` exposes `CountryTaxBenefitSystem` as the
  OpenFisca extension entry point.

### Simulation helper

- `openfisca_aotearoa/simulation.py` imports
  `openfisca_core.simulation_builder.SimulationBuilder`.
- The batch helper calls `SimulationBuilder().build_from_entities(...)` and
  then calculates requested variables by period.

### Variables

- The variables tree currently contains 101 Python files.
- Direct OpenFisca variable APIs include `openfisca_core.variables.Variable`,
  `openfisca_core.periods` constants, `periods.DateUnit`, `openfisca_core.holders`
  input helpers, and `openfisca_core.populations` aggregation options.
- A direct scan found 523 relevant `definition_period`, period, input helper,
  aggregation, tax-benefit-system, and simulation-builder references under
  `openfisca_aotearoa/variables` and adjacent package files.
- Both import styles are in use:
  `from openfisca_core.periods import MONTH` and
  `from openfisca_core import periods, variables`.
- Input helpers currently include both `set_input_dispatch_by_period` and
  `set_input_divide_by_period`.
- Aggregation code uses `populations.ADD` for family-to-person computation.

## Parameter Surface

- The parameters tree currently contains 79 files.
- Parameter files are split across `.yaml`, `.yml`, and `.csv` inputs.
- Current high-risk parameter areas for OpenFisca Core compatibility are:
  family scheme YAML, Social Security Schedule 5 YAML, and accommodation
  supplement CSV-backed area parameters.
- Track 14 review found a Windows YAML decoding issue in family scheme tests;
  this should remain in scope for the strict YAML test baseline rather than
  being treated as a solved compatibility item.

## Test and Documentation Surface

- There is no top-level `tests/` directory in the current checkout.
- Python tests live under `openfisca_aotearoa/tests`.
- README currently documents `uv run pytest` as the main local test command.
- `.github/workflows/ci.yml` already defines CI entry points for:
  `uv run basedpyright openfisca_aotearoa`,
  `uv run complexipy openfisca_aotearoa --max-complexity 15`, and
  `uv run pytest --cov=openfisca_aotearoa --cov-report=xml --strict-markers
  --strict-config -W error`.
- `.github/workflows/ci.yml` also runs Ruff through `astral-sh/ruff-action@v1`.

## Quality Gate Configuration Snapshot

- Ruff is installed through the `dev` extra and currently configured for the
  Pyflakes rule family only: `select = ["F"]`.
- Basedpyright is installed through the `dev` extra but currently configured as
  `typeCheckingMode = "basic"`.
- Basedpyright excludes `openfisca_aotearoa/variables`, which means the main
  OpenFisca formula surface is not yet under static type checking.
- Complexipy is installed through the `dev` extra with `max-complexity = 15`.
- Pytest is configured with strict markers, strict config, coverage reporting,
  and warnings-as-errors, with one explicit
  `pytest.PytestUnraisableExceptionWarning` ignore.

## Compatibility Risks Identified

- The project metadata is already on a v44+ dependency path, but the codebase
  still needs an API compatibility comparison against OpenFisca Core v44+
  migration notes before the upgrade can be declared complete.
- OpenFisca Core version checks should not rely on
  `openfisca_core.__version__`.
- The mixed period import styles are valid today but make broad migration edits
  harder to review; future compatibility changes should normalise by module
  area rather than by repository-wide replacement.
- The variables tree is excluded from Basedpyright, so strict type safety is
  currently aspirational for the largest runtime surface.
- The absence of a top-level `tests/` directory means broad commands or docs
  that assume `tests` will fail on Windows.
- Windows text encoding behaviour remains a known YAML test risk and should be
  captured in the next baseline-failure task.

## Commands Used

```text
uv --no-cache run python -c "import importlib.metadata as m; print(m.version('openfisca-core'))"
rg -n '^version =' uv.lock
rg --files openfisca_aotearoa/parameters
rg --files openfisca_aotearoa/variables
rg -n 'set_input_|populations\.|periods\.DateUnit|periods\.(DAY|WEEK|MONTH|YEAR|ETERNITY)|definition_period = ' openfisca_aotearoa/variables
rg -n 'openfisca test|openfisca-core|basedpyright|ruff|complexipy|pytest|coverage|test:' .github pyproject.toml README.md Makefile* conductor
```

## Next Track 15 Work

1. Run the full quality gate baseline and capture concrete failures for Ruff,
   Basedpyright, Complexipy, coverage, and OpenFisca YAML tests.
2. Compare the direct OpenFisca Core API usage above against v44+ migration
   requirements from primary OpenFisca sources.
3. Fix the Windows YAML decoding issue or document it as an explicit blocker
   with a minimal reproducer.
4. Tighten Basedpyright incrementally, starting with package entry points and
   helper modules before bringing variable modules into scope.
