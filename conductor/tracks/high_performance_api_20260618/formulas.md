# Formula Evidence

Track 17 does not change legislative formulas.

The calculation endpoint reuses `BatchSimulator` and the existing OpenFisca
tax-benefit system. The API layer validates request shape and serialises
results; it does not duplicate formula logic.
