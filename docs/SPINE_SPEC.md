# SPINE Specification — Post-Beta Canonical

> **Version:** v0.2.0
> **Status:** Current canonical spec
> **Supersedes:** [`docs/SPINE_OFFICIAL_SPEC_v0.1.md`](SPINE_OFFICIAL_SPEC_v0.1.md) (v0.1 foundation — historical archive)
> **See also:** [`docs/SPINE_PHASE3A_v0.2_SPEC.md`](SPINE_PHASE3A_v0.2_SPEC.md) (Phase 3A planning — complete/historical)

---

## What SPINE Is

SPINE (Strategic Proof & Intelligent Navigation Engine) is a **repo-native mission governor** for AI coding agents. It is the governance layer above coding agents — not another coding agent itself.

SPINE exists to turn repo chaos, project sprawl, and agent drift into: one active mission, one bounded execution lane, one proof ledger, one review loop, and one anti-drift governance layer.

All state is local. All state is in the repo. No daemon, no cloud, no external service dependency at runtime.

---

## Non-Goals

These are permanent non-goals for v0.x, not deferred features:

- No web UI or dashboard
- No authentication or billing
- No cloud sync or remote daemon
- No background workers or autonomous long-running orchestration
- No required external APIs or live model dependency at runtime
- No multi-user collaboration

---

## Core Design Rules

1. **Repo first, UI second.** All state lives in the repo under `.spine/`.
2. **One active mission by default.** SPINE enforces bounded execution lanes.
3. **Canonical state lives in files under `.spine/`** — never in memory or external stores.
4. **JSONL + YAML are the only source of truth.**
5. **SQLite is a rebuildable projection only.** Never a dual-write source.
6. **Deterministic heuristics first; model integration later.**
7. **Git-native evidence and git-native drift logic where possible.**
8. **No speculative architecture unless tiny and inert.**
9. **Agents consume SPINE; SPINE does not depend on agent memory.**
10. **Public CLI contract matters more than internal implementation excuses.**

---

## Command Surface

Full stable command surface as of v0.2.0:

| Command | Purpose |
|---------|---------|
| `spine init` | Bootstrap `.spine/`, `AGENTS.md`, `CLAUDE.md`, `.claude/settings.json`, `.codex/config.toml` in target repo |
| `spine doctor [--json]` | Validate required files exist, YAML/JSONL parse cleanly, projection rebuild works |
| `spine mission show [--json]` | Read and validate `mission.yaml`; display title, status, target, scope, forbidden expansions |
| `spine mission set` | Update `mission.yaml` with validation; refresh `updated_at`; reject invalid transitions |
| `spine brief --target <claude\|codex>` | Generate markdown brief under `.spine/briefs/<target>/` including `latest.md` alias |
| `spine opportunity score` | Deterministic weighted scoring; append JSONL to `opportunities.jsonl` |
| `spine evidence add` | Append validated evidence record to `evidence.jsonl` |
| `spine evidence list` | Print recent evidence records from `evidence.jsonl` |
| `spine decision add` | Append validated decision record to `decisions.jsonl` |
| `spine decision list` | Print recent decision records from `decisions.jsonl` |
| `spine drift scan [--json]` | Git-native deterministic drift scanning; append to `drift.jsonl`; print severity summary |
| `spine check before-work [--json]` | Preflight check before starting work (advisory; non-zero exit is advisory only) |
| `spine check before-pr [--json]` | Preflight check before opening a PR (blocks with exit 1 on high-severity drift) |
| `spine review weekly [--json]` | Aggregate recent evidence/decisions/drift/mission; write markdown under `.spine/reviews/` |
| `spine hooks install` | Install SPINE git hooks (e.g. pre-push preflight) into a governed repo |
| `spine hooks list` | List installed SPINE hooks |
| `spine hooks uninstall` | Remove installed SPINE hooks |
| `spine mcp serve` | Blocking stdio MCP server exposing resources and tools |
| `spine drafts list` | List pending draft governance records **[beta]** |
| `spine drafts confirm <id>` | Promote a draft record to canonical state **[beta]** |

All commands support `--cwd <path>` to target any repo. Target resolution precedence: `--cwd` > `SPINE_ROOT` > current working directory.

### Exit code contract

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | Validation failure (e.g. `check before-pr` blocked by drift) |
| 2 | Context failure (missing repo, missing `.spine/`) |

### JSON output surfaces

Machine-readable output (`--json`) is stable and validated on:

```
spine doctor --json
spine mission show --json
spine drift scan --json
spine check before-work --json
spine check before-pr --json
spine review weekly --json
```

---

## Canonical State Rules

