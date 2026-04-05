# Milestone 1 — SPINE Phase 1: Repository Bootstrap

## Scope

Phase 1 implements exactly one CLI command: `spine init`.

No other commands are implemented. No MCP, no drift scanning, no review generation, no run management, no model inference, no network access, no background processes, no web UI.

## What `spine init` does

When run inside a git repository, `spine init`:

1. Detects the repository root via `git rev-parse --show-toplevel`
2. Creates the `.spine/` directory
3. Generates canonical governance files if they do not already exist
4. Creates agent guidance files (`AGENTS.md`, `CLAUDE.md`) at the repo root
5. Creates AI tool configuration files (`.claude/settings.json`, `.codex/config.toml`)
6. Prints a Rich-formatted summary of created and skipped files

### Flags

| Flag | Effect |
|------|--------|
| `--force` | Overwrite existing files |
| `--allow-no-git` | Allow init outside a git repository |

### Exit codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 2 | Not in a git repo |
| 3 | Conflicting files without `--force` |

## Generated files

### `.spine/mission.yaml`

Defines the active mission. Validated by `MissionModel` (Pydantic v2). Fields include:
- `id`, `title`, `status` — identity and lifecycle
- `target_user`, `user_problem`, `one_sentence_promise` — mission clarity
- `success_metric` — typed (milestone / metric / user_signal)
- `allowed_scope`, `forbidden_expansions` — scope boundaries for agents
- `kill_conditions`, `proof_requirements` — exit criteria
- `created_at`, `updated_at` — UTC ISO 8601 timestamps

### `.spine/constraints.yaml`

Defines operational constraints. Validated by `ConstraintsModel`. Fields include:
- `work_schedule` — timezone and blocked time windows
- `parallel_limits` — max concurrent missions and runs
- `budget` — monthly USD soft cap
- `routing_preferences` — local vs frontier model routing
- `behavior_rules` — agent behavioral flags

### JSONL append logs

Empty at init time. Future phases append newline-delimited JSON records:

| File | Purpose |
|------|---------|
| `opportunities.jsonl` | Candidate opportunities identified during runs |
| `not_now.jsonl` | Deferred ideas and features |
| `evidence.jsonl` | Evidence collected for weekly review |
| `decisions.jsonl` | Decision record with rationale |
| `drift.jsonl` | Scope drift detection events |
| `runs.jsonl` | Agent run metadata |

### Subdirectories

| Directory | Purpose |
|-----------|---------|
| `.spine/reviews/` | Generated weekly review documents |
| `.spine/briefs/` | Mission briefs for agent context |
| `.spine/skills/` | Agent skill definitions |
| `.spine/checks/` | Automated check scripts |

## Why YAML and JSONL are canonical

**YAML** (`.spine/mission.yaml`, `.spine/constraints.yaml`) is human-readable and diff-friendly. Mission state changes should be reviewable in git history. Pydantic v2 models provide schema validation and clear error messages when fields are wrong.

**JSONL** (append logs) is append-safe, streamable, and trivially parseable. Each record is an independent JSON object on its own line. No locking required for sequential append. Future tooling can stream records without loading the full file.

**SQLite** (`.spine/state.db`) is a future projection target only. Phase 1 creates an empty placeholder file but never writes SQLite. The canonical state always lives in YAML/JSONL; SQLite is derived and can be rebuilt at any time.

## Why full governance features are deferred

The `.spine/` contract does not exist until `spine init` runs. Every subsequent feature (drift scanning, review generation, run management, adapters, scoring) depends on reading from a valid `.spine/mission.yaml` and `.spine/constraints.yaml`. Building those features before the bootstrap path would create circular dependencies and make the codebase harder to test.

Phase 1 establishes the contract. Phase 2 reads it.

## Running Phase 1

```bash
uv sync
uv run spine init
uv run pytest
```
