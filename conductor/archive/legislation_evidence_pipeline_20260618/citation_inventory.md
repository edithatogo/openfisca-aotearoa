# Citation Inventory

## Scope

Track 19 inventories citations in:

- `openfisca_aotearoa/variables/**/*.py`
- `openfisca_aotearoa/parameters/**/*.yaml`
- `openfisca_aotearoa/parameters/**/*.yml`
- roadmap and track documentation under `conductor/`

## Findings

- Variables and parameters already contain many direct `legislation.govt.nz`
  references through `reference = ...`, `reference: ...`, and nested
  `metadata.reference.href` fields.
- Parameter citations are concentrated in social security, income tax,
  citizenship, ACC, minimum wage, disability allowance, superannuation, health,
  and rates rebates parameter trees.
- Variable citations are concentrated under `openfisca_aotearoa/variables/acts`
  and include Act-level, schedule-level, part-level, and historical-version
  references.
- `conductor/product-guidelines.md` already requires new variables or
  parameters to link directly to legislative source material.
- `conductor/roadmap.md` names `nz-legislation`, `sourceright`,
  `nlp-policy-nz`, and `fyi-cli`, but before this track there was no local
  manifest contract or adapter boundary for those tools.

## Implementation Target

Track 19 implements the initial evidence contract in
`openfisca_aotearoa/evidence.py`. The extractor is intentionally offline and
line-oriented so default tests do not require network access, external tools,
or credentials.
