# Parameter Evidence

Track 17 does not change legislative parameter values.

The API exposes bounded parameter inspection through `GET /parameters`:

- `path` defaults to `root`.
- `limit` defaults to `50`.
- `limit` is capped at `200`.
- invalid `limit` values return a structured `422` validation error.
- unknown parameter paths return a structured `404` error.

The parameter endpoint resolves OpenFisca parameters through
`CountryTaxBenefitSystem().parameters` rather than duplicating parameter data.
