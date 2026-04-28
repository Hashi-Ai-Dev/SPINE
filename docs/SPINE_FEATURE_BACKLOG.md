# SPINE Feature Backlog

Grouped by target milestone. Each item: title, short description, why it matters, status.

---

## v0.1.2 — Stabilization

### ✅ Add `--cwd` support to Phase 2 commands
**Status:** DONE — PR #11

### ✅ Add minimal CI pipeline
**Status:** DONE — PR #12

### ✅ Clarify onboarding / quickstart docs
**Status:** DONE — PR #13

---

## Alpha Exit — v0.2.0-beta (Released 2026-04-07)

### ✅ All Phase 3A items (#15–#18, #23–#25)
**Status:** DONE — PRs #19–#29

---

## Beta — v0.2.0-beta

> ✅ Beta core and polish complete. **Beta exit achieved** (2026-04-09).

### Completed Beta Issues

| # | Issue | PR |
|---|---|
| #31 | `spine check before-pr` preflight checkpoint | PR #35 |
| #32 | Handoff/PR-prep summary primitive | PR #39 |
| #33 | Draftable governance records | PR #40 |
| #34 | Local optional hook/checkpoint integration | PR #41 |
| #36 | Mission refine draft flow | PR #47 |
| #37 | Compatibility/integration guide | PR #48 |
| #38 | Deterministic validation fixtures | PR #52 |
| #43 | `check before-pr` exit 1 on healthy repos | PR #46 |
| #44 | Hook script missing `uv run` | PR #46 |
| #45 | AGENTS.md template invalid commands | PR #46 |
| #49 | Write-flow machine-readable consistency | PR #53 |
| #50 | Before-work / start-session governance checkpoint | PR #54 |
| #57 | MCP TextContent NameError | PR #61 |
| #58 | README exit code + test count | PR #63 |
| #59 | `spine drift scan --json` | PR #67 |
| #64 | `spine evidence list` + `spine decision list` | PR #68 |
| #65 | `check before-pr --json` structured doctor detail | PR #69 |
| #66 | `check before-work` no-brief advisory | PR #70 |
| #60 | SECURITY_BASELINE wrong repo name | commit `9feb2642` |
| #51 | Beta-exit proof/validation | PR #72 |

---

## ✅ Pre-Beta-Exit Blockers — All Cleared (Milestone #5)

| # | Issue | Status |
|---|---|
| ~~#65~~ | ~~`check before-pr --json` structured doctor detail~~ | ✅ Fixed — PR #69 |
| ~~#66~~ | ~~`check before-work` no-brief advisory not exit 1~~ | ✅ Fixed — PR #70 |
| ~~#60~~ | ~~SECURITY_BASELINE wrong repo name~~ | ✅ Fixed — commit `9feb2642` |
| ~~#51~~ | ~~Beta-exit proof/validation~~ | ✅ Fixed — PR #72 |

Beta exit gate is open. See `docs/SPINE_BETA_EXIT_VALIDATION.md` for the full evidence-backed judgment.

---

## v1.0 — Post-Beta Stabilization (Active — Milestone #6)

> Bug fixes and usability hardening only. No new features until v0.2.0 stabilizes.

| # | Issue | Status |
|---|---|
| #73 | SPINE_ROOT ergonomics for long-running shells / multi-repo use | 🟡 Open — Phase 3B candidate |
| ~~#74~~ | ~~Discipline-tax reduction — `spine log` short-form evidence add~~ | ✅ Fixed — PR #78 |
| ~~#75~~ | ~~OpenClaw first-class startup/skill path~~ | ✅ Fixed — PR #80 |


---

## Phase 3B Candidates

### 🟡 SPINE_ROOT ergonomics (#73)
**Status:** Active — Phase 3B candidate

### 🟡 Discipline-tax reduction (#74)
**Status:** Active — Phase 3B candidate

#
## v1.0.0 — Stable Release

**Stage:** Building

