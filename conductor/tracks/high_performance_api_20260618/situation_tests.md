# Situation-Test Evidence

Focused API validation rerun on 2026-06-19:

```text
uv run pytest openfisca_aotearoa/tests/test_api_app.py openfisca_aotearoa/tests/test_api_models.py --strict-markers --strict-config -W error
```

Result:

```text
16 passed
```

Packaged server smoke rerun on 2026-06-19:

```text
uv run python scripts/smoke_api_server.py
```

Result: passed.

The smoke starts Granian on an ephemeral localhost port, verifies `/health`,
posts a representative `/calculate` request, and terminates the server.
