"""Tests for the git note attachment helper."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest


SCRIPT_PATH = Path(__file__).parents[2] / "scripts" / "attach_git_note.py"
SPEC = importlib.util.spec_from_file_location("attach_git_note", SCRIPT_PATH)
assert SPEC is not None
attach_git_note = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(attach_git_note)


def test_build_command_reads_note_body_from_file() -> None:
    command = attach_git_note.build_git_notes_command(
        Path("notes/track-21.txt"),
        "abc1234",
    )

    assert command == [
        "git",
        "notes",
        "--ref",
        "commits",
        "add",
        "-F",
        str(Path("notes/track-21.txt")),
        "abc1234",
    ]


def test_force_replaces_existing_note_without_shell_content() -> None:
    command = attach_git_note.build_git_notes_command(
        Path("track-20-note.md"),
        "HEAD",
        force=True,
    )

    assert command == [
        "git",
        "notes",
        "--ref",
        "commits",
        "add",
        "-f",
        "-F",
        "track-20-note.md",
        "HEAD",
    ]


def test_attach_git_note_rejects_empty_note(tmp_path: Path) -> None:
    note_file = tmp_path / "empty.md"
    note_file.write_text("\n", encoding="utf-8")

    with pytest.raises(ValueError, match="empty"):
        attach_git_note.attach_git_note(note_file, "HEAD")


def test_attach_git_note_invokes_git_without_shell(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    note_file = tmp_path / "note.md"
    note_file.write_text("Track summary\n\n- Tests passed\n", encoding="utf-8")
    calls: list[dict[str, object]] = []

    def fake_run(command: list[str], *, check: bool) -> None:
        calls.append({"command": command, "check": check})

    monkeypatch.setattr(attach_git_note.subprocess, "run", fake_run)

    attach_git_note.attach_git_note(note_file, "abc1234", append=True)

    assert calls == [
        {
            "command": [
                "git",
                "notes",
                "--ref",
                "commits",
                "append",
                "-F",
                str(note_file.resolve()),
                "abc1234",
            ],
            "check": True,
        },
    ]


def test_attach_git_note_rejects_force_with_append(tmp_path: Path) -> None:
    note_file = tmp_path / "note.md"
    note_file.write_text("content", encoding="utf-8")

    with pytest.raises(ValueError, match="cannot be combined"):
        attach_git_note.attach_git_note(note_file, "HEAD", force=True, append=True)
