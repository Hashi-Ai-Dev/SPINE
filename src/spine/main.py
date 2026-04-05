"""SPINE CLI entry point."""

from __future__ import annotations

# Import app and all commands so they register on the app object.
from spine.cli.app import app
import spine.cli.init_cmd  # noqa: F401 — registers @app.command("init")

__all__ = ["app"]
