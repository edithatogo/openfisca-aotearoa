# OpenFisca Core v44+ Compatibility Assessment

Generated: 2026-06-18
Updated: 2026-06-19

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

### Implemented compatibility changes

1. **Enum formula outputs**

   OpenFisca Core 43 tightened enum validation and 44.7.0 enforces that behaviour.
   Local OpenFisca YAML execution now surfaces enum encoding failures for
   accommodation supplement situation formulas. Representative error:

   ```text
   EnumEncodingError: Failed to encode "[0 0 0 0 0]" of type 'int'
   ```

   Implemented change: `accommodation_supplement__situation` now returns
   integer enum indices consistently from `numpy.select`, avoiding an
   object-dtype array that mixes enum objects and integer fallback values.

2. **YAML test encoding on Windows**

   The OpenFisca YAML runner opens files with the platform default encoding.
   On Windows, that is `cp1252` in this environment, which cannot decode Maori
   macron names in family-scheme YAML tests.

   Implemented change: `scripts/run_openfisca_yaml_tests.py` resolves the
   installed OpenFisca YAML runner and runs it with `PYTHONUTF8=1` and
   `PYTHONIOENCODING=utf-8`.

3. **OpenFisca Web API smoke on Windows**

   The OpenFisca web API path imports Gunicorn, and Gunicorn imports Unix-only
   modules such as `grp`. This is not a country formula compatibility issue, but
   it means the API smoke test cannot be a mandatory Windows local gate.

   Implemented change: keep the smoke active on Linux CI and skip it on Windows,
   as implemented in `openfisca_aotearoa/tests/test_api.py`.

4. **OpenFisca YAML runner target**

   Running `openfisca test openfisca_aotearoa/tests -c openfisca_aotearoa`
   collects both YAML and Python tests in this checkout. On Windows, this mixes
   YAML compatibility failures with the web API platform limitation.

   Implemented change: the project-owned YAML runner targets explicit YAML
   files or directories and is wired into the focused compatibility CI gate.

## Verification

Focused compatibility tests now pass:

```text
uv run python scripts/run_openfisca_yaml_tests.py openfisca_aotearoa/tests/social_security/accommodation_supplement/2018/situation.yaml openfisca_aotearoa/tests/income_tax/family_scheme/family_tax_credit.yaml
```

Result on 2026-06-19:

```text
9 passed in 1.49s
```

The `family_tax_credit__eldest` invalid option failure was resolved by the
current branch's use of `populations.ADD` for the group-to-person aggregation
call. The focused `family_tax_credit.yaml` fixture passes under the UTF-8-safe
runner.

## Deferrals

- No dependency upgrade beyond `openfisca-core==44.7.0` is required for v44+
  compatibility because the project is already resolved on the v44 line.
- Strict Basedpyright expansion into `openfisca_aotearoa/variables` remains a
  separate typed-formula migration. Track 15 enforces Basedpyright for the
  non-variable package and keeps the variable tree as an explicit scoped
  exclusion.
- Full legacy OpenFisca YAML suite remediation remains out of scope for Track
  15. The focused v44 compatibility fixtures pass; broader accommodation
  supplement fixture mismatches should be handled in a formula/test-data
  remediation track.
