# SPINE

**Local-first, repo-native mission governor for AI-native builders.**

SPINE runs as a CLI tool inside any git repository and uses a `.spine/` directory as the canonical source of truth for governance state — version-controlled alongside your code. No daemons, no network, no model inference required.

## What is SPINE?

SPINE helps a solo developer or small team maintain clarity about:
- What the current mission is (and isn't)
- What scope is allowed vs. forbidden
- What evidence has been collected
- What decisions have been made and why
- Whether the project is drifting from its stated scope

All state lives in plain YAML and JSONL files in `.spine/`. Human-readable, diffable, git-native.

## Quickstart

```bash
# Install (requires uv)
cd /your/project
git init  # SPINE requires a git repo
uv run spine init

# Set your mission
uv run spine mission set --title "My Project" --status active \
  --scope "backend,api" --forbid "ui,billing"

# Generate a mission brief for Claude
uv run spine brief --target claude

# Check repo health
uv run spine doctor
```

## Current Alpha Capabilities

| Command | What it does |
|---------|-------------|
| `spine init` | Scaffold `.spine/` governance state in a git repo |
| `spine mission show` | Display current mission (table or `--json`) |
| `spine mission set` | Update mission fields |
| `spine opportunity score` | Score an opportunity with a weighted 6-factor rubric |
| `spine evidence add` | Log evidence (commits, PRs, test passes, demos, etc.) |
| `spine decision add` | Log a decision record with rationale |
| `spine drift scan` | Detect scope drift using git-native diff |
| `spine brief --target claude\|codex` | Generate a mission brief for a specific AI agent |
| `spine review weekly` | Generate a weekly review document |
| `spine doctor` | Validate `.spine/` state and repo contract |
| `spine mcp serve` | Start a local MCP server (blocking stdio mode) |

`--json` output is available on `mission show`, `doctor`, and `review weekly`.

## What `spine init` creates

```
.spine/
├── mission.yaml        ← Active mission definition
├── constraints.yaml    ← Work schedule, budget, routing rules
├── opportunities.jsonl ← Candidate opportunities log
├── not_now.jsonl       ← Deferred ideas
├── evidence.jsonl      ← Evidence log
├── decisions.jsonl     ← Decision record
├── drift.jsonl         ← Drift detection log
├── runs.jsonl          ← Agent run log
├── state.db            ← Placeholder (future use)
├── reviews/            ← Generated review documents
├── briefs/             ← Mission briefs
├── skills/             ← Agent skill definitions
└── checks/             ← Automated check scripts
AGENTS.md               ← Guidance for AI agents in this repo
CLAUDE.md               ← Claude-specific rules
```

## Governing an External Repo

To run SPINE against a repo other than your current working directory:

```bash
# One-time init
uv run spine init --cwd /path/to/other-repo

# All subsequent commands via env var
SPINE_ROOT=/path/to/other-repo uv run spine doctor
SPINE_ROOT=/path/to/other-repo uv run spine mission show
```

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 2 | Not in a git repo (use `--allow-no-git` to override) |
| 3 | Conflicting existing files (use `--force` to overwrite) |

## Validation Summary

This alpha release was validated against two repos:

- **Self-governance:** Full governance loop run on SPINE's own repo — mission set, evidence logged, drift scanned, weekly review generated, briefs produced. Test suite: **122 passed, 1 skipped** (Windows SIGINT — not a real failure).
- **External repo (gsn-connector):** `SPINE_ROOT` targeting verified end-to-end. All commands bound correctly to the external repo; no state pollution of the operator's own `.spine/`.

## Known Limitations

1. `--cwd` only works with `spine init`. All other commands use `SPINE_ROOT` for external targeting.
2. `SPINE_ROOT` is process-global — if it's set in your shell profile, all spine commands are affected.
3. No upgrade/migration path yet — this is the first public alpha.
4. No undo/rollback — JSONL logs are append-only.
5. Single git repo per `.spine/` — cannot govern multiple repos from one state directory.

## What's Next

- `--cwd` support on all commands (not just `spine init`)
- Richer drift detection (semantic, not just git diff)
- Improved review summaries
- Migration tooling for state upgrades

Not planned for this release: dashboard UI, auth, billing, cloud sync, remote MCP, background workers, or multi-user support.

## Alpha Status

This is an **alpha** release. The core command surface is stable and validated, but rough edges remain. Do not use in production without review.

---

*Built with [Claude Code](https://claude.ai/code)*
