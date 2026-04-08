# SPINE Product Notes

> External product insights preserved for future planning. Not active work. Not all are in-scope now.
> Source: human review session 2026-04-07.

---

## Core Thesis

> **SPINE should reduce discipline tax not by hiding governance, but by making governance easy for agents and tools to execute explicitly.**

**Operational rule:**
> **Agents may execute governance mechanics. Operators retain governance authority.**

---

## Strong Fits

These align with SPINE's identity as a repo-native mission governor above coding agents. Preserve for Phase 3B / beta planning.

### 1. Agent-Executable Governance
SPINE should reduce discipline tax by making governance easier for agents and tools to execute explicitly. Stable command contracts, machine-readable outputs, draftable records. Humans retain authority over mission, scope changes, pivots, and canonical repo truth.

### 2. Draftable Governance Records
Draft evidence. Draft decisions. Draft PR/handoff summaries. Governance records that are explicitly tentative until the operator confirms them as canonical. Reduces friction without mutating truth silently.

### 3. Native Hooks / Lifecycle Enforcement
Local, explicit, opt-in hook flows — pre-commit, pre-PR checks. Not hidden daemon behavior. Makes SPINE governance naturally part of the existing developer workflow without adding a daemon layer.

### 4. Stronger Local Tool-Consumption Surfaces
Stable command contracts, machine-readable outputs, stable artifact references. Richer local MCP surfaces later. All local. All explicit. Consistent with SPINE's identity.

---

## Good — But Constrained

These are good directions but need to stay constrained. No drift toward dashboard, orchestration, or cloud.

### 5. Mission Interview / Brainstorm Flow
Explicit operator-invoked mission refinement. Draft mission generation only. Must not silently mutate canonical mission truth. Operator always controls what becomes canonical.

### 6. Optional Worktree Helpers
Explicit, optional, and later. Not core product identity. No orchestration creep. SPINE governs the agent, not the agent system.

### 7. Optional Governance Profiles
Explicit opt-in workflow profiles. Visible rules, not hidden methodology enforcement. Could be useful for team-specific governance styles — but only if entirely operator-controlled.

---

## Defer / Not Now

These are weak fits or premature. Do not prioritize.

### 8. HUD / Live Observability Mode
Too easy to drift toward dashboard creep. SPINE is a governance layer, not a monitoring tool. The value is in governance, not observability. Defer indefinitely unless a specific, constrained use case emerges.

### 9. Notification / Webhook Systems
Not core right now. Only consider much later, and only if explicit/local/optional. A governance tool that pings you about things is no longer purely local.

---



## Operator Model

SPINE is designed for an operator who is:
- high-agency and autonomous
- nonlinear in how they work
- context-switch-prone
- vulnerable to branch explosion and agent-generated chaos
- especially impacted by ambiguity in governance state

This means SPINE should never assume the operator is naturally linear, ceremony-tolerant, or consistent at remembering governance steps manually. Governance must fit around how operators actually work — not the other way around.

**Implications for product direction:**
- Explicit checkpoints reduce the mental load of remembering what to verify
- Draft-first governance means provisional work doesn't require cleanup until ready
- Handoff summaries reduce context-switch cost when returning to a project
- Local opt-in hooks make governance available without being obtrusive
- Strong queue clarity and anti-drift structure compensate for nonlinear workflow

## Anti-Drift Rules

These insights were classified against SPINE's core identity:

**What SPINE is NOT:**
- A dashboard or observability tool
- A monitoring or alerting system
- A daemon or background service
- A cloud service or SaaS layer
- An orchestration platform
- A swarm coordination system

**What SPINE IS:**
- Repo-native, local-first
- Above the coding agent — governs, doesn't code
- Governance primitives: mission, scope, proof, decisions, drift
- Explicit by default — no hidden behavior
- Operator-controlled at all times

---

*Preserved for Phase 3B / beta planning. Not active work.*
