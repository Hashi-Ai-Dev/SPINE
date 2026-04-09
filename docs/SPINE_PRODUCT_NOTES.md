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



---

## Pre-Beta-Exit Triage Rule — Internal Policy

**Classification:** Internal governance policy — not for public copy.
**Applies to:** All SPINE contributors and agents.

### Core Rule

Before beta exit, prioritize only work that materially improves:
- Trust
- Agent usability
- Contract truth
- Beta-exit proof

Do NOT use "more polish" as a reason to expand scope endlessly.

### Beta-Exit Pass Criteria

SPINE must not exit beta until ALL are true:
1. 0 known blocker bugs on shipped core surface
2. 0 known high-severity trust/usability bugs on core agent workflows
3. Docs, command examples, and actual CLI behavior tell the same truth
4. SPINE's own repo looks self-governed and credible
5. Repeated-use proof is strong enough that beta exit is a confirmation step, not a discovery step

### What Must Be Prioritized

**A) Agent trust + usability:**
- Machine-readable outputs, queryable governance state, first-run ergonomics
- Readable/queryable evidence + decision surfaces
- Reliable drift detection for agents/tools
- Agent-consumable briefs / handoffs / checks

**B) Repo truth:**
- Stale command examples, docs/CLI mismatches
- Weak or misleading mission state in SPINE's own repo
- Version-story ambiguity, public docs that undermine trust

**C) Beta-exit proof:**
- Repeated governed workflows validated
- Agent use credible in practice
- Trust leaks addressed
- Remaining issues low-risk and explicitly deferred

### Support / Compatibility Rule

Before beta exit, SPINE must remain clearly compatible with and complementary to Claude Code, Codex, oh-my-claudecode, Superpowers, and OpenClaw.

Favor: stable CLI contracts, plain file contracts, deterministic `--json`, local-first usage, brief generation, startup/skill clarity for external agent runtimes.

Do NOT prioritize work that makes SPINE a competing orchestration platform, dashboard-first, cloud-first, dependent on hidden automation, or tightly coupled to only one runtime.

### Triage Decision Rule

Every new issue/finding must be classified as exactly one of:

1. **MUST FIX BEFORE BETA EXIT** — affects agent trust, public contract correctness, repo self-credibility, reproducible workflow reliability, or compatibility for Claude Code/Codex/oh-my-claudecode/Superpowers/OpenClaw

2. **GOOD TO FIX BEFORE BETA EXIT IF CHEAP** — small docs-truth fixes, small ergonomics improvements, version-story cleanup, agent onboarding clarity, small compatibility clarifications

3. **DEFER UNTIL AFTER BETA EXIT** — new platform features, orchestration expansion, dashboards/cloud/remote, speculative abstractions, "nice to have" ideas that do not change trust

### Anti-Sprawl Rule

"Pre-beta-exit polish" does NOT justify issue spam, broad rewrites, architecture drift, new platform ambitions, or "while we're here" expansion. Only fix things that reduce meaningful trust leaks.

### External-Runtime Rule

If a finding improves support for Claude Code, Codex, oh-my-claudecode, Superpowers, or OpenClaw — treat it as strategically important IF it improves SPINE as a governance layer ABOVE those tools. Do NOT chase parity with those tools' orchestration features. Do NOT turn SPINE into their replacement.

### One-Line Operating Principle

Before beta exit, fix every meaningful trust leak for agents and operators — especially across Claude Code, Codex, oh-my-claudecode, Superpowers, and OpenClaw — and defer everything else.


## External Agent Feedback — Pre-Beta-Exit Validation (2026-04-09)

**Source:** External coding-agent evaluation session.
**Classification:** Internal product guidance — not for public copy.

### What landed as real value
- Repo-native `.spine/` governance state
- `brief --target claude` — agent-consumable governance context (strongest product wedge)
- Git-native `drift scan` — explicit scope drift detection
- Proof/decision logging — auditable trail

### What remains the biggest risk
Discipline tax: repeated manual `decision add` / `evidence add` feels like overhead.
May not sustain without sufficient payoff in real, messy agent workflows.

### Correct positioning
NOT "every solo dev should use this."

SPINE earns its keep when:
- Drift, coordination failure, and proof ambiguity become expensive
- AI-heavy or multi-agent workflows are running
- Long-running projects where context decays

### What SPINE is NOT
Do NOT overreact into dashboards, cloud, remote platform creep, or hidden automation theater.
These erode the explicit/local/repo-native model that makes SPINE trustworthy.

### Beta-exit standards
Before calling beta ready, validate:
- First-run and session-start ergonomics feel low-friction
- Docs truth: nothing misleading about command scope or behavior
- Discipline tax is reduced, not just documented
- Governance feels worth the overhead in real, messy agent workflows

### Fold into existing work
Discipline-tax reduction → Beta polish queue (#51 beta-exit proof)
First-run ergonomics → consider in #50 before-work checkpoint refinement
Docs truth → #59, #60
Messy-repo validation → no issue yet — note for Phase 3B candidates

*One-line takeaway: SPINE's concept is real, but adoption depends on reducing discipline tax enough that governance feels worth the overhead in real, messy agent workflows.*



---

## External Agent Adoption Read — Agent Credibility Validation (2026-04-09)

**Source:** External agent evaluation session.
**Classification:** Internal product guidance — not for public copy.

### Adoption status

SPINE is already credible for **Claude Code CLI** and **Codex** as a governance layer above execution. **OpenClaw** is compatible in principle but not yet first-class in docs/onboarding.

### Trust signals that landed well

- Real CLI, `--cwd` / `SPINE_ROOT`, stable exit behavior, `--json`, local-only operation
- Agent-readable repo files (`.spine/*.jsonl`)
- CI + tests as trust signals
- Drift / check / brief / MCP / review surfaces

### What this validates

- SPINE is past "interesting idea" — it is now a **real agent-governance repo**
- `brief --target ...` + repo-native agent files are the strongest adoption wedge
- File-native, inspectable, deterministic governance is landing as intended

### Main hesitations exposed

1. **Repo's own mission quality is too weak** — blank/generic mission reduces trust immediately
2. **Instruction-surface drift is still dangerous** — stale examples create friction; SPINE must not become a source of agent confusion
3. **Version-story ambiguity weakens confidence** — README / release / package version should tell one coherent story
4. **OpenClaw needs a thin first-class startup contract** — skill/onboarding should be explicit, not just "compatible in theory"

### Durability signal

Ephemeral outputs (briefs, reviews) correctly gitignored; durable governance (decisions, evidence, drift) committed. That split improves agent trust materially.

### Strategic direction

Keep: repo-native governance above execution; strongest when drift/coordination/proof ambiguity become expensive.
Do NOT drift into: orchestration theater, cloud/platform sprawl, "universal agent framework" positioning.

### Follow-up implications (no new issues — fold into existing work)

- Mission quality → relevant to #51 (beta-exit proof)
- Stale command examples → already addressed via AGENT_SKILL normalization; remain vigilant
- Version story → note for Phase 3B
- OpenClaw first-class path → Phase 3B candidate

*One-line takeaway: SPINE is already agent-credible, but trust still depends on operational sharp edges being cleaned up so agents can rely on it instead of merely tolerating it.*


*Preserved for Phase 3B / beta planning. Not active work.*
