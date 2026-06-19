# Parameter Evidence

Track 18 does not change OpenFisca parameter values.

The cohort contract passes parameter and variable inputs through to the existing
OpenFisca simulation layer. The bounded runner validates cohort shape, record
count, family references, requested variables, and periods before or during
OpenFisca execution.

Relevant configuration boundary:

- default `BoundedBatchRunner.max_records`: `10000`.
- runner rejects cohorts above the configured bound before OpenFisca execution.
