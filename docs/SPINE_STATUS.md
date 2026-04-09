# SPINE Status

**Last updated:** 2026-04-09 (Issue #60 — SECURITY_BASELINE wrong repo name fixed on main, pre-beta-exit blockers cleared)
**Repo:** `Hashi-Ai-Dev/SPINE`

---

## Current Release

| | |
|---|---|
| **Version** | `v0.2.0-beta` |
| **Status** | Published (2026-04-07) — pre-release |
| **Target** | Beta |

---

## Phase Map

| Phase | Status |
|---|---|
| Phase 1 + 2 | ✅ Complete |
| Alpha Exit → v0.2.0-beta | ✅ Released (2026-04-07) |
| Beta blocker stabilization | ✅ Complete — PR #46 |
| Beta core feature queue | ✅ Complete |
| Beta polish queue | ✅ Complete |
| **Pre-Beta-Exit blockers** | ✅ All cleared |

---

## ✅ Beta Exit Blockers Cleared

All pre-beta-exit blockers are resolved. Beta exit is now unblocked pending #51 proof/validation.

### Pre-Beta-Exit Queue (Milestone #5) — All Fixed

| Priority | # | Issue | Status |
|---|---|---|---|
| 1 | ~~#66~~ | ~~`check before-work` no-brief advisory~~ | ✅ Fixed — PR #70 |
| 2 | ~~#60~~ | ~~SECURITY_BASELINE wrong repo name~~ | ✅ Fixed — commit `9feb2642` |

### Fixed

| # | Issue | Status |
|---|---|
| ~~#57~~ | ~~MCP TextContent NameError~~ | ✅ Fixed — PR #61 |
| ~~#58~~ | ~~README exit code + test count~~ | ✅ Fixed — PR #63 |
| ~~#59~~ | ~~`spine drift scan --json` missing~~ | ✅ Fixed — PR #67 |
| ~~#64~~ | ~~`spine evidence list` + `spine decision list`~~ | ✅ Fixed — PR #68 |
| ~~#65~~ | ~~`check before-pr --json` structured doctor detail~~ | ✅ Fixed — PR #69 |
| ~~#66~~ | ~~`check before-work` no-brief advisory~~ | ✅ Fixed — PR #70 |
| ~~#60~~ | ~~SECURITY_BASELINE wrong repo name~~ | ✅ Fixed — commit `9feb2642` |

---

## Current Milestone

**`Beta`** — v0.2.0-beta

### Beta Complete

| # | Issue | PR |
|---|---|---|
| #31–#50 | All Beta core + polish issues | PRs #35–#54 |
| #57 | MCP TextContent NameError | PR #61 |
| #58 | README exit codes + test count | PR #63 |
| #59 | `spine drift scan --json` | PR #67 |
| #64 | `spine evidence list` + `spine decision list` | PR #68 |
| #65 | `check before-pr --json` structured | PR #69 |
| #66 | `check before-work` no-brief advisory | PR #70 |
| #60 | SECURITY_BASELINE wrong repo name | commit `9feb2642` |

### Beta Polish Queue

| # | Issue | Status |
|---|---|---|
| #51 | Beta-exit proof/validation | 📋 Last — unblocked now that pre-beta-exit issues cleared |

---

## Next Active Priority

**Issue #51** — Beta-exit proof/validation. All pre-beta-exit blockers cleared. This is the final step before beta exit.

---

## What SPINE Is

SPINE is a **repo-native mission governor** for AI coding agents. It sits above the agent and keeps it aligned to a defined mission — not by being smart, but by being explicit.

**Core loop:** Mission → Scope → Proof → Decisions → Drift Check

**Discipline rule:** SPINE should reduce discipline tax not by hiding governance, but by making governance easy for agents and tools to execute explicitly.

**Authority rule:** Agents may execute governance mechanics. Operators retain governance authority.

---

## Links

- Repo: https://github.com/Hashi-Ai-Dev/SPINE
- Releases: https://github.com/Hashi-Ai-Dev/SPINE/releases
- Spec: `docs/SPINE_PHASE3A_v0.2_SPEC.md`
- Tracking policy: `docs/SPINE_TRACKING_POLICY.md`
- Agent skill: `docs/SPINE_AGENT_SKILL.md`

---

*Updated by: SPINE Repo Manager Agent*
