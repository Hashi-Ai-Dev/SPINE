"""Tests for Issue #49 — machine-readable consistency for governance write flows.

Covers --json output contracts for all write-oriented CLI commands:
- spine evidence add --json
- spine decision add --json
- spine drafts list --json
- spine drafts confirm --json
- spine mission refine --json
- spine mission confirm --json
- spine mission drafts --json

Contract assertions:
- Exit codes: 0=success, 1=validation, 2=context (unchanged)
- JSON output: valid, parseable, deterministic shape
- ok=True on success, error+exit_code on failure
- draft_id present when draft mode is used
- No human-readable chatter mixed into JSON output
"""

from __future__ import annotations

import json
import os
from pathlib import Path

from typer.testing import CliRunner

from spine.main import app

runner = CliRunner()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def make_git_repo(tmp_path: Path) -> Path:
    (tmp_path / ".git").mkdir()
    return tmp_path


def run_init(tmp_path: Path) -> None:
    result = runner.invoke(app, ["init", "--cwd", str(tmp_path)])
    assert result.exit_code == 0, result.output


def run_cmd(args: list[str], cwd: Path | None = None) -> tuple[int, str]:
    if cwd is not None:
        original = os.getcwd()
        try:
            os.chdir(cwd)
            result = runner.invoke(app, args)
        finally:
            os.chdir(original)
    else:
        result = runner.invoke(app, args)
    return result.exit_code, result.output


# ---------------------------------------------------------------------------
# spine evidence add --json
# ---------------------------------------------------------------------------


class TestEvidenceAddJson:
    def test_evidence_add_json_success_shape(self, tmp_path: Path) -> None:
        """evidence add --json returns valid JSON with ok=True and record fields."""
        make_git_repo(tmp_path)
        run_init(tmp_path)

        code, out = run_cmd(
            ["evidence", "add", "--kind", "commit", "--description", "test commit", "--json"],
            cwd=tmp_path,
        )
        assert code == 0, out

        data = json.loads(out)
        assert data["ok"] is True
        assert data["kind"] == "commit"
        assert data["description"] == "test commit"
        assert "created_at" in data
        assert "evidence_url" in data

    def test_evidence_add_json_draft_shape(self, tmp_path: Path) -> None:
        """evidence add --draft --json returns JSON with draft_id and draft=True."""
        make_git_repo(tmp_path)
        run_init(tmp_path)

        code, out = run_cmd(
            ["evidence", "add", "--kind", "pr", "--description", "draft pr", "--draft", "--json"],
            cwd=tmp_path,
        )
        assert code == 0, out

        data = json.loads(out)
        assert data["ok"] is True
        assert data["draft"] is True
        assert "draft_id" in data
        assert data["draft_id"].startswith("evidence-")
        assert data["kind"] == "pr"

    def test_evidence_add_json_url_field(self, tmp_path: Path) -> None:
        """evidence add --json includes evidence_url in output."""
        make_git_repo(tmp_path)
        run_init(tmp_path)

        code, out = run_cmd(
            ["evidence", "add", "--kind", "pr", "--url", "https://example.com/pr/1", "--json"],
            cwd=tmp_path,
        )
        assert code == 0, out

        data = json.loads(out)
        assert data["evidence_url"] == "https://example.com/pr/1"

    def test_evidence_add_json_context_failure(self, tmp_path: Path) -> None:
        """evidence add --json with no git repo exits 2 with JSON error."""
        code, out = run_cmd(
            ["evidence", "add", "--kind", "commit", "--cwd", str(tmp_path), "--json"],
        )
        assert code == 2, out

        data = json.loads(out)
        assert "error" in data
        assert data["exit_code"] == 2

    def test_evidence_add_json_stdout_pure(self, tmp_path: Path) -> None:
        """evidence add --json stdout is parseable JSON only — no chatter."""
        make_git_repo(tmp_path)
        run_init(tmp_path)

        code, out = run_cmd(
            ["evidence", "add", "--kind", "demo", "--description", "a demo", "--json"],
            cwd=tmp_path,
        )
        assert code == 0
        parsed = json.loads(out.strip())
        assert isinstance(parsed, dict)


# ---------------------------------------------------------------------------
# spine decision add --json
# ---------------------------------------------------------------------------


