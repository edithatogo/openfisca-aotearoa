# Runtime Selection: Granian

Generated: 2026-06-18

## Decision

Use Granian to serve a small ASGI application.

## Requirements Matrix

| Requirement | Granian | Robyn | Decision |
| --- | --- | --- | --- |
| Rust-backed runtime | Rust HTTP server built on Hyper and Tokio. | Rust-backed web framework/runtime. | Both satisfy. |
| Windows support | PyPI classifiers include Microsoft Windows and Python 3.11-3.14. | PyPI classifiers are OS Independent and Python 3.10-3.14. | Both plausible; Granian is explicit. |
| Packaging impact | One server dependency, while the app can stay standard ASGI. | Adds a framework-specific routing/request model. | Granian has lower app coupling. |
| CI behaviour | ASGI app can be tested in-process without starting Granian. | Framework handlers need Robyn app/runtime semantics. | Granian is easier to smoke test safely. |
| API surface fit | Serves `/health`, `/metadata`, `/calculate`, and `/parameters` via standard HTTP. | Can implement the endpoints directly, but owns framework patterns. | Granian preserves portability. |

## Rationale

Granian is a Rust HTTP server for Python applications and supports ASGI, RSGI,
and WSGI interfaces. Its PyPI metadata lists production/stable status,
Microsoft Windows support, and Python 3.11+ compatibility. Granian's ASGI mode
allows this repository to keep the application logic framework-neutral and test
the app without a network listener.

Robyn is also Rust-backed, but it is a Python web framework with its own request
and response APIs. That would be a larger surface-area choice for this track and
would make future migration to standard ASGI tooling less direct.

## Packaging Boundary

Add Granian as a runtime dependency only for serving. Keep request validation,
response rendering, and tests in package-owned modules so CI can exercise the
API without starting a long-running server process.

## Sources

- Granian PyPI: <https://pypi.org/project/granian/>
- Granian project repository: <https://github.com/emmett-framework/granian>
- Robyn PyPI: <https://pypi.org/project/robyn/>
- Robyn API documentation: <https://robyn.tech/documentation/en/api_reference/getting_started>
