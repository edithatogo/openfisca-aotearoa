"""Attach multiline git notes without shell-quoting note content."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


DEFAULT_REF = "commits"


def build_git_notes_command(
    note_file: Path,
    commit: str,
    *,
    notes_ref: str = DEFAULT_REF,
    force: bool = False,
    append: bool = False,
) -> list[str]:
    """Build a git-notes command that reads note content from a file."""
    action = "append" if append else "add"
    command = ["git", "notes", "--ref", notes_ref, action]
    if force and not append:
        command.append("-f")
    command.extend(["-F", str(note_file), commit])
    return command


def attach_git_note(
    note_file: Path,
    commit: str,
    *,
    notes_ref: str = DEFAULT_REF,
    force: bool = False,
    append: bool = False,
    allow_empty: bool = False,
) -> None:
    """Attach a note file to a commit using subprocess without a shell."""
    note_file = note_file.resolve()
    if not note_file.is_file():
        raise ValueError(f"Note file does not exist: {note_file}")
    if not allow_empty and note_file.read_text(encoding="utf-8").strip() == "":
        raise ValueError(f"Note file is empty: {note_file}")
    if force and append:
        raise ValueError("--force cannot be combined with --append")

    subprocess.run(
        build_git_notes_command(
            note_file,
            commit,
            notes_ref=notes_ref,
            force=force,
            append=append,
        ),
        check=True,
    )


def parse_args(argv: list[str]) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Attach a multiline git note from a UTF-8 text file without passing "
            "the note body through shell quoting."
        ),
    )
    parser.add_argument("note_file", type=Path)
    parser.add_argument("commit", nargs="?", default="HEAD")
    parser.add_argument(
        "--ref",
        default=DEFAULT_REF,
        help="Git notes ref name, default: commits.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing note. Cannot be combined with --append.",
    )
    parser.add_argument(
        "--append",
        action="store_true",
        help="Append to an existing note instead of adding a new one.",
    )
    parser.add_argument(
        "--allow-empty",
        action="store_true",
        help="Allow attaching an empty note file.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        attach_git_note(
            args.note_file,
            args.commit,
            notes_ref=args.ref,
            force=args.force,
            append=args.append,
            allow_empty=args.allow_empty,
        )
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"attach_git_note: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
