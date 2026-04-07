# SPINE Post-Launch Stabilization Report

**Date:** 2026-04-07
**Repo:** `Hashi-Ai-Dev/HASHI.AI-Spine`
**Status:** Post-public-alpha launch audit

---

## 1. Current Public Repo State

| Property | Value | Status |
|----------|-------|--------|
| Visibility | **public** | ✅ |
| Default branch | `main` | ✅ |
| Branch protection on `main` | PR required + force-push blocked + delete blocked | ✅ |
| Release `v0.1.1-alpha` | Published (2026-04-07, prerelease) | ✅ |
| Tags | `v0.1.1-alpha` at `3f2b3ef` | ✅ |
| README | Public-alpha appropriate, badges current | ✅ |
| Repo description | **Set** — "Local-first, repo-native mission governor for AI coding agents..." | ✅ |
| Topics | **Set** — ai, automation, cli, developer-tools, governance, open-source, python | ✅ |
| LICENSE | **MIT** — added post-launch | ✅ |
| SECURITY.md | **Added** — has `hashiai.dev@gmail.com` contact | ✅ |

---

## 2. Remaining Gaps

| Gap | Severity | Owner Action |
|-----|----------|--------------|
| `secret_scanning` disabled | **High** — should be enabled for public repo | Human: visit settings page |
| `secret_scanning_push_protection` disabled | **High** | Human: visit settings page |
| `dependabot_alerts` disabled | **Medium** | Human: visit settings page |
| No org-level ruleset | **Medium** — future repos unprotected | Human: create org ruleset |

GitHub API cannot enable secret scanning on a public repo in free tier — the settings page shows it as auto-enabled but the API reports `disabled`. This may resolve automatically or require manual confirmation at:
`https://github.com/Hashi-Ai-Dev/HASHI.AI-Spine/settings/security_and_analysis`

---

## 3. Security / Settings Verification

```json
{
  "secret_scanning": "disabled ⚠️",
  "secret_scanning_push_protection": "disabled ⚠️",
  "dependabot_alerts": "disabled ⚠️ (API cannot enable — human required)",
  "dependabot_security_updates": "disabled"
}
```

**Immediate human action needed:**
Visit `https://github.com/Hashi-Ai-Dev/HASHI.AI-Spine/settings/security_and_analysis` and enable:
- ✅ Secret scanning
- ✅ Secret scanning push protection
- ✅ Dependabot alerts

---

## 4. Ruleset Sanity Judgment

**Current settings on `main`:**
- Required PR reviews: 1 approval
- Block force pushes: ✅
- Block deletions: ✅
- Strict status checks: ✅ (branch up-to-date before merge)

**Solo-dev judgment: ruleset is appropriate as-is.**

Rationale:
- "1 approval" sounds strict but since the owner is the only committer, they approve their own PR — it's a self-review checkpoint, not friction.
- Force-push blocking is essential (alpha has no history rewriting infrastructure).
- The `enforce_admins: false` setting means the owner bypasses in emergencies — correct for solo operation.
- No tightening needed now. Consider adding CI checks in v0.2 for marginally more safety.

**Verdict: Leave ruleset as-is.**

---

## 5. Repo / Org Polish Actions Taken

| Action | Result |
|--------|--------|
| Set repo description | ✅ Added — "Local-first, repo-native mission governor for AI coding agents..." |
| Set repo topics | ✅ Added — 7 topics covering the use case |
| Org profile | ✅ Already sane — "Hashi Ai Dev" with description and location |

No rewrites performed. Narrow polish only.

---

## 6. Branch Recommendations

| Branch | Action | Reason |
|--------|--------|--------|
| `main` | Keep | Default, protected |
| `codex/draft-official-phase-3a-spec-for-spine` | **Merged + Deleted** | Phase 3A planning spec added real value — `docs/SPINE_PHASE3A_v0.2_SPEC.md` now on `main`. Branch deleted post-merge. |

**Post-cleanup branch list:** `main` only.

---

## 7. Top 5 Follow-Up Issues for v0.1.2

1. **Enable secret scanning + push protection** — must be on for public repo security
2. **Enable Dependabot alerts** — dependency vulnerability monitoring
3. **Create org-level ruleset** — enforce `main` protection across all `Hashi-Ai-Dev` repos
4. **Add `--cwd` support to Phase 2 commands** — only `spine init` accepts it currently; blocks external repo workflows
5. **Add a CI pipeline** (even minimal: lint + test on push) — enables status checks on PRs and removes the "always-passing" status check gap

---

## 8. What Waits for v0.2 / Phase 3A

The following are **explicitly out of scope** for v0.1.x and should not be started until Phase 3A planning is approved:

- Any CLI command surface expansion beyond Phase 2 (brief, doctor, mission, drift, etc.)
- Remote MCP server or any networking layer
- Multi-user or collaboration features
- Web UI / dashboard
- Auth, billing, or cloud sync
- Phase 3 implementation (architecture refactors, agentic loops, etc.)
- Any product feature work not already in the v0.1 spec

---

## 9. What Should NOT Be Touched

The `docs/SPINE_PHASE3A_v0.2_SPEC.md` is a **planning reference only**. It does not authorize implementation. Any Phase 3A work must go through proper scoping before touching production code.

---

*End of stabilization report.*
