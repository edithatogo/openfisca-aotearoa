# High-Performance API

OpenFisca Aotearoa includes a lightweight ASGI API for CI, local service
checks, and high-throughput calculation workers. It is served by Granian and
uses Pydantic v2 models for request and response validation.

## Run Locally

Start the API with the packaged command:

```sh
uv run openfisca-aotearoa-api
```

The command serves `openfisca_aotearoa.api.app:app` with the ASGI interface.
Granian command-line options can be passed through:

```sh
uv run openfisca-aotearoa-api --host 127.0.0.1 --port 8000 --workers 1
```

Granian also reads non-interactive runtime configuration from `GRANIAN_*`
environment variables. Common settings are:

```sh
GRANIAN_HOST=0.0.0.0
GRANIAN_PORT=8000
GRANIAN_WORKERS=2
```

The package sets conservative `OPENBLAS_NUM_THREADS` and `OMP_NUM_THREADS`
defaults of `1` unless the caller provides explicit values. This keeps local
and CI server startup deterministic on machines with tight thread limits.

## Health

```sh
curl "http://127.0.0.1:8000/health"
```

Response:

```json
{
  "status": "ok",
  "service": "openfisca-aotearoa-api"
}
```

## Metadata

```sh
curl "http://127.0.0.1:8000/metadata"
```

Response:

```json
{
  "country_package": "openfisca-aotearoa",
  "model": "AotearoaLegislationModel",
  "openfisca_core_version": "44.6.0",
  "api_version": "1"
}
```

## Calculation

The calculation endpoint accepts a period, one or more output variables, and a
list of persons. Each person must have a unique `id`; additional fields are
passed through as OpenFisca input variables.

```sh
curl -X POST "http://127.0.0.1:8000/calculate" \
  -H "content-type: application/json" \
  -d '{
    "period": "2025-01-01",
    "variables": ["age"],
    "persons": [
      {
        "id": "person_a",
        "date_of_birth": {"ETERNITY": "1995-01-01"}
      }
    ]
  }'
```

Response:

```json
{
  "period": "2025-01-01",
  "results": [
    {
      "id": "person_a",
      "age": 30
    }
  ]
}
```

Validation errors return `422`. Calculation errors, such as requesting an
unknown variable, return `400`.

## Parameters

The parameters endpoint returns bounded child names for a parameter node. It
does not dump the full parameter tree by default.

```sh
curl "http://127.0.0.1:8000/parameters"
curl "http://127.0.0.1:8000/parameters?path=taxes&limit=25"
```

Response:

```json
{
  "path": "taxes",
  "children": ["income_tax"],
  "truncated": false
}
```

`path` defaults to `root`. `limit` defaults to `50` and is capped at `200`.
Unknown paths return `404`.

## Error Shape

All JSON error responses use the same envelope:

```json
{
  "error": {
    "code": "validation_error",
    "message": "Request body is invalid.",
    "details": []
  }
}
```

## Smoke Check

CI runs a packaged server smoke test:

```sh
uv run python scripts/smoke_api_server.py
```

The smoke test starts Granian on an ephemeral localhost port, verifies
`/health`, posts a representative `/calculate` request, and terminates the
server.

## Deployment Notes

- Run behind a reverse proxy or platform ingress that provides TLS.
- Configure host, port, worker count, and logging with Granian options or
  `GRANIAN_*` environment variables.
- Keep worker counts conservative until representative calculation workloads
  have been profiled.
- Use `/health` for liveness checks. It does not instantiate the tax-benefit
  system.

## Non-Goals

- Authentication, tenancy, rate limiting, and authorization.
- Browser-facing frontend routes.
- Full OpenAPI generation.
- Production deployment automation.
- Parity with the legacy `openfisca serve` API surface.