Canonical state lives in `.spine/`:

- `.spine/mission.yaml` — active mission definition
- `.spine/constraints.yaml` — operational constraints
- `.spine/*.jsonl` — append-only event logs (evidence, decisions, drift, opportunities, runs)

`.spine/state.db` is optional and projection-only. Allowed uses: rebuild at command start, rebuild at `spine doctor`, rebuild at `spine mcp serve` startup, skip entirely if not needed.

Forbidden:
- Dual-write canonical files and SQLite
- Reconciliation engine
- Background sync service
- Incremental sync complexity

---

## Repo Contract

`spine init` writes these to the governed repo:

```
AGENTS.md                      ← agent guidance (any agent that reads the repo)
CLAUDE.md                      ← Claude Code-specific governance rules
.claude/settings.json          ← Claude Code settings
.codex/config.toml             ← Codex configuration
.spine/
  mission.yaml
  constraints.yaml
  opportunities.jsonl
  not_now.jsonl
  evidence.jsonl
  decisions.jsonl
  drift.jsonl
  runs.jsonl
  reviews/                     ← generated weekly reviews (ephemeral, gitignored)
  briefs/
    claude/                    ← Claude-targeted briefs (ephemeral, gitignored)
    codex/                     ← Codex-targeted briefs (ephemeral, gitignored)
  skills/
  checks/
```

Durable governance data (decisions, evidence, drift, opportunities) is committed to git. Generated outputs (briefs, reviews) are ephemeral and gitignored.

---

## Drift Detection Rules

Drift is detected by scanning git diff output across two modes:

- **Working tree:** `git diff HEAD` — catches uncommitted/staged forbidden changes
- **Branch drift:** `git diff <default_branch>...HEAD` — catches forbidden changes committed on the current branch

Patterns that trigger drift flags:

- New directories or files matching forbidden scope (e.g. `/ui/`, `/dashboard/`, `/auth/`, `/billing/`) — **HIGH** severity
- Dependencies added to `pyproject.toml` or `package.json` that imply forbidden capabilities — **LOW** severity
- Service files added without corresponding test files — **LOW** severity

Severity levels: **HIGH** = forbidden scope match; **MEDIUM** = likely sprawl; **LOW** = worth noting.

Default branch detection: `git symbolic-ref refs/remotes/origin/HEAD` → `main` → `master`. `--against <branch>` overrides.

Untracked files are not flagged — changes must be staged or committed to be detected.

---

## Agent Compatibility

| Agent runtime | Status | How it integrates |
|---|---|---|
| **Claude Code** | **First-class** | `spine init` writes `CLAUDE.md` + `.claude/settings.json`; `brief --target claude` writes `.spine/briefs/claude/latest.md`; load with `@.spine/briefs/claude/latest.md` |
| **Codex** | **First-class** | `spine init` writes `AGENTS.md` + `.codex/config.toml`; `brief --target codex` writes a codex-native brief |
| **oh-my-claudecode** | **Compatible** | Works through Claude Code file contracts (`CLAUDE.md`, `.claude/`, briefs); no runtime coupling required |
| **Superpowers** | **Compatible** | Same file-based compatibility as oh-my-claudecode; SPINE sits above the session layer |
| **OpenClaw** | **Compatible (not yet first-class)** | Repo-native contracts (`AGENTS.md`, `.spine/`, JSON surfaces) are runtime-agnostic and work for any file-reading agent; no OpenClaw-specific init file generated; first-class integration is a Phase 3B follow-up |

Integration rule: SPINE connects to the execution layer through `.spine/briefs/`, `CLAUDE.md`, `AGENTS.md`, and `--json` outputs. No runtime coupling required.

---

## MCP Process Model

`spine mcp serve` is a stdio-only MCP server:

- Runs as a separate blocking process
- Does not daemonize
- Exposes typed resources and tools via MCP protocol
- Reads canonical state from `.spine/` files on each request
- Never writes to canonical state directly (all writes go through CLI commands)

Resources exposed: active mission, current constraints, recent evidence, recent decisions, open drift, latest review.

Tools exposed: `mission_get`, `mission_update`, `brief_generate`, `evidence_add`, `decision_add`, `drift_scan`, `review_generate`, `opportunity_score`.

---

*This is the canonical SPINE specification for v0.2.0 and beyond. For v0.1 historical context, see [`SPINE_OFFICIAL_SPEC_v0.1.md`](SPINE_OFFICIAL_SPEC_v0.1.md). For Phase 3A planning history, see [`SPINE_PHASE3A_v0.2_SPEC.md`](SPINE_PHASE3A_v0.2_SPEC.md).*
