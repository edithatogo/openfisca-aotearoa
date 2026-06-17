# API Contract

Generated: 2026-06-18

## Protocol

- Transport: HTTP.
- Application interface: ASGI.
- Server runtime: Granian.
- Request and response body format: JSON.
- Error response body format: JSON error envelope.

## `GET /health`

Purpose: cheap liveness check that does not instantiate the tax-benefit system.

Response `200`:

```json
{
  "status": "ok",
  "service": "openfisca-aotearoa-api"
}
```

## `GET /metadata`

Purpose: return package and model metadata.

Response `200`:

```json
{
  "country_package": "openfisca-aotearoa",
  "model": "AotearoaLegislationModel",
  "openfisca_core_version": "44.6.0",
  "api_version": "1"
}
```

## `POST /calculate`

Purpose: run OpenFisca calculations using the existing batch simulation helper.

Request:

```json
{
  "period": "2025-01-01",
  "variables": ["age"],
  "persons": [
    {
      "id": "person_a",
      "date_of_birth": {
        "ETERNITY": "1995-01-01"
      }
    }
  ]
}
```

Response `200`:

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

Validation errors return `422`. Calculation errors return `400`.

## `GET /parameters`

Purpose: inspect a bounded subset of parameter metadata without dumping the full
parameter tree by default.

Query parameters:

- `path`: optional dotted path under the parameter root.
- `limit`: maximum number of child names returned, default `50`, maximum `200`.

Response `200`:

```json
{
  "path": "root",
  "children": ["taxes", "benefits"],
  "truncated": false
}
```

Unknown parameter paths return `404`.

## Error Envelope

All non-2xx JSON errors use the same shape:

```json
{
  "error": {
    "code": "validation_error",
    "message": "Request body is invalid.",
    "details": []
  }
}
```

## Non-Goals

- No authentication or tenancy.
- No frontend routes.
- No full OpenAPI generator in this track.
- No production deployment automation.
