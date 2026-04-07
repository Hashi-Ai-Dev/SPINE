# SPINE Internal Roadmap

## Purpose of this document

This is the **internal roadmap and release-gating document** for SPINE.

It exists to answer four questions clearly:

1. What state is SPINE actually in right now?
2. What must happen before SPINE exits alpha?
3. What should beta prove?
4. What must be stable before SPINE can honestly claim `v1.0.0`?

This file is intentionally more operational and more explicit than the public roadmap.  
It is for maintainers, future sessions, and agents working on SPINE itself.

For public-facing positioning, use the public roadmap and README.  
For implementation truth, also consult:
- `docs/SPINE_STATUS.md`
- `docs/SPINE_FEATURE_BACKLOG.md`
- `docs/SPINE_PHASE3A_v0.2_SPEC.md`
- active issues and milestones

---

## 1. Current Verified State

SPINE is in **public alpha**.

Current verified state:
- `v0.1.2` stabilization is complete
- `v0.2 / Phase 3A` is the active implementation phase
- Phase 3A is approved for implementation
- Issue `#15` (explicit repo targeting contract) is complete
- Issue `#16` (repo/branch context visibility) is complete
- the next planned step is Issue `#17`
- the remaining open Phase 3A issues are `#17` and `#18`

That means SPINE is no longer proving the core loop exists.  
It is now proving that it can become **portable, agent-executable, and repeatedly usable without collapsing into ceremony or drift**.

---

## 2. Product North Star

SPINE is a **repo-native mission governor for AI coding workflows**.

It sits **above** coding agents and helps keep work:
- focused
- bounded
- reviewable
- evidence-backed
- resistant to drift

### Core product rule

**Agents may execute governance mechanics. Operators retain governance authority.**

This is the core trust model for the roadmap.

It means:

#### Agents may execute
- reading mission and constraints before work
- generating task-scoped briefs
- running doctor checks
- running drift scans
- drafting evidence entries
- drafting decision entries
- producing handoff/review summaries
- preparing CI-safe and PR-safe governance outputs

#### Humans retain authority over
- mission direction
- scope expansion
- pivots or kills
- roadmap/phase intent
- canonical public repo truth
- whether drift is acceptable or must be reversed

This must remain stable across all phases.

---

## 3. Roadmap Principles

Everything below should reinforce these rules:

1. **Repo-native truth first**
   - canonical truth remains in `.spine/` files and repo contract surfaces
   - never in hidden runtime state

2. **Governance above generation**
   - SPINE is not another coding agent
   - it governs coding-agent workflows

3. **Trust over novelty**
   - deterministic behavior, visible state, inspectable artifacts, and explicit authority beat cleverness

4. **Discipline tax is a first-class product problem**
   - if governance becomes too annoying to sustain, SPINE fails

5. **Open-source maturity is part of product maturity**
   - issue discipline, milestones, CI, release notes, docs, and repo hygiene are part of the product, not side chores

---

## 4. Alpha Exit

### Goal

Exit alpha only when SPINE is **trustworthy enough for repeated real use** across arbitrary repos.

Alpha exit is not just "implemented enough."
It is "implemented enough, validated enough, and clear enough."

### Alpha Exit Work

#### A. Complete Phase 3A remaining issues

##### Issue #17 — Operator / CI output modes + stable exit codes

What this should achieve:
- `--json` on operationally justified commands
- `--quiet` where reduced-noise healthy-path behavior is useful
- stable, documented exit codes
- output trustworthy enough for CI and automation

Why it matters:
- if SPINE is only human-readable, agents and CI will treat it as advisory text
- Phase 3A is explicitly about portability and operator polish, so stable machine-readable surfaces are core scope, not optional polish

##### Issue #18 — Bootstrap polish + discipline-tax ergonomics

What this should achieve:
- clearer first-run expectations
- clearer prerequisites and verification steps
- fewer confusing or repetitive governance steps
- more specific and consistent errors
- lower ceremony without opacity

Why it matters:
- discipline tax is highest at first use and repeated use
- poor bootstrap and repeated friction are adoption killers

#### B. Add and complete the missing artifact ergonomics work

This should become its own explicit issue if it is not already tracked.

