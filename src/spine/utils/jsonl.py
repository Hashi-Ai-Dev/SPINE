"""JSONL file utilities (Phase 1: creation only, no record appends yet)."""

from __future__ import annotations

from pathlib import Path


def ensure_jsonl(path: Path, *, force: bool = False) -> bool:
    """
    Create an empty JSONL file at `path` if it does not exist.
    Returns True if created, False if skipped.
    """
    if path.exists() and not force:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("", encoding="utf-8")
    return True
