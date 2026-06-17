"""Command-line entry point for the high-performance API server."""

from __future__ import annotations

import sys
from os import environ

from granian.cli import cli

APP_TARGET = "openfisca_aotearoa.api.app:app"


def main() -> None:
    """Run the API with Granian using the ASGI interface.

    Granian reads server options from CLI flags and `GRANIAN_*` environment
    variables. Common non-interactive settings are `GRANIAN_HOST`,
    `GRANIAN_PORT`, and `GRANIAN_WORKERS`.
    """
    environ.setdefault("OPENBLAS_NUM_THREADS", "1")
    environ.setdefault("OMP_NUM_THREADS", "1")
    cli.main(
        args=["--interface", "asgi", *sys.argv[1:], APP_TARGET],
        prog_name="openfisca-aotearoa-api",
    )


if __name__ == "__main__":
    main()
