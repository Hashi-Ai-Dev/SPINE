"""Top-level Typer application factory."""

from __future__ import annotations

import typer
from rich.console import Console

console = Console()
err_console = Console(stderr=True)

app = typer.Typer(
    name="spine",
    help=(
        "SPINE — local-first, repo-native mission governor.\n\n"
        "Phase 1: repository initialization only.\n"
        "Run [bold]spine init[/bold] to scaffold .spine/ governance state."
    ),
    rich_markup_mode="rich",
    no_args_is_help=True,
    add_completion=False,
)
