# SPINE Tracking Policy

> **Purpose:** Define what goes where — so SPINE's project memory is always findable and never contradictory.

---

## Document Hierarchy

```
README.md               ← public front door. What SPINE is, install, quickstart.
SPEC files              ← detailed product/technical specifications
docs/SPINE_ROADMAP.md   ← current phase, milestones, what's next, what's out of scope
docs/SPINE_FEATURE_BACKLOG.md ← all known features/issues grouped by target release
docs/SPINE_STATUS.md    ← current version, phase, blockers, next 3 moves
docs/SPINE_TRACKING_POLICY.md ← this file
```

---

## What Goes in README.md

- One-line description
- Installation / install commands
- Quickstart (3-5 commands)
- Badges (version, license, status)
- Link to full docs

**Not in README:** planning details, backlog, internal decisions, long explanations.

---

## What Goes in Spec Docs (e.g., `docs/SPINE_PHASE3A_v0.2_SPEC.md`)

- Detailed product design for a specific feature or phase
- Architecture decisions with rationale
- Command surface design
- State management approach
- Acceptance criteria

Spec docs are **planning references**. They do not authorize implementation. Implementation requires a separate review + approval step.

---

## What Goes in SPINE_ROADMAP.md

- What SPINE is overall (2-3 sentences)
- Current project stage
- Current phase + milestone
- Next major phases + milestone structure
- What is explicitly out of scope
- Strategic positioning note

**Not in roadmap:** detailed feature lists (those go in the backlog).

---

## What Goes in SPINE_FEATURE_BACKLOG.md

- All known feature requests, fixes, and improvements
- Grouped by target release (v0.1.2, v0.2, later, rejected)
- Each item: title + description + why it matters + status

**Not in backlog:** spec-level detail. If an item needs a full spec, create a separate doc and link to it.

---

## What Goes in SPINE_STATUS.md

- Current version / release
- Current phase
- Current milestone
- Active blockers (with resolution owner)
- Next 3 moves only
- Branch / release state

**Not in status:** history, long explanations, spec details.

---

## What Becomes a GitHub Issue

A GitHub issue is created when:

- A backlog item is **ready to be worked** (not just planned)
- A bug is **confirmed** (not suspected)
- A decision needs **external input or review**
- Something requires **discussion with a specific person** or team

GitHub issues are **unit of work** — not thought-dumping ground.

**Size rule:** Each issue should be completable in one focused session. If an issue would take a week of work, break it up.

**Issue states:**
- `open` — not started, not blocked
- `in progress` — being actively worked
- `closed` — done or rejected

---

## What Becomes a Milestone

A milestone is created when:

- A set of issues represents a **releaseable unit**
- There is a **clear target version** (e.g., `v0.1.2`)
- The milestone has a **realistic scope** for a solo builder

Milestones are **release containers**. Keep them small and achievable.

**Milestone naming:** Use semver tags (`v0.1.2`, `v0.2`) so they map directly to git tags and releases.

---

## What the Repo Manager Agent Owns

The SPINE Repo Manager Agent owns:

- README and public-surface docs (keeping them accurate)
- SPINE_ROADMAP.md (updating when phase/milestone changes)
- SPINE_STATUS.md (updating on each significant event)
- SPINE_FEATURE_BACKLOG.md (adding items, updating status)
- GitHub issues (creating, updating, closing)
- GitHub milestones (creating, assigning, closing)
- Branch hygiene (cleaning stale branches, protecting main)
- Release prep (git tags, GitHub releases, prerelease flags)
- CI pipeline (adding and maintaining)
- Org rulesets (creating and updating)

---

## What Requires Human / Product Judgment

These require explicit human decision — the Repo Manager does not decide unilaterally:

- **New features** beyond the current phase scope
- **Architectural changes** to SPINE's core design
- **Phase transitions** (e.g., moving from Phase 2 to Phase 3A)
- **Scope changes** (adding things explicitly marked as out of scope)
- **Strategic direction** (market positioning, partnership, monetization)
- **Rejecting** an item from the backlog permanently
- **Releasing** a new version (Repo Manager prepares, human approves)

The Repo Manager can **recommend** in all of the above. The human **decides**.

---

## Rule Summary

| Type | Repo Manager | Human Decision |
|------|-------------|----------------|
| Doc maintenance | ✅ Owns | — |
| Bug fix | ✅ Can create issue + fix | Reviews PR |
| New feature (in-scope) | ✅ Can create issue | Approves before impl |
| New feature (out-of-scope) | ❌ | ✅ Explicit approval |
| Phase transition | Recommends | ✅ Approves |
| Milestone/release | Prepares | ✅ Approves |
| Org rulesets / CI | ✅ Owns | — |

---

*This policy is owned by the SPINE Repo Manager Agent and updated as project structure evolves.*
*Last updated: 2026-04-07*