class TestDecisionAddJson:
    def test_decision_add_json_success_shape(self, tmp_path: Path) -> None:
        """decision add --json returns valid JSON with ok=True and record fields."""
        make_git_repo(tmp_path)
        run_init(tmp_path)

        code, out = run_cmd(
            [
                "decision", "add",
                "--title", "Use JSON output",
                "--why", "Agents need machine-readable data",
                "--decision", "Add --json to write commands",
                "--json",
            ],
            cwd=tmp_path,
        )
        assert code == 0, out

        data = json.loads(out)
        assert data["ok"] is True
        assert data["title"] == "Use JSON output"
        assert data["why"] == "Agents need machine-readable data"
        assert data["decision"] == "Add --json to write commands"
        assert "created_at" in data
        assert "alternatives" in data

    def test_decision_add_json_draft_shape(self, tmp_path: Path) -> None:
        """decision add --draft --json returns JSON with draft_id and draft=True."""
        make_git_repo(tmp_path)
        run_init(tmp_path)

        code, out = run_cmd(
            [
                "decision", "add",
                "--title", "Draft decision",
                "--why", "Exploring option",
                "--decision", "Do X",
                "--draft",
                "--json",
            ],
            cwd=tmp_path,
        )
        assert code == 0, out

        data = json.loads(out)
        assert data["ok"] is True
        assert data["draft"] is True
        assert "draft_id" in data
        assert data["draft_id"].startswith("decision-")
        assert data["title"] == "Draft decision"

    def test_decision_add_json_alternatives_field(self, tmp_path: Path) -> None:
        """decision add --json includes alternatives list."""
        make_git_repo(tmp_path)
        run_init(tmp_path)

        code, out = run_cmd(
            [
                "decision", "add",
                "--title", "T",
                "--why", "W",
                "--decision", "D",
                "--alternatives", "option A, option B",
                "--json",
            ],
            cwd=tmp_path,
        )
        assert code == 0, out

        data = json.loads(out)
        assert "alternatives" in data
        assert len(data["alternatives"]) == 2

    def test_decision_add_json_validation_failure(self, tmp_path: Path) -> None:
        """decision add --json with empty required field exits 1 with JSON error."""
        make_git_repo(tmp_path)
        run_init(tmp_path)

        code, out = run_cmd(
            [
                "decision", "add",
                "--title", "   ",
                "--why", "W",
                "--decision", "D",
                "--json",
            ],
            cwd=tmp_path,
        )
        assert code == 1, out

        data = json.loads(out)
        assert "error" in data
        assert data["exit_code"] == 1

    def test_decision_add_json_context_failure(self, tmp_path: Path) -> None:
        """decision add --json with no git repo exits 2 with JSON error."""
        code, out = run_cmd(
            [
                "decision", "add",
                "--title", "T", "--why", "W", "--decision", "D",
                "--cwd", str(tmp_path),
                "--json",
            ],
        )
        assert code == 2, out

        data = json.loads(out)
        assert "error" in data
        assert data["exit_code"] == 2

    def test_decision_add_json_stdout_pure(self, tmp_path: Path) -> None:
        """decision add --json stdout is parseable JSON only."""
        make_git_repo(tmp_path)
        run_init(tmp_path)

        code, out = run_cmd(
            ["decision", "add", "--title", "T", "--why", "W", "--decision", "D", "--json"],
            cwd=tmp_path,
        )
        assert code == 0
        parsed = json.loads(out.strip())
        assert isinstance(parsed, dict)


# ---------------------------------------------------------------------------
# spine drafts list --json
# ---------------------------------------------------------------------------