This is not a minor cleanup task.  
It is a formal Phase 3A requirement.

See section **6. Artifact Ergonomics Contract** below.

#### C. Strengthen external-repo docs/examples

This must be strong enough that SPINE is understandable outside the SPINE repo itself.

Expected result:
- non-SPINE repo quickstart
- CI usage examples
- branch workflow examples
- anti-pattern examples
- explicit "govern any repo" walkthrough

---

### Alpha Exit Acceptance Gates

SPINE exits alpha only when **all** of these gates are satisfied:

#### Gate A — Feature gates
- explicit repo targeting is implemented and stable
- repo / branch / compare-context visibility is implemented and stable
- machine-readable output exists where justified
- stable exit-code semantics are documented
- bootstrap/install guidance is improved
- artifact ergonomics contract is implemented enough for real operator and agent use
- external-repo docs/examples are strong

#### Gate B — Validation gates

At minimum, alpha exit must include an explicit validation matrix covering:

- fresh external git repo
- dirty repo
- repo missing `.spine/`
- non-git directory
- detached HEAD
- CI invocation path
- at least one end-to-end branch workflow pass
- at least one end-to-end external-repo workflow pass

#### Gate C — Usability gates
- repeated use feels materially lighter than early alpha
- no major ambiguity remains around targeting or context
- no hidden or magical behavior was added to reduce friction

#### Gate D — Anti-drift gates
- no dashboard creep
- no cloud/control-plane creep
- no hidden daemons/background automation
- no model-required governance logic
- no authority-model erosion

### Alpha Exit Deliverable

Target outcome: **`v0.2.0-beta`**

---

## 5. Contract Stability Policy

This section becomes active **before beta** and must be used throughout beta.

The reason: once operators, CI systems, and agents start wiring to SPINE's contracts, unstable semantics become a product liability.

### Contract categories

#### Stable

A surface is **stable** when:
- it is documented
- it is expected to remain backward-compatible across minor releases
- changes require explicit migration or versioning treatment

Examples by the time SPINE reaches beta:
- canonical `.spine/` truth model
- repo targeting precedence contract
- core mission/evidence/decision/drift/review semantics
- documented exit-code classes
- established machine-readable output fields that external tooling may consume

#### Provisional

A surface is **provisional** when:
- it is intended for real use
- it may still change during beta
- changes must still be documented and justified

Examples:
- newly introduced handoff or checkpoint commands
- branch-local governance lane semantics
- draftable evidence/decision helper flows
- local MCP surface expansions during beta

#### Experimental

A surface is **experimental** when:
- it is intentionally unstable
- it is not yet promised as durable
- it should not be marketed as a dependable automation contract

Examples:
- early beta convenience helpers
- experimental branch-local workflows
- optional tool-facing schemas not yet frozen

### Stability policy rules

1. Publicly documented automation surfaces must be labeled as stable, provisional, or experimental.
2. Stable surfaces must not change casually.
3. Provisional surfaces may evolve, but changes must be announced in release notes and reflected in docs.
4. Experimental surfaces must not be presented as settled product contracts.
5. By `v1.0.0`, anything central to repeated use must be either stable or removed.

---

## 6. Artifact Ergonomics Contract

This is a formal sub-contract of the roadmap, not a leftover task.

SPINE cannot become agent-executable in practice if artifacts remain hard to locate or ambiguous.

### Why this matters

Agents and operators need to know where the latest:
- brief
- review
- drift output
- evidence rollup
- handoff artifact

actually lives, without path-guessing.

### Required outcomes

#### 6.1 Canonical latest aliases

For artifact families that produce historical records, SPINE should expose stable "current" references where appropriate.

Examples:
- latest brief
- latest review
- latest drift summary
- latest handoff artifact

#### 6.2 Deterministic file naming

Artifact names should be:
- predictable
- script-friendly
- human-readable enough for inspection
- stable enough that docs/examples can rely on them

#### 6.3 Machine-readable artifact manifest

SPINE should eventually expose a machine-readable way to identify:
- current artifacts
- historical artifacts
- artifact type
- branch/task relevance where appropriate

This does **not** require a database or cloud service.

