# SPINE Beta Implementation Report

*Last updated: 2026-04-09 — Issue #64*

---

## Issue #64 — `spine evidence list` + `spine decision list`

**Branch:** `beta/usability64-evidence-decision-list`  
**Status:** ✅ Implemented — pending PR

### Problem

Governance records (evidence, decisions) were write-only from the CLI.
Agents and operators could append records but had no clean way to inspect them.

### Solution

Added `list` sub-commands to the existing `evidence` and `decision` command groups.

### Commands Added

| Command | Flags |
|---|---|
| `spine evidence list` | `--cwd PATH`, `--json` |
| `spine decision list` | `--cwd PATH`, `--json` |

### Output Behavior

**Human-readable (default):**
- Evidence: `[kind]  description  url (if set)  date`
- Decision: `title  date` / `  Decision: ...` / `  Alternatives: ...` (if set)
- Empty state: `No evidence records found.` / `No decision records found.`

**`--json` shape:**
```json
{
  "ok": true,
  "count": N,
  "records": [
    {
      "kind": "commit",
      "description": "...",
      "evidence_url": "...",
      "created_at": "2026-04-09T..."
    }
  ]
}
```

```json
{
  "ok": true,
  "count": N,
  "records": [
    {
      "title": "...",
      "why": "...",
      "decision": "...",
      "alternatives": ["..."],
      "created_at": "2026-04-09T..."
    }
  ]
}
```

**Ordering:** ascending by `created_at` (deterministic, stable).

### Files Changed

| File | Change |
|---|---|
| `src/spine/cli/evidence_cmd.py` | Added `evidence_list` command |
| `src/spine/cli/decision_cmd.py` | Added `decision_list` command |
| `src/spine/services/evidence_service.py` | Added `list()` method |
| `src/spine/services/decision_service.py` | Added `list()` method |
| `tests/test_evidence_list.py` | New — 9 focused tests |
| `tests/test_decision_list.py` | New — 9 focused tests |
| `docs/SPINE_STATUS.md` | Updated blocker count (4 → 3), #64 marked fixed |
| `docs/SPINE_FEATURE_BACKLOG.md` | #64 marked ✅ Fixed |
| `docs/SPINE_BETA_IMPLEMENTATION_REPORT.md` | This file (new) |

### Test Results

- New tests: **18 passed** (9 evidence list + 9 decision list)
- Full suite: **530 passed**, 0 failed

### SPINE Governance Commands Run

```
uv run spine mission show
uv run spine doctor
uv run spine decision add --title "Implement spine evidence list and spine decision list (#64)" ...
uv run spine evidence add --kind commit --description "Implemented spine evidence list and spine decision list..."
uv run spine review weekly --recommendation continue --notes "Pre-beta-exit usability fix: #64..."
```

### What Remains in Blocker Lane

| # | Issue | Status |
|---|---|---|
| #65 | `check before-pr --json` structured doctor detail | Open |
| #66 | `check before-work` no-brief advisory not exit 1 | Open |
| #60 | SECURITY_BASELINE wrong repo name | Open |

Beta exit requires #65, #66, #60, and #51 to be cleared.
