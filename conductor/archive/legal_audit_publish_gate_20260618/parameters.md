# Parameter Evidence

Track 21 does not change OpenFisca parameter values.

The readiness model treats parameter evidence as a required publish-readiness
class for legislation tracks. Missing parameter evidence is surfaced in the
machine-readable manifest and Markdown report.

Relevant contract:

- `ReadinessManifest.required_evidence` includes `parameters`.
- `ReadinessManifest.missing_evidence` lists `parameters` when a track lacks a
  parameter evidence artifact.