#### 6.4 Draft vs canonical distinction

Where relevant, SPINE should distinguish:
- proposed/draft artifacts
- canonical artifacts
- branch-local artifacts
- promoted canonical artifacts

This becomes especially important in beta once governance mechanics become more agent-executable.

#### 6.5 Branch-local vs canonical placement

If branch-local governance artifacts exist, their location and promotion path must be explicit.

SPINE must not silently blur:
- local branch working state
- canonical repo truth

### Acceptance for this contract

Alpha should at least establish:
- deterministic artifact naming
- stable latest aliases where justified
- predictable artifact locations in docs/examples

Beta may extend this into:
- artifact manifests
- richer branch-local vs canonical workflows
- handoff/PR-prep artifact sets

---

## 7. Beta

### Goal

Beta is where SPINE proves that it can be used **repeatedly in real AI-assisted workflows** without turning governance into a burden.

This is where the product note becomes active in earnest:

> SPINE should reduce discipline tax not by hiding governance, but by making governance easy for agents and tools to execute explicitly.

### Beta Product Definition

#### What "agent-friendly" should mean
- stable command contracts
- machine-readable outputs
- deterministic repo targeting
- visible context
- predictable artifact locations
- auditable state changes
- easy handoff between tools

#### What "agent-friendly" must not mean
- silent background behavior
- hidden auto-logging
- invisible scope changes
- orchestration creep
- opaque "smart governance"
- replacing operator judgment

### Beta Workstreams

#### Workstream 1 — Task-scoped governance lanes

Possible outcomes:
- issue-scoped brief generation
- task-local or branch-local governance lanes
- clearer bounded lane workflows
- promote-to-canonical flow for approved outputs

#### Workstream 2 — Handoff and PR-prep primitives

Possible outcomes:
- handoff summaries
- PR-prep governance summaries
- evidence rollups
- "what changed against mission" views

#### Workstream 3 — Preflight / checkpoint commands

Possible outcomes:
- before-work checks
- before-PR checks
- after-test checks
- explicit governance gates

#### Workstream 4 — Draftable evidence / decision workflows

Possible outcomes:
- draft evidence helpers
- draft decision helpers
- clear proposed-vs-canonical distinction
- human approval where authority matters

#### Workstream 5 — Stronger local tool-consumption surfaces

Possible outcomes:
- richer local MCP resources
- stable schemas for:
  - current mission
  - latest brief
  - open drift
  - latest review
  - recent evidence / decisions

#### Workstream 6 — Branch-local governance hygiene

Possible outcomes:
- keep-local vs promote-canonical rules
- protections against accidental canonical churn
- safer branch-local `.spine/` use

---

### Beta Acceptance Gates

Beta is successful only if all of the following are true:

#### Gate A — Repeated-use proof

SPINE must be demonstrated in repeated real use, not just one-off demos.

Minimum proof targets should include:
- SPINE used on itself plus at least **2–3 unrelated repos**
- at least **N real PRs** prepared using SPINE artifacts
- at least **N consecutive sessions** where the evidence/decision/drift/review loop was actually used
- at least one documented case where SPINE visibly prevented or bounded drift in a real workflow

The exact `N` can be decided operationally, but the principle must hold:  
**proof of repeated use is a release artifact, not just a belief.**

#### Gate B — Trust-model proof
- agents can execute governance mechanics reliably
- humans still clearly control mission truth and scope changes
- no invisible or magical governance behavior becomes necessary for repeated use

#### Gate C — Open-source proof
- docs support real external adoption
- issue/release discipline is strong
- contribution surfaces are credible enough for outside use
- CI/release process is dependable

### Beta Deliverable

Target outcome: **release candidate path to `v1.0.0`**

---

## 8. v1.0.0

### Goal

`v1.0.0` means SPINE is stable enough that:
- people can depend on its contracts
- its trust model is clear
- its authority boundaries are stable
- its automation surfaces are dependable
- repeated real use has been demonstrated

It does **not** mean "finished forever."

### v1.0.0 Requirements

#### 8.1 Stable command contract

The core CLI should feel settled.

#### 8.2 Stable file/state contract

The `.spine/` model must be documented, durable, and migratable.

