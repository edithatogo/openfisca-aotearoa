# Formula Evidence

Track 18 does not change legislative formulas.

The bounded runner reuses `BatchSimulator`, which in turn reuses the existing
OpenFisca tax-benefit system. Formula errors are wrapped as
`MicrosimulationError` so callers receive a clear bounded-runner failure rather
than a silent analytics result.
