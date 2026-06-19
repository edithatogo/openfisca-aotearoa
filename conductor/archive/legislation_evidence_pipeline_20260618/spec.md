# Specification: Legislation Evidence Pipeline Integrations

## Purpose

Implement the roadmap's legislation-to-code evidence workflow by integrating
legislation retrieval, citation validation, Hansard/policy search, and OIA
evidence checks into a reproducible local pipeline.

## Requirements

- Use `nz-legislation` or existing local legislation corpus outputs as the
  source for Act and regulation text.
- Integrate `sourceright` to validate and report citations used by variables,
  parameters, and documentation.
- Define an `nlp-policy-nz` boundary for Hansard and policy-intent search.
- Define an `fyi-cli` boundary for OIA/disclosure evidence lookup.
- Produce machine-readable evidence manifests and human-readable reports.
- Add offline tests for manifest generation and graceful handling of missing
  external tools or credentials.
- Keep live OIA or authenticated lookup steps explicitly manual or optional.

## Non-Goals

- Sending OIA requests automatically.
- Requiring network access for the default test suite.
- Treating generated LLM mappings as legal advice.