#### 8.3 Stable authority boundaries

The line between:
- agent-executable mechanics
- human-authorized governance decisions

must be explicit and trustworthy.

#### 8.4 Stable automation-facing surfaces

Machine-readable outputs, exit codes, artifact contracts, and tool-consumption surfaces must be stable enough for real dependency.

#### 8.5 Real-world proof

SPINE should not hit 1.0 because the maintainers are tired of saying alpha or beta.
It should hit 1.0 when repeated real use has been demonstrated and documented.

#### 8.6 Documentation maturity

By v1, docs should clearly cover:
- quickstart
- external-repo usage
- command reference
- governance model
- troubleshooting
- migration/versioning
- advanced/agent workflows

#### 8.7 Maintenance maturity

By v1, repo operations should be boring in the best way:
- dependable releases
- clear changelog / release note practice
- issue and milestone hygiene
- contribution/security/community surfaces
- strong CI
- normal open-source maintenance expectations

---

### v1.0.0 Acceptance Gates

#### Gate A — Contract gates
- command contracts are stable
- file/state contracts are stable
- automation-facing surfaces are stable
- authority boundaries are stable

#### Gate B — Validation gates
- repeated real use is documented
- migration/versioning policy exists where needed
- no unresolved ambiguity remains in core operator flows

#### Gate C — Credibility gates
- repo/release/docs posture is credible for a serious open-source tool
- no major internal/public doc contradictions
- no known product-identity drift

---

## 9. Open-source / GitHub Maturity

### Beta-required

These should be treated as beta-required, not vague future nice-to-haves:
- `CONTRIBUTING.md`
- PR template
- changelog / release discipline
- clear docs index
- dependable milestone hygiene

### v1-preferred

These are still desirable, but do not need to be front-loaded if they would create noise:
- broader contributor workflow optimization
- fuller community-health polish
- more advanced org-level defaults and contributor experience improvements

This split matters because the repo should not pretend to be more socially mature than it actually is.

---

## 10. Discipline-tax Strategy

### Working thesis

SPINE should reduce discipline tax not by hiding governance, but by making governance easy for agents and tools to execute explicitly.

### What this means in practice

#### Good targets
- reading mission and constraints before work
- generating task-scoped briefs
- running doctor checks
- running drift scans before PRs
- drafting evidence entries after real work
- drafting decision entries for real tradeoffs
- producing handoff and review summaries
- preparing CI-safe and PR-safe outputs

#### Human-authority boundaries remain
- mission changes
- scope expansion
- pivots / kills
- roadmap or phase changes
- canonical public repo truth
- acceptance of drift vs rollback

### Roadmap use of this lens

**In Alpha** — reduce obvious friction:
- targeting
- context visibility
- machine-readable output
- bootstrap clarity
- artifact discoverability
- external-repo examples

**In Beta** — make governance mechanics more executable:
- task lanes
- handoff / PR-prep
- draftable records
- checkpoints
- richer local tool surfaces

**In v1** — stabilize these behaviors so they are dependable and inspectable.

---

## 11. Out-of-scope Guardrails

These remain **out of scope** unless a future spec explicitly changes direction:

- dashboard-first control surfaces
- cloud sync / cloud control plane
- remote MCP hosting
- account systems
- billing
- multi-user collaboration
- autonomous multi-agent orchestration
- hidden background governance daemons
- model-required governance logic
- silent canonical state mutation
- broad platform sprawl disguised as ergonomics

> SPINE should reduce friction **without reducing visibility**.

---

## 12. Immediate Next Priorities

1. Complete Issue `#17`
2. Complete Issue `#18`
3. Add and complete the explicit artifact ergonomics issue/contract work
4. Verify external-repo docs/examples are strong enough for alpha exit
5. Run the alpha-exit validation matrix
6. Exit alpha only when the actual gates are met

---

## 13. Final Position

SPINE is not trying to become another coding agent or an orchestration platform.

It is trying to become the **trustworthy governance layer above AI coding tools**:
- repo-native
- explicit
- inspectable
- auditable
- sustainable in repeated real use

That is the path:
- out of alpha
- through beta
- to `v1.0.0`
