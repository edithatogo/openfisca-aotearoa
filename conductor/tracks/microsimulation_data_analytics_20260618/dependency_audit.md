# Optional Dependency Audit

Generated: 2026-06-18

## Local Import Probe

Command:

```sh
uv run python -c "import importlib.util,json; names=['open_social_data','voiage','mars','innovate']; print(json.dumps({n: importlib.util.find_spec(n) is not None for n in names}, indent=2))"
```

Result:

```json
{
  "open_social_data": false,
  "voiage": false,
  "mars": false,
  "innovate": false
}
```

## Lockfile Probe

`pyproject.toml` and `uv.lock` do not contain direct dependencies for
`open_social_data`, `voiage`, `mars`, or `innovate`. The only `mars` substring
match is the unrelated `marshmallow` package.

## Sibling Repository Probe

A sibling `open_social_data` checkout exists at:

```text
C:/Users/60217257/OneDrive - Flinders/repos/legal-nz/open_social_data
```

Its current status is dirty:

```text
M conductor/tracks/short_term_completion_20260618/validation.md
M docs/technical/release_readiness_checklist.md
```

Track 18 should not couple this package to that working tree. Any
`open_social_data` import should remain optional and should support fixture
cohorts when the package is absent.

## Integration Decision

- `open_social_data`: optional source adapter boundary only.
- `voiage`: optional value-of-information adapter boundary only.
- `mars`: optional spline-regression adapter boundary only.
- `innovate`: optional policy-diffusion adapter boundary only.

The package should expose dependency status and raise clear, actionable errors
when optional analytics packages are unavailable.
