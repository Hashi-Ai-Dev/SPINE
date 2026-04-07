# SPINE Branch Cleanup Report

**Generated:** 2026-04-07
**Context:** Pre-alpha-release branch audit for `prep/v0.1.1-alpha`

---

## Summary

7 branches classified. Do NOT delete remote branches automatically. All remote deletions
require explicit human action.

---

## Branch Classification

| Branch | Status | Recommendation | Reason |
|--------|--------|----------------|--------|
| `main` | Active, default target | **Keep** | Default/target branch. All PRs merge here. |
| `prep/v0.1.1-alpha` | Active, alpha release prep | **Keep** | The branch under review. Contains README cleanup, SPINE evidence/decisions for this cleanup pass, and the branch cleanup report. Should be merged to `main` after human review. |
| `claude/alpha-release-prep-DU2Ul` | Stale automation branch | **Likely safe to delete later** | Was the working branch for this cleanup session's initial state. Changes were moved to `prep/v0.1.1-alpha`. Contains no unique work not present in `prep/v0.1.1-alpha`. |
| `claude/dogfood-phase3a-polish-zHDuu` | Stale | **Likely safe to delete later** | Dogfood polish pass branch. Work was folded into the main alpha branch. No active PRs observed. |
| `claude/dogfood-phase3a-artifact-hygiene` | Stale | **Likely safe to delete later** | Artifact hygiene pass. Work completed and integrated. |
| `claude/dogfood-phase3a-json-automation` | Stale | **Likely safe to delete later** | JSON automation work. Integrated into `prep/v0.1.1-alpha`. |
| `claude/spine-phase-1-init-hOwIP` | Stale, historical | **Uncertain — leave alone** | Original Phase 1 `spine init` implementation branch. Could be useful for historical reference. Low risk either way, but leave for human decision. |
| `codex/draft-official-phase-3a-spec-for-spine` | Stale spec branch | **Uncertain — leave alone** | Codex-generated spec draft. Not integrated into alpha. May be referenced for future planning. Leave for human decision. |

---

## Recommended Human Actions

### Safe to delete (remote, when ready):
```bash
git push origin --delete claude/alpha-release-prep-DU2Ul
git push origin --delete claude/dogfood-phase3a-polish-zHDuu
git push origin --delete claude/dogfood-phase3a-artifact-hygiene
git push origin --delete claude/dogfood-phase3a-json-automation
```

### Leave alone until human review:
- `claude/spine-phase-1-init-hOwIP` — historical reference value
- `codex/draft-official-phase-3a-spec-for-spine` — may feed future planning

### Must keep:
- `main`
- `prep/v0.1.1-alpha` (until merged)

---

## Notes

- Only 2 remote branches were visible from this environment at analysis time:
  `origin/claude/alpha-release-prep-DU2Ul` and `origin/prep/v0.1.1-alpha`.
  The other branches listed above (`claude/dogfood-*`, `claude/spine-phase-1-init-hOwIP`,
  `codex/draft-*`) are classified based on the task description and may need to be
  confirmed with `git branch -r` after a fresh `git fetch --all`.
- Do NOT delete any branch without confirming it has no open PRs.
- After merging `prep/v0.1.1-alpha` → `main`, the `prep/v0.1.1-alpha` branch itself
  can be deleted.