class TestDraftsListJson:
    def test_drafts_list_json_empty_shape(self, tmp_path: Path) -> None:
        """drafts list --json with no drafts returns ok=True, count=0, drafts=[]."""
        make_git_repo(tmp_path)
        run_init(tmp_path)

        result = runner.invoke(app, ["drafts", "list", "--cwd", str(tmp_path), "--json"])
        assert result.exit_code == 0, result.output

        data = json.loads(result.output)
        assert data["ok"] is True
        assert data["count"] == 0
        assert data["drafts"] == []

    def test_drafts_list_json_with_evidence_draft(self, tmp_path: Path) -> None:
        """drafts list --json includes evidence draft entries with expected fields."""
        make_git_repo(tmp_path)
        run_init(tmp_path)

        # Create a draft
        runner.invoke(app, [
            "evidence", "add", "--kind", "commit",
            "--description", "draft", "--draft", "--cwd", str(tmp_path),
        ])

        result = runner.invoke(app, ["drafts", "list", "--cwd", str(tmp_path), "--json"])
        assert result.exit_code == 0, result.output

        data = json.loads(result.output)
        assert data["ok"] is True
        assert data["count"] == 1
        assert len(data["drafts"]) == 1

        entry = data["drafts"][0]
        assert "draft_id" in entry
        assert entry.get("_record_type") == "evidence"
        assert entry.get("kind") == "commit"

    def test_drafts_list_json_with_decision_draft(self, tmp_path: Path) -> None:
        """drafts list --json includes decision draft entries."""
        make_git_repo(tmp_path)
        run_init(tmp_path)

        runner.invoke(app, [
            "decision", "add",
            "--title", "Decision draft",
            "--why", "W",
            "--decision", "D",
            "--draft",
            "--cwd", str(tmp_path),
        ])

        result = runner.invoke(app, ["drafts", "list", "--cwd", str(tmp_path), "--json"])
        assert result.exit_code == 0, result.output

        data = json.loads(result.output)
        assert data["count"] == 1
        entry = data["drafts"][0]
        assert entry.get("_record_type") == "decision"
        assert entry.get("title") == "Decision draft"

    def test_drafts_list_json_context_failure(self, tmp_path: Path) -> None:
        """drafts list --json with no git repo exits 2 with JSON error."""
        result = runner.invoke(app, ["drafts", "list", "--cwd", str(tmp_path), "--json"])
        assert result.exit_code == 2, result.output

        data = json.loads(result.output)
        assert "error" in data
        assert data["exit_code"] == 2

    def test_drafts_list_json_stdout_pure(self, tmp_path: Path) -> None:
        """drafts list --json stdout is parseable JSON only."""
        make_git_repo(tmp_path)
        run_init(tmp_path)

        result = runner.invoke(app, ["drafts", "list", "--cwd", str(tmp_path), "--json"])
        assert result.exit_code == 0
        parsed = json.loads(result.output.strip())
        assert isinstance(parsed, dict)


# ---------------------------------------------------------------------------
# spine drafts confirm --json
# ---------------------------------------------------------------------------


class TestDraftsConfirmJson:
    def test_drafts_confirm_json_evidence_success_shape(self, tmp_path: Path) -> None:
        """drafts confirm --json on evidence draft returns ok=True, draft_id, record_type."""
        make_git_repo(tmp_path)
        run_init(tmp_path)

        # Create draft and capture draft_id
        result = runner.invoke(app, [
            "evidence", "add", "--kind", "commit",
            "--description", "confirm me", "--draft", "--json",
            "--cwd", str(tmp_path),
        ])
        assert result.exit_code == 0
        draft_data = json.loads(result.output)
        draft_id = draft_data["draft_id"]

        # Confirm it
        result = runner.invoke(app, [
            "drafts", "confirm", draft_id, "--cwd", str(tmp_path), "--json",
        ])
        assert result.exit_code == 0, result.output

        data = json.loads(result.output)
        assert data["ok"] is True
        assert data["draft_id"] == draft_id
        assert data["record_type"] == "evidence"
        assert data["kind"] == "commit"
        assert data["description"] == "confirm me"

    def test_drafts_confirm_json_decision_success_shape(self, tmp_path: Path) -> None:
        """drafts confirm --json on decision draft returns ok=True and record fields."""
        make_git_repo(tmp_path)
        run_init(tmp_path)

        result = runner.invoke(app, [
            "decision", "add",
            "--title", "Confirm me decision",
            "--why", "W", "--decision", "D",
            "--draft", "--json",
            "--cwd", str(tmp_path),
        ])
        assert result.exit_code == 0
        draft_data = json.loads(result.output)
        draft_id = draft_data["draft_id"]

        result = runner.invoke(app, [
            "drafts", "confirm", draft_id, "--cwd", str(tmp_path), "--json",
        ])
        assert result.exit_code == 0, result.output

        data = json.loads(result.output)
        assert data["ok"] is True
        assert data["record_type"] == "decision"
        assert data["title"] == "Confirm me decision"

    def test_drafts_confirm_json_not_found_exits_1(self, tmp_path: Path) -> None:
        """drafts confirm --json with missing draft_id exits 1 with JSON error."""
        make_git_repo(tmp_path)
        run_init(tmp_path)

        result = runner.invoke(app, [
            "drafts", "confirm", "evidence-nonexistent", "--cwd", str(tmp_path), "--json",
        ])
        assert result.exit_code == 1, result.output

        data = json.loads(result.output)
        assert "error" in data
        assert data["exit_code"] == 1

    def test_drafts_confirm_json_context_failure(self, tmp_path: Path) -> None:
        """drafts confirm --json with no git repo exits 2 with JSON error."""
        result = runner.invoke(app, [
            "drafts", "confirm", "any-id", "--cwd", str(tmp_path), "--json",
        ])
        assert result.exit_code == 2, result.output

        data = json.loads(result.output)
        assert "error" in data
        assert data["exit_code"] == 2

    def test_drafts_confirm_json_promotes_to_canonical(self, tmp_path: Path) -> None:
        """drafts confirm --json still promotes draft to canonical JSONL."""
        make_git_repo(tmp_path)
        run_init(tmp_path)

        result = runner.invoke(app, [
            "evidence", "add", "--kind", "test_pass",
            "--description", "passing tests", "--draft", "--json",
            "--cwd", str(tmp_path),
        ])
        draft_id = json.loads(result.output)["draft_id"]

        runner.invoke(app, [
            "drafts", "confirm", draft_id, "--cwd", str(tmp_path), "--json",
        ])

        evidence_file = tmp_path / ".spine" / "evidence.jsonl"
        lines = [l for l in evidence_file.read_text().splitlines() if l.strip()]
        assert len(lines) == 1
        record = json.loads(lines[0])
        assert record["kind"] == "test_pass"

        # Draft file must be deleted
        drafts_dir = tmp_path / ".spine" / "drafts"
        assert not (drafts_dir / f"{draft_id}.json").exists()


