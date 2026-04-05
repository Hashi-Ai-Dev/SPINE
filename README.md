# SPINE

**Local-first, repo-native mission governor for AI-native builders.**

SPINE governs repositories through a `.spine/` contract directory that captures your active mission, constraints, evidence, decisions, and run history as plain YAML and JSONL files — version-controlled alongside your code.

## Phase 1

Phase 1 implements only `spine init`: bootstrapping the `.spine/` contract in any git repository. No daemons, no network, no model inference.

## Setup

```bash
# Install dependencies
uv sync

# Bootstrap .spine/ in this repo
uv run spine init

# Run tests
uv run pytest
```

## What `spine init` creates

```
.spine/
├── mission.yaml        ← Active mission definition
├── constraints.yaml    ← Work schedule, budget, routing rules
├── opportunities.jsonl ← Candidate opportunities log
├── not_now.jsonl       ← Deferred ideas
├── evidence.jsonl      ← Evidence for weekly review
├── decisions.jsonl     ← Decision record
├── drift.jsonl         ← Drift detection log
├── runs.jsonl          ← Agent run log
├── state.db            ← Future projection target (placeholder)
├── reviews/            ← Generated review documents
├── briefs/             ← Mission briefs
├── skills/             ← Agent skill definitions
└── checks/             ← Automated check scripts
AGENTS.md               ← Guidance for all AI agents
CLAUDE.md               ← Claude-specific rules
.claude/settings.json   ← Claude Code permissions
.codex/config.toml      ← Codex sandbox config
```

## CLI

```
spine --help
spine init [--force] [--allow-no-git]
```

## Exit codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 2 | Not in a git repo (use `--allow-no-git` to override) |
| 3 | Conflicting existing files (use `--force` to overwrite) |
