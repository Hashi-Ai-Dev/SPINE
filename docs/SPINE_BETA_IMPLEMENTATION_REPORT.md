# SPINE Beta Implementation Report

**Repo:** `Hashi-Ai-Dev/SPINE`
**Branch:** `claude/issue31-check-before-pr-6z236`
**Date:** 2026-04-08

---

## Issue #31 — `spine check before-pr` preflight checkpoint

### Issue targeted

GitHub Issue #31: "Beta: `spine check before-pr` — preflight checkpoint command"

First Beta implementation slice. Adds an explicit, local, deterministic preflight
governance checkpoint before opening a PR or pushing a batch of work.

---

### Checkpoint behavior implemented

`spine check before-pr [--cwd PATH] [--json]`

Runs a bounded set of governance checks against a SPINE-instrumented repository
and reports what passed and what needs review. Does **not** mutate any state,
make network calls, install hooks, or take any hidden action.

---

### Checks included

| Check | Pass condition | Review-recommended trigger |
|---|---|---|
| `spine_dir` | `.spine/` directory exists | Missing `.spine/` |
| `mission` | `mission.yaml` present and parses cleanly | Missing or corrupt `mission.yaml` |
| `doctor` | No doctor errors (warnings surface as warn) | Any doctor error; warnings → warn |
| `drift` | No drift events in `drift.jsonl` | Any drift events logged |
| `evidence` | At least 1 evidence record present | Empty or missing `evidence.jsonl` |
| `decisions` | At least 1 decision record present | Empty or missing `decisions.jsonl` |

If `.spine/` is missing, further checks are skipped (no point checking files that can't exist).

---

### Output / exit behavior

**Human-readable output (default):**
- Context line: `repo: <path>  branch: <branch>  default: <default>`
- Table: one row per check (`name`, `status`, `detail`)
- Final result line: `Result: PASS` or `Result: REVIEW RECOMMENDED`

**JSON output (`--json`):**
```json
{
  "result": "pass | review_recommended",
  "passed": true | false,
  "repo": "<path>",
  "branch": "<branch>",
  "default_branch": "<branch | null>",
  "checked_at": "<ISO 8601>",
  "checks": [
    { "name": "<name>", "status": "pass | warn | fail", "message": "<message>" }
  ]
}
```

**Exit codes (stable):**
- `0` — All checks passed
- `1` — Review recommended (one or more checks are warn or fail)
- `2` — Context failure (no git repo, cannot resolve paths)

Consistent with existing SPINE exit-code contract (EXIT_OK=0, EXIT_VALIDATION=1, EXIT_CONTEXT=2).

---

### Files changed

**New files:**
- `src/spine/services/check_service.py` — `CheckService` business logic (pure read, no mutation)
- `src/spine/cli/check_cmd.py` — CLI command (`check_app` Typer group, `before-pr` subcommand)
- `tests/test_check_before_pr.py` — 18 focused tests
- `docs/SPINE_BETA_IMPLEMENTATION_REPORT.md` — this file

**Modified files:**
- `src/spine/main.py` — registered `spine.cli.check_cmd`
- `src/spine/services/__init__.py` — exported `CheckService`, `BeforePrResult`, `CheckItem`
- `docs/SPINE_STATUS.md` — updated Issue #31 status to Implemented
- `docs/SPINE_FEATURE_BACKLOG.md` — updated #31 to DONE

---

### Test results

```
249 passed in 8.76s
```

All 18 new tests pass. All 231 pre-existing tests continue to pass.

**New test coverage:**
- Command registration
- Pass path (all checks green, exit 0)
- Review-recommended path: missing .spine/, corrupt mission, no evidence, no decisions, drift present
- `--cwd` support (no process cwd change)
- Invalid `--cwd` → exit 2
- JSON output structure and exit code alignment
- Deterministic behavior (same result on two consecutive runs)
- No state mutation (`.spine/` file set unchanged after run)
- Human output includes repo path and final Result line

---

### What was explicitly deferred

Per the mission constraint (Issue #31 only):

| Deferred | Target issue |
|---|---|
| `spine check before-work` | Not in #31 |
| Hook installation / `spine hooks install` | #34 |
| Handoff / PR-prep summary generation | #32 |
| Draft evidence/decision flows | #33 |
| Automatic remediation | Out of scope entirely |
| PR creation or PR description generation | Out of scope entirely |
| Hidden blocking / gating behavior | Out of scope entirely |

---

### Architecture notes

- `CheckService` composes `DoctorService` rather than duplicating checks.
- `DriftService.get_open_drift()` exists but reads from `drift.jsonl` (already-logged drift). The `before-pr` check reads `drift.jsonl` directly for lightweight presence check — it does NOT run a new scan (no mutation, no append).
- Exit code `1` means "review recommended" not "error" — consistent with Issue #31 spec.
- No hidden logging, no silent mutation, no network calls, no model calls.
