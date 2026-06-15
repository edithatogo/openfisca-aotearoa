# Specification: Target Legislation Audit & Track Scaffolding

## Purpose

Execute a comprehensive audit of current New Zealand social security, health primary care funding, and tax legislation using the `nz-legislation` CLI tool, identifying missing rules and scaffolding separate Conductor tracks to implement each Act.

## Requirements

- Identify core Acts including Social Security Act 2018, Income Tax Act 2007, primary care funding legislation, housing, tax administration, and ACC levy instruments.
- Use `nz-legislation` CLI tool to fetch and check for updates and text changes when the command is available in the local environment.
- Identify missing rules and gaps in `openfisca-aotearoa`.
- Generate distinct, granular Conductor tracks under `conductor/tracks/` for each piece of legislation to explore and codify.
