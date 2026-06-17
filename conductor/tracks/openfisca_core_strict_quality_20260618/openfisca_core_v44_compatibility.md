# OpenFisca Core v44+ Compatibility Assessment

Generated: 2026-06-18

## Sources Checked

- OpenFisca Core changelog:
  <https://raw.githubusercontent.com/openfisca/openfisca-core/master/CHANGELOG.md>
- Local resolved dependency:
  `openfisca-core==44.7.0` from `uv.lock` and package metadata.

## Upstream Migration Surface

The upstream changelog records the v44 release line as technical rather than a
country-package API break:

- `44.0.0`: conditional NumPy dependency based on Python version.
- `44.0.1`: parallel execution support for the `openfisca test` command line.
- `44.0.2`: CI cache-name fix for conditional Python-version dependency.

No v44-specific country package migration instruction was found in the official
changelog. However, this repository is running on `44.7.0`, so it also inherits
the v43 enum validation changes that materially affect local YAML tests.

## Local API Usage Compared To v44+

### Compatible today

- `TaxBenefitSystem` subclassing in
  `openfisca_aotearoa/aotearoa_legislationmodel.py` still imports and
  instantiates under OpenFisca Core 44.7.0.
- Entity declarations with `openfisca_core.entities.build_entity` still load.
- `SimulationBuilder().build_from_entities(...)` is still available and covered
  by the local Python simulation tests.
- `holders.set_input_dispatch_by_period` and `holders.set_input_divide_by_period`
  remain available.
- Period constants and `periods.DateUnit` imports remain available.
- `populations.ADD` remains available for group-to-person aggregation.

### Requires code or test-data changes

1. **Enum formula outputs**

   OpenFisca Core 43 tightened enum validation and 44.7.0 enforces that behaviour.
   Local OpenFisca YAML execution now surfaces enum encoding failures for
   accommodation supplement situation formulas. Representative error:

   ```text
   EnumEncodingError: Failed to encode "[0 0 0 0 0]" of type 'int'
   ```

   Required change: formula paths returning enum values should return typed enum
   members, string enum names, or integer arrays with an integer dtype that
   OpenFisca Core can encode. Object-dtype arrays containing integers are not a
   stable v44+ output contract.

2. **YAML test encoding on Windows**

   The OpenFisca YAML runner opens files with the platform default encoding.
   On Windows, that is `cp1252` in this environment, which cannot decode Maori
   macron names in family-scheme YAML tests.

   Required change: provide a project-owned UTF-8 YAML test entry point for
   Windows, or configure the environment for `PYTHONUTF8=1` wherever YAML tests
   are run locally.

3. **OpenFisca Web API smoke on Windows**

   The OpenFisca web API path imports Gunicorn, and Gunicorn imports Unix-only
   modules such as `grp`. This is not a country formula compatibility issue, but
   it means the API smoke test cannot be a mandatory Windows local gate.

   Required change: keep the smoke active on Linux CI and skip it on Windows,
   which is now implemented in `openfisca_aotearoa/tests/test_api.py`.

4. **OpenFisca YAML runner target**

   Running `openfisca test openfisca_aotearoa/tests -c openfisca_aotearoa`
   collects both YAML and Python tests in this checkout. On Windows, this mixes
   YAML compatibility failures with the web API platform limitation.

   Required change: add a YAML-only runner command or script that targets YAML
   files explicitly and avoids Python smoke-test collection.

## Required Code Changes

The next compatibility implementation should be ordered as follows:

1. Fix accommodation supplement enum formula outputs so they return
   OpenFisca-encodable enum values under 44.7.0.
2. Investigate and fix the `family_tax_credit__eldest` invalid option `a`
   failure surfaced by the UTF-8 OpenFisca YAML run.
3. Add a UTF-8-safe YAML test command for Windows and document it beside the
   existing pytest command.
4. Add focused regression tests for enum formula output dtype and family tax
   credit option handling before changing the broader YAML suite.

## Deferrals

- No dependency upgrade beyond `openfisca-core==44.7.0` is required for v44+
  compatibility because the project is already resolved on the v44 line.
- Strict Basedpyright expansion into `openfisca_aotearoa/variables` should remain
  a separate Phase 3 task. It is related to quality gates, not a blocker for the
  v44 runtime compatibility fixes above.
