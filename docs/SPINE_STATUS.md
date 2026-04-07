# SPINE Status

**Last updated:** 2026-04-07
**Repo:** `Hashi-Ai-Dev/HASHI.AI-Spine`
**Agent:** SPINE Repo Manager

---

## Current Release

| | |
|---|---|
| **Version** | `v0.1.1-alpha` |
| **Published** | 2026-04-07 |
| **Tag** | `v0.1.1-alpha` at commit `3f2b3ef` |
| **Type** | Public alpha (prerelease) |
| **Next target** | `v0.1.2` |

---

## Current Phase

**Phase 2 Complete.** Full governance command suite implemented:
- `spine init` — mission bootstrapping
- `spine brief` — current mission display
- `spine doctor` — environment validation
- `spine mission` — goal check
- `spine proof` — artifact manifest
- `spine decision` — decision logger
- `spine drift` — deviation detection

Phase 1 + 2 = stable core. No known critical bugs. Alpha smoke test: 120+ tests passing.

---

## Current Milestone

**`v0.1.2 — Stabilization** (planned, not started)

Top items:
1. Enable Dependabot alerts + secret scanning push protection (human: GitHub settings page)
2. Add `--cwd` to Phase 2 commands
3. Add minimal CI pipeline
4. Create org-level ruleset for `Hashi-Ai-Dev`
5. Clarify onboarding docs

---

## Current Blockers

| Blocker | Severity | Resolution |
|---------|----------|------------|
| GitHub secret scanning / Dependabot not enabled | High | Human visit: `github.com/Hashi-Ai-Dev/HASHI.AI-Spine/settings/security_and_analysis` |
| GitHub org ruleset not created | Medium | Human or token: create org-level ruleset |

---

## Next 3 Moves

1. **Add `--cwd` support to Phase 2 commands** — small scoped fix, unblocks external-repo usage
2. **Write CI pipeline** — `ci.yml` with lint + test on push/PR; enables status checks
3. **Update README quickstart** — clarify external-repo path; reduce onboarding friction

*(After those: tag v0.1.2, publish release)*

---

## Branch / Release State

| | |
|---|---|
| **Default branch** | `main` (protected) |
| **Branch protection** | PR required + force-push blocked + delete blocked |
| **Open PRs** | None |
| **Open branches** | `main` only |
| **Releases** | `v0.1.1-alpha` (published) |

---

## Phase 3A Planning Status

**Phase 3A spec** (`docs/SPINE_PHASE3A_v0.2_SPEC.md`) was referenced in prior audits but has not yet been committed to the repo. Planning should be completed and approved before v0.2 work begins.

**Do not begin Phase 3A implementation without approved spec.**

---

## Repo Health

| Check | Status |
|-------|--------|
| README | ✅ Public-alpha appropriate |
| LICENSE | ✅ MIT |
| SECURITY.md | ✅ Contact + policy |
| Branch protection | ✅ `main` protected |
| Org ruleset | ❌ Not created |
| CI pipeline | ❌ Not created |
| Dependabot alerts | ⚠️ Human action required |
| Secret scanning | ⚠️ Human action required |

---

*Next status review: when v0.1.2 is ready for release*
