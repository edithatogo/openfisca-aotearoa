"""Run OpenFisca YAML tests with UTF-8-safe defaults.

The OpenFisca CLI reads YAML fixtures using Python's default text encoding.
On Windows that can be cp1252 unless the process opts into UTF-8, which makes
fixtures containing macrons fail before the model code is exercised.
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


DEFAULT_TEST_PATHS = ("openfisca_aotearoa/tests",)


def _runner_path() -> str:
    executable_name = (
        "openfisca-run-test.exe" if os.name == "nt" else "openfisca-run-test"
    )
    adjacent_runner = Path(sys.executable).with_name(executable_name)
    if adjacent_runner.exists():
        return str(adjacent_runner)

    discovered_runner = shutil.which(executable_name)
    if discovered_runner is not None:
        return discovered_runner

    raise SystemExit(
        f"Unable to find {executable_name!r}. Run through `uv run python` "
        "or install the project with its OpenFisca dependency first."
    )


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run OpenFisca YAML tests with UTF-8 process encoding.",
    )
    parser.add_argument(
        "paths",
        nargs="*",
        default=DEFAULT_TEST_PATHS,
        help=(
            "YAML files or directories to run. Defaults to the full "
            "openfisca_aotearoa/tests tree."
        ),
    )
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    env["PYTHONIOENCODING"] = "utf-8"

    command = [_runner_path(), *args.paths]
    print("Running:", " ".join(command))
    return subprocess.run(command, env=env, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
