"""Validate Conductor track legal audit and publish readiness."""

from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path

from openfisca_aotearoa.readiness import (
    ReadinessGateError,
    build_readiness_manifest,
    render_readiness_report,
    require_publish_ready,
)


def main() -> int:
    """Run the publish-readiness gate for one or more tracks."""
    parser = argparse.ArgumentParser(
        description="Check legal audit and publish-readiness evidence.",
    )
    parser.add_argument("tracks", nargs="+")
    parser.add_argument("--report", default=None)
    parser.add_argument("--allow-not-ready", action="store_true")
    args = parser.parse_args()

    git_notes = _git_notes()
    registry_statuses = _registry_statuses(Path("conductor/tracks.md"))
    manifests = [
        build_readiness_manifest(
            track,
            git_notes=git_notes,
            registry_status=registry_statuses.get(Path(track).name),
        )
        for track in args.tracks
    ]
    report = render_readiness_report(manifests)
    if args.report:
        Path(args.report).write_text(report, encoding="utf-8")
    else:
        print(report)

    if args.allow_not_ready:
        return 0
    try:
        require_publish_ready(manifests)
    except ReadinessGateError as error:
        print(str(error))
        return 1
    return 0


def _git_notes() -> dict[str, str]:
    try:
        result = subprocess.run(
            ["git", "notes", "list"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return {}
    notes: dict[str, str] = {}
    for line in result.stdout.splitlines():
        parts = line.split()
        if len(parts) == 2:
            note_hash, commit_hash = parts
            notes[commit_hash[:7]] = note_hash
            notes[commit_hash[:8]] = note_hash
    return notes


def _registry_statuses(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    statuses: dict[str, str] = {}
    current_status: str | None = None
    heading = re.compile(r"^## \[([ x~])\] Track ")
    link = re.compile(r"\./conductor/tracks/([^/]+)/")
    for line in path.read_text(encoding="utf-8").splitlines():
        heading_match = heading.search(line)
        if heading_match:
            current_status = heading_match.group(1)
            continue
        link_match = link.search(line)
        if current_status is not None and link_match:
            statuses[link_match.group(1)] = current_status
            current_status = None
    return statuses


if __name__ == "__main__":
    raise SystemExit(main())
