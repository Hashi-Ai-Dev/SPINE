"""Git repo root detection and .spine path resolution."""

from __future__ import annotations

import subprocess
from pathlib import Path


class GitRepoNotFoundError(Exception):
    """Raised when no git repository can be found."""


def find_git_root(start: Path | None = None) -> Path:
    """
    Walk up from `start` (default: cwd) to find the git repository root.

    Uses `git rev-parse --show-toplevel` as the primary mechanism (handles
    worktrees and .git files). Falls back to a pure-Python parent-walk for
    environments where git is not in PATH.

    Raises GitRepoNotFoundError if no git root is found.
    """
    if start is None:
        start = Path.cwd()

    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            cwd=str(start),
            timeout=5,
        )
        if result.returncode == 0:
            return Path(result.stdout.strip())
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass  # git not in PATH; fall through to pure-Python walk

    # Pure-Python fallback: walk up looking for .git
    current = start.resolve()
    while True:
        if (current / ".git").exists():
            return current
        parent = current.parent
        if parent == current:
            break
        current = parent

    raise GitRepoNotFoundError(
        f"No git repository found at or above: {start}"
    )


def spine_dir(repo_root: Path) -> Path:
    from spine.constants import SPINE_DIR
    return repo_root / SPINE_DIR
