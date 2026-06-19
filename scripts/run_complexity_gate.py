"""Run Complexipy with UTF-8-safe output on Windows."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path


def _runner_path() -> str:
    executable_name = "complexipy.exe" if os.name == "nt" else "complexipy"
    adjacent_runner = Path(sys.executable).with_name(executable_name)
    if adjacent_runner.exists():
        return str(adjacent_runner)

    discovered_runner = shutil.which(executable_name)
    if discovered_runner is not None:
        return discovered_runner

    raise SystemExit(
        f"Unable to find {executable_name!r}. Run through `uv run python` "
        "or install the project with its development dependencies first."
    )


def main() -> int:
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    env["PYTHONIOENCODING"] = "utf-8"
    command = [
        _runner_path(),
        "openfisca_aotearoa",
        "--max-complexity-allowed",
        "15",
    ]
    return subprocess.run(command, env=env, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
