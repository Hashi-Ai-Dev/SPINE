"""Safe file I/O helpers for SPINE init."""

from __future__ import annotations

from pathlib import Path


def write_file_safe(path: Path, content: str, *, force: bool = False) -> bool:
    """
    Write `content` to `path` only if the file does not already exist,
    unless `force=True`.

    Returns True if the file was written, False if it was skipped.
    """
    if path.exists() and not force:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def ensure_dir(path: Path) -> None:
    """Create directory (and parents) if it does not exist."""
    path.mkdir(parents=True, exist_ok=True)


def touch_file(path: Path, *, force: bool = False) -> bool:
    """
    Create an empty file at `path` if it does not exist.
    Returns True if created, False if skipped.
    """
    if path.exists() and not force:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch()
    return True
