# Tool Boundaries

The optional tool boundaries are implemented by
`openfisca_aotearoa.evidence.default_tool_boundaries()`.

## nz-legislation

- Purpose: retrieve New Zealand Act and regulation text.
- Default mode: optional live operation.
- Offline mode: fixture-backed document payloads through `FixtureEvidenceAdapter`.
- Credentials: not required by default.

## sourceright

- Purpose: validate and report citation metadata.
- Default mode: optional live operation.
- Machine-readable output: JSON report parsed by `SourcerightAdapter`.
- Credentials: not required by default.

## nlp-policy-nz

- Purpose: search Hansard and policy-intent corpora.
- Default mode: optional live operation.
- Offline mode: fixture-backed policy-search evidence can be loaded without
  network access.
- Credentials: not required by default.

## fyi-cli

- Purpose: look up OIA and disclosure evidence.
- Default mode: manual live operation only.
- Machine-readable output: expected when an operator exports a local report.
- Credentials: required for live or authenticated lookup.
- Boundary: the default pipeline must not send OIA requests or perform
  authenticated lookups automatically.
