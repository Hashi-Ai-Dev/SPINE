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
    invoke_without_command=True,
)


@app.callback()
def _root(ctx: typer.Context) -> None:
    """SPINE — local-first, repo-native mission governor."""
    # Callback exists to prevent Typer 0.24 from flattening the single
    # subcommand into the top-level app. Without it, `spine init` would
    # fail because Typer promotes the sole command to the root and treats
    # `init` as an unexpected extra argument.
    if ctx.invoked_subcommand is None:
        typer.echo(ctx.get_help())
        raise typer.Exit(0)