| # | Issue | Status |
### CLAWNAV Real-Usage Feedback (2026-04-15)

| # | Issue | Status |
|---|---|
| #86 | Decision query interface — `spine query` for semantic search | 🟡 Open — v1.0.0 |
| #87 | `spine brief` output doesn't match what agents actually use in practice | 🟡 Open — v1.0.0 |
| #88 | Lightweight shell helper for agents that cannot assume `spine` is in $PATH | 🟡 Open — v1.0.0 |


|---|---|
| #82 | External/sandboxed agent bootstrap path (parent) | 🟡 Open |
| #83 | Explicit `uv run spine` bootstrap path for external agents | 🟡 Open — #82 sub-issue |
| #84 | Clear `--cwd` targeting semantics to prevent init from wrong repo | 🟡 Open — #82 sub-issue |
| #85 | Structured file-mode fallback when CLI unavailable | 🟡 Open — #82 sub-issue |


## v0.2.2 — Truth Sync + Code Hygiene

**Stage:** Planned

| # | Issue | Status |
|---|---|
| #89 | [release] v0.2.2 — Truth Sync + Code Hygiene | 🟡 Open |
| #90 | Fix SPINE_VERSION constant (0.1 → 0.2.1) | 🟡 Open |
| #91 | Fix SPINE_AGENT_SKILL.md — invalid commands, stale spine target | 🟡 Open |
| #92 | Fix README command table — OpenClaw support | 🟡 Open |
| #93 | Fix SPINE_STATUS.md — #75 contradiction | 🟡 Open |
| #94 | Verify DRIFT_SEVERITY import (Luciel claim → unconfirmed) | 🟡 Open |
| #95 | BriefService refactor + DriftService path hygiene | 🟡 Open |

## v0.2.3 — Agent Context Export + Strict Checks

**Stage:** Planned

| # | Issue | Status |
|---|---|
| #96 | [release] v0.2.3 — Agent Context Export + Strict Checks | 🟡 Open |
| #97 | spine context export — injectable context for spawned agents | 🟡 Open |
| #98 | spine check --strict mode — block work when prerequisites unmet | 🟡 Open |
| #99 | SPINE_REPO_MANAGER_RUNBOOK.md | 🟡 Open |

## v0.2.4 — Identity + Mission Ensure + Query

**Stage:** Planned

| # | Issue | Status |
|---|---|
| #100 | [release] v0.2.4 — Identity + Mission Ensure + Query | 🟡 Open |
| #101 | spine identity verify | 🟡 Open |
| #102 | spine mission ensure | 🟡 Open |
| #86 | spine query — semantic search (existing) | 🟡 Open |

## v0.2.5 — OpenClaw Adoption Pack

**Stage:** Planned

| # | Issue | Status |
|---|---|
| #103 | [release] v0.2.5 — OpenClaw Adoption Pack | 🟡 Open |
| #104 | SPINE_OPENCLAW_ADOPTION.md | 🟡 Open |
| #105 | OpenClaw brief improvements | 🟡 Open |
| #88 | Lightweight shell helper (existing) | 🟡 Open |

## v0.3.0 — Drift Lifecycle + Mission-Aware Drift

**Stage:** Planned

| # | Issue | Status |
|---|---|
| #106 | [release] v0.3.0 — Drift Lifecycle + Mission-Aware Drift | 🟡 Open |
| #107 | spine drift resolve + Drift IDs | 🟡 Open |
| #108 | Mission-derived drift patterns | 🟡 Open |

## 🚫 HUD / live observability mode
**Status:** REJECTED

### 🚫 Notification / webhook systems
**Status:** REJECTED

### 🚫 Remote MCP (strategic question — INTERNAL, not yet approved)
**Status:** DEFERRED — Issue #76 — product decision pending

---

*Last updated: 2026-04-28 — v0.2.2-v0.3.0 roadmap issues created. Full release plan approved by Hashi.*
