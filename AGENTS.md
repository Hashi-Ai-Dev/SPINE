# SPINE Agent Guidance

This repository uses `.spine/` as canonical governance state.

## Rules for all agents

- Read `.spine/mission.yaml` before making non-trivial changes.
- Read `.spine/constraints.yaml` to understand work schedule and budget limits.
- Never silently expand scope beyond `allowed_scope` in `mission.yaml`.
- Never add UI, auth, billing, cloud sync, or autonomous background loops unless
  they appear explicitly in `allowed_scope`.
- Do not create new `spine` subcommands — Phase 1 implements only `spine init`.
- After any change session: run `uv run pytest` and fix all failures before finishing.

## Phase 1 scope

Only `spine init` is implemented. Do not add `spine run`, `spine review`,
`spine status`, or any other command yet.

## Running tests

```
uv run pytest
```

## Governance files

| File | Purpose |
|------|---------|
| `.spine/mission.yaml` | Active mission definition |
| `.spine/constraints.yaml` | Work schedule, budget, routing rules |
| `.spine/opportunities.jsonl` | Candidate opportunities log |
| `.spine/evidence.jsonl` | Evidence collected for review |
| `.spine/decisions.jsonl` | Decision record |
| `.spine/runs.jsonl` | Agent run log |
