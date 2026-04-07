# SPINE Branch Ruleset Baseline

**Date:** 2026-04-07
**Applies to:** `Hashi-Ai-Dev/HASHI.AI-Spine`
**Target branch:** `main`

---

## Goal

Apply a sane solo-developer public-alpha branch baseline that prevents accidental force-pushes and ensures review discipline without blocking the owner/administrator.

---

## Branch Protection Applied (via GitHub Branch Protection API)

| Setting | Value | Rationale |
|---------|-------|-----------|
| **Require pull request reviews** | ✅ 1 approval required | Solo-dev alpha baseline — at least self-review or peer-review |
| **Dismiss stale reviews** | ❌ Off | Stale reviews don't apply at solo-dev scale |
| **Require code owner review** | ❌ Off | Overkill for solo/alpha |
| **Require status checks** | ✅ Strict (require branch up-to-date) | No CI defined yet — `strict: true` means branch must be up-to-date before merge |
| **Status checks (contexts)** | None | No CI pipelines yet in alpha |
| **Allow force pushes** | ❌ Blocked | Prevent accidental history rewrites |
| **Allow branch deletions** | ❌ Blocked | Prevent accidental branch deletion |
| **Block creation** | ❌ Off | Admins can still create branches |
| **Enforce on admins** | ❌ Off | Owner/admins operate without restrictions |

---

## Ruleset Summary

```
main branch protection:
  ✅ Require PR before merge
  ✅ 1 approving review
  ✅ Block force pushes
  ✅ Block branch deletions
  ✅ Require branch up-to-date (strict status check)
  ✅ Admin/bypass: NO (no force-push bypass for anyone)
```

---

## Future Considerations

When the project grows:

1. **Add CI checks** (e.g., `lint`, `test`, `type-check`) → add to `required_status_checks.contexts`
2. **Enable `require_code_owner_reviews`** if Phase 3 spec review process is formalized
3. **Consider GitHub Ruleset** (repo-level or org-level) for more granular control (byte-size rulesets, path-based rules, etc.)
4. **Org-level ruleset** to enforce `main` protection across all repos in `Hashi-Ai-Dev`

---

## Verification

Branch protection can be verified at:
```
https://github.com/Hashi-Ai-Dev/HASHI.AI-Spine/settings/branches
```

Or via API:
```bash
curl -H "Authorization: token $TOKEN" \
  https://api.github.com/repos/Hashi-Ai-Dev/HASHI.AI-Spine/branches/main/protection
```
