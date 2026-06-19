# Situation-Test Evidence

Workspace smoke validation was rerun on 2026-06-19:

```text
uv run --extra dev python scripts/smoke_workspace.py
```

Result:

```text
uv lock --check: passed
uv run --extra dev una --help: passed
local package import and una version check: passed
uv --directory openfisca-aotearoa run ... from parent root: passed
uv --directory openfisca-aotearoa run --extra dev una --help from parent root: passed
```

Additional focused commands rerun on 2026-06-19:

```text
uv lock --check
uv run --extra dev una --help
```

Both passed.
