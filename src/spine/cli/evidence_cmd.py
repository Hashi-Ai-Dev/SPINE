"""spine evidence add command — spec-compliant nesting."""

from __future__ import annotations

import json
from pathlib import Path

import typer
from rich.console import Console

from spine.cli.app import app, resolve_roots, EXIT_VALIDATION, EXIT_CONTEXT
from spine.models.evidence import EVIDENCE_KINDS
from spine.services.evidence_service import EvidenceService, EvidenceValidationError

console = Console()

# ---------------------------------------------------------------------------
# Evidence command group (spine evidence <action>)
# ---------------------------------------------------------------------------
evidence_app = typer.Typer()
app.add_typer(evidence_app, name="evidence", help="Manage evidence records.")


@evidence_app.command("add", help="Add an evidence record to .spine/evidence.jsonl.")
def evidence_add(
    cwd: Path | None = typer.Option(
        None,
        "--cwd",
        help="Target repository path. Overrides SPINE_ROOT. Precedence: --cwd > SPINE_ROOT > cwd.",
    ),
    kind: EVIDENCE_KINDS = typer.Option(..., "--kind", "-k", help="Evidence kind"),
    description: str = typer.Option("", "--description", "-d", help="Description of the evidence"),
    url: str = typer.Option("", "--url", help="URL or reference for the evidence"),
    draft: bool = typer.Option(
        False,
        "--draft",
        help="[Beta] Save as a draft under .spine/drafts/ instead of appending to evidence.jsonl. Use 'spine drafts confirm <id>' to promote.",
    ),
    json_output: bool = typer.Option(
        False,
        "--json",
        help="Output result as JSON (machine-readable). Exit codes still apply.",
    ),
) -> None:
    """
    Add an evidence record to .spine/evidence.jsonl.

    Allowed kinds: brief_generated, commit, pr, test_pass, review_done,
                   demo, user_feedback, payment, kill, narrow

    Use --draft to save provisionally to .spine/drafts/ without touching canonical state.

    Exit codes:
      0  Success
      1  Validation failure — invalid kind or field
      2  Context failure   — repo not found or .spine/ missing
    """
    try:
        repo_root, spine_root = resolve_roots(cwd)
    except Exception as exc:
        if json_output:
            print(json.dumps({"error": str(exc), "exit_code": EXIT_CONTEXT}, indent=2))
        else:
            console.print(f"[bold red]Error:[/bold red] {exc}")
        raise typer.Exit(EXIT_CONTEXT)

    service = EvidenceService(repo_root, spine_root=spine_root)
    try:
        if draft:
            evidence, draft_id = service.add_draft(kind=kind, description=description, evidence_url=url)
            if json_output:
                data = {"ok": True, "draft": True, "draft_id": draft_id, **evidence.to_json()}
                print(json.dumps(data, indent=2))
            else:
                console.print(f"[bold yellow]Evidence draft saved:[/bold yellow] [{evidence.kind}] {evidence.description or '(no description)'}")
                console.print(f"  Draft ID: {draft_id}")
                console.print(f"  Promote with: spine drafts confirm {draft_id}")
        else:
            evidence = service.add(kind=kind, description=description, evidence_url=url)
            if json_output:
                data = {"ok": True, **evidence.to_json()}
                print(json.dumps(data, indent=2))
            else:
                console.print(f"[bold green]Evidence added:[/bold green] [{evidence.kind}] {evidence.description or '(no description)'}")
                console.print(f"  Created at: {evidence.created_at}")
    except EvidenceValidationError as exc:
        if json_output:
            print(json.dumps({"error": str(exc), "exit_code": EXIT_VALIDATION}, indent=2))
        else:
            console.print(f"[bold red]Validation error:[/bold red] {exc}")
        raise typer.Exit(EXIT_VALIDATION)