# ---------------------------------------------------------------------------
# spine mission refine --json
# ---------------------------------------------------------------------------


class TestMissionRefineJson:
    def test_mission_refine_json_success_shape(self, tmp_path: Path) -> None:
        """mission refine --json returns ok=True, draft_id, draft_path, and mission fields."""
        make_git_repo(tmp_path)
        run_init(tmp_path)

        result = runner.invoke(app, [
            "mission", "refine",
            "--title", "Refined title",
            "--cwd", str(tmp_path),
            "--json",
        ])
        assert result.exit_code == 0, result.output

        data = json.loads(result.output)
        assert data["ok"] is True
        assert "draft_id" in data
        assert data["draft_id"].startswith("mission-")
        assert "draft_path" in data
        assert data["title"] == "Refined title"

    def test_mission_refine_json_stdout_pure(self, tmp_path: Path) -> None:
        """mission refine --json stdout is parseable JSON only."""
        make_git_repo(tmp_path)
        run_init(tmp_path)

        result = runner.invoke(app, [
            "mission", "refine", "--title", "T", "--cwd", str(tmp_path), "--json",
        ])
        assert result.exit_code == 0
        parsed = json.loads(result.output.strip())
        assert isinstance(parsed, dict)

    def test_mission_refine_json_context_failure(self, tmp_path: Path) -> None:
        """mission refine --json with no .spine/ exits 2 with JSON error."""
        make_git_repo(tmp_path)
        # No spine init

        result = runner.invoke(app, [
            "mission", "refine", "--title", "T", "--cwd", str(tmp_path), "--json",
        ])
        assert result.exit_code == 2, result.output

        data = json.loads(result.output)
        assert "error" in data
        assert data["exit_code"] == 2


# ---------------------------------------------------------------------------
# spine mission confirm --json
# ---------------------------------------------------------------------------


class TestMissionConfirmJson:
    def test_mission_confirm_json_success_shape(self, tmp_path: Path) -> None:
        """mission confirm --json returns ok=True, draft_id, and mission fields."""
        make_git_repo(tmp_path)
        run_init(tmp_path)

        # Create a draft first
        refine_result = runner.invoke(app, [
            "mission", "refine",
            "--title", "Confirmed mission",
            "--cwd", str(tmp_path),
            "--json",
        ])
        assert refine_result.exit_code == 0
        draft_id = json.loads(refine_result.output)["draft_id"]

        result = runner.invoke(app, [
            "mission", "confirm", draft_id, "--cwd", str(tmp_path), "--json",
        ])
        assert result.exit_code == 0, result.output

        data = json.loads(result.output)
        assert data["ok"] is True
        assert data["draft_id"] == draft_id
        assert data["title"] == "Confirmed mission"
        assert "status" in data
        assert "updated_at" in data

    def test_mission_confirm_json_not_found_exits_1(self, tmp_path: Path) -> None:
        """mission confirm --json with missing draft exits 1 with JSON error."""
        make_git_repo(tmp_path)
        run_init(tmp_path)

        result = runner.invoke(app, [
            "mission", "confirm", "mission-nonexistent", "--cwd", str(tmp_path), "--json",
        ])
        assert result.exit_code == 1, result.output

        data = json.loads(result.output)
        assert "error" in data
        assert data["exit_code"] == 1

    def test_mission_confirm_json_context_failure(self, tmp_path: Path) -> None:
        """mission confirm --json with no git repo exits 2 with JSON error."""
        result = runner.invoke(app, [
            "mission", "confirm", "any-id", "--cwd", str(tmp_path), "--json",
        ])
        assert result.exit_code == 2, result.output

        data = json.loads(result.output)
        assert "error" in data
        assert data["exit_code"] == 2


