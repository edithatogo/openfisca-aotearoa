# Specification: High-Performance Web API Serving

## Purpose

Implement the roadmap's API-serving goal by exposing OpenFisca Aotearoa through
a small, validated, high-performance web service using a Rust-backed runtime
such as Granian or Robyn.

## Requirements

- Select Granian or Robyn based on compatibility, maintenance, Windows support,
  and packaging impact.
- Define a minimal API surface for calculation, health, metadata, and parameter
  inspection endpoints.
- Use Pydantic v2 request and response models for validation.
- Reuse OpenFisca simulation APIs rather than duplicating calculation logic.
- Add unit and smoke tests for request validation, successful calculation, and
  error responses.
- Add local run commands and CI-safe smoke checks.
- Document deployment and non-goal boundaries.

## Non-Goals

- Building a frontend client in this repository.
- Deploying to production infrastructure.
- Adding authentication or tenant management.
