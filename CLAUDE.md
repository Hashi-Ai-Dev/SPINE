# CLAUDE.md — SPINE Phase 1

## Scope constraint

This is **Phase 1 only**. The only implemented command is `spine init`.

## Rules

- Preserve `.spine/` as the canonical source of truth for governance state.
- Do not silently expand scope beyond what is defined in `.spine/mission.yaml`.
- Do not add new CLI commands (`spine run`, `spine status`, `spine review`, etc.).
- Do not add web UI, authentication, billing, or cloud sync.
- Do not write to `.spine/state.db` as SQLite in Phase 1.
- Run `uv run pytest` before finishing any change session. Fix all failures.

## Quick reference

```bash
uv sync              # install dependencies
uv run spine init    # bootstrap .spine/ governance state
uv run pytest        # run tests
```