# ---------------------------------------------------------------------------
# spine mission drafts --json
# ---------------------------------------------------------------------------


class TestMissionDraftsJson:
    def test_mission_drafts_json_empty_shape(self, tmp_path: Path) -> None:
        """mission drafts --json with no drafts returns ok=True, count=0, drafts=[]."""
        make_git_repo(tmp_path)
        run_init(tmp_path)

        result = runner.invoke(app, ["mission", "drafts", "--cwd", str(tmp_path), "--json"])
        assert result.exit_code == 0, result.output

        data = json.loads(result.output)
        assert data["ok"] is True
        assert data["count"] == 0
        assert data["drafts"] == []

    def test_mission_drafts_json_with_draft(self, tmp_path: Path) -> None:
        """mission drafts --json with one draft returns count=1 and draft entry."""
        make_git_repo(tmp_path)
        run_init(tmp_path)

        refine_result = runner.invoke(app, [
            "mission", "refine",
            "--title", "Draft mission title",
            "--cwd", str(tmp_path),
            "--json",
        ])
        assert refine_result.exit_code == 0

        result = runner.invoke(app, ["mission", "drafts", "--cwd", str(tmp_path), "--json"])
        assert result.exit_code == 0, result.output

        data = json.loads(result.output)
        assert data["ok"] is True
        assert data["count"] == 1
        assert len(data["drafts"]) == 1

        entry = data["drafts"][0]
        assert "draft_id" in entry
        assert entry.get("title") == "Draft mission title"
        assert "status" in entry

    def test_mission_drafts_json_context_failure(self, tmp_path: Path) -> None:
        """mission drafts --json with no git repo exits 2 with JSON error."""
        result = runner.invoke(app, ["mission", "drafts", "--cwd", str(tmp_path), "--json"])
        assert result.exit_code == 2, result.output

        data = json.loads(result.output)
        assert "error" in data
        assert data["exit_code"] == 2

    def test_mission_drafts_json_stdout_pure(self, tmp_path: Path) -> None:
        """mission drafts --json stdout is parseable JSON only."""
        make_git_repo(tmp_path)
        run_init(tmp_path)

        result = runner.invoke(app, ["mission", "drafts", "--cwd", str(tmp_path), "--json"])
        assert result.exit_code == 0
        parsed = json.loads(result.output.strip())
        assert isinstance(parsed, dict)


# ---------------------------------------------------------------------------
# Exit code contract: write commands (unchanged by --json)
# ---------------------------------------------------------------------------


class TestWriteFlowExitCodes:
    def test_evidence_add_success_exits_0(self, tmp_path: Path) -> None:
        make_git_repo(tmp_path)
        run_init(tmp_path)
        code, out = run_cmd(
            ["evidence", "add", "--kind", "commit", "--cwd", str(tmp_path)],
        )
        assert code == 0, out

    def test_evidence_add_no_git_exits_2(self, tmp_path: Path) -> None:
        code, out = run_cmd(
            ["evidence", "add", "--kind", "commit", "--cwd", str(tmp_path)],
        )
        assert code == 2, out

    def test_decision_add_success_exits_0(self, tmp_path: Path) -> None:
        make_git_repo(tmp_path)
        run_init(tmp_path)
        code, out = run_cmd(
            ["decision", "add", "--title", "T", "--why", "W", "--decision", "D",
             "--cwd", str(tmp_path)],
        )
        assert code == 0, out

    def test_decision_add_validation_exits_1(self, tmp_path: Path) -> None:
        make_git_repo(tmp_path)
        run_init(tmp_path)
        code, out = run_cmd(
            ["decision", "add", "--title", "  ", "--why", "W", "--decision", "D",
             "--cwd", str(tmp_path)],
        )
        assert code == 1, out

    def test_drafts_list_no_git_exits_2(self, tmp_path: Path) -> None:
        result = runner.invoke(app, ["drafts", "list", "--cwd", str(tmp_path)])
        assert result.exit_code == 2, result.output

    def test_drafts_confirm_not_found_exits_1(self, tmp_path: Path) -> None:
        make_git_repo(tmp_path)
        run_init(tmp_path)
        result = runner.invoke(app, [
            "drafts", "confirm", "evidence-doesnotexist", "--cwd", str(tmp_path),
        ])
        assert result.exit_code == 1, result.output
