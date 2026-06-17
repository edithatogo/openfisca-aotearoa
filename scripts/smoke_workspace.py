"""Smoke-test uv and una workspace integration.

The checks intentionally cover both supported execution boundaries:

* this repository as a standalone package; and
* this repository invoked from its parent directory with ``uv --directory``.
"""

from __future__ import annotations

import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
PARENT_ROOT = REPO_ROOT.parent


def run(command: list[str], cwd: Path) -> None:
    print(f"+ ({cwd}) {' '.join(command)}", flush=True)
    subprocess.run(command, cwd=cwd, check=True)


def main() -> int:
    package_name = REPO_ROOT.name

    run(["uv", "lock", "--check"], REPO_ROOT)
    run(["uv", "run", "--extra", "dev", "una", "--help"], REPO_ROOT)
    run(
        [
            "uv",
            "run",
            "--extra",
            "dev",
            "python",
            "-c",
            (
                "import importlib.metadata as m; "
                "import openfisca_aotearoa; "
                "print(m.version('una')); "
                "print(openfisca_aotearoa.CountryTaxBenefitSystem.__name__)"
            ),
        ],
        REPO_ROOT,
    )
    run(
        [
            "uv",
            "--directory",
            package_name,
            "run",
            "--extra",
            "dev",
            "python",
            "-c",
            (
                "from pathlib import Path; "
                f"expected = r'{REPO_ROOT}'; "
                "actual = str(Path.cwd()); "
                "print(actual); "
                "raise SystemExit(0 if actual == expected else 1)"
            ),
        ],
        PARENT_ROOT,
    )
    run(
        [
            "uv",
            "--directory",
            package_name,
            "run",
            "--extra",
            "dev",
            "una",
            "--help",
        ],
        PARENT_ROOT,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
