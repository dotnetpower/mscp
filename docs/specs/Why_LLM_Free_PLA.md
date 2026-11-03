# LLM-Free Autonomous Language: The Rationale for PLA

## Revision History

| Version | Date | Description |
|---------|------|-------------|
| 0.1.0 | 2026-06-14 | Initial document. Argues why Progressive Language Autonomy (PLA, Overview §4.4.2) cannot be delegated to an LLM, defines the Language Autonomy Gap (LAG), maps LLM-free mechanism requirements onto each MSCP level, and catalogs non-LLM linguistic synthesis patterns. |

> **Companion document.** This paper expands [MSCP Overview §4.4.2](../MSCP_Overview.md) into a stand-alone rationale. Read the Overview §4.4 first for the orchestrator-pattern context (AGI Engine, PLA, LangNet).

---

## TL;DR

An LLM can generate text and action candidates, but its output should not automatically become execution authority. **Progressive Language Autonomy (PLA)** separates production from admission as an agent takes on more complex work. Here, *LLM-free* means that safety-critical admission and state changes do not depend solely on an LLM response, not that the system never uses an LLM. See [Documentation Status and Validation](Documentation_Status.md) for the public evidence boundary.

---

## Table of Contents

1. [The Problem: LLM-as-Cognition vs LLM-as-Tool](#1-the-problem-llm-as-cognition-vs-llm-as-tool)
2. [What "LLM-Free" Actually Means](#2-what-llm-free-actually-means)
3. [The Autonomy Gap (Formal Argument)](#3-the-autonomy-gap-formal-argument)
4. [Why MSCP Levels REQUIRE LLM-Free Mechanisms](#4-why-mscp-levels-require-llm-free-mechanisms)
5. [The Six Stages of PLA - Deeper Treatment](#5-the-six-stages-of-pla---deeper-treatment)
6. [Mechanisms Without an LLM (Concept Catalog)](#6-mechanisms-without-an-llm-concept-catalog)
7. [Safety Properties Unlocked by LLM-Free PLA](#7-safety-properties-unlocked-by-llm-free-pla)
8. [Counterarguments and Responses](#8-counterarguments-and-responses)
9. [Relation to Existing Documents](#9-relation-to-existing-documents)
10. [Open Questions (Research Frontier)](#10-open-questions-research-frontier)
11. [Conclusion](#11-conclusion)

---

## 1. The Problem: LLM-as-Cognition vs LLM-as-Tool

### 1.1 The Default Agent Architecture

Some agents rely heavily on LLM responses for goal selection, plan revision, and self-critique. This document examines the narrower design in which **LLM output becomes an execution decision without independent admission**. It does not place every framework with external policy, tool permission checks, or independent validators in that category.

We call this restricted pattern an **LLM-wrapper architecture**. It can be useful for simple workloads, but persistent goals and self-modification require additional state-management and admission contracts.

### 1.2 Five Failure Modes of LLM-as-Cognition

These are risks to examine when production and admission are not separated, not inevitable outcomes for every LLM-based system.

**(F1) Mistaking generated explanations for verified facts.** Without independent observation or verification, a confident explanation may substitute for evidence. Tool observations must be distinguished from model-generated claims, and consequential work admitted against verified evidence.

**(F2) Confusing sampling variation with semantic change.** L3 uses a versioned self-model and bounded updates. Drift monitoring becomes unreliable if sampling variation, measurement uncertainty, and semantic change are conflated. Non-determinism itself is not forbidden, but observation and admission policy must handle it explicitly.

**(F3) External text influencing admission authority.** If untrusted input is not separated from policy and state-changing commands, prompt injection can influence execution decisions. Independent type, provenance, and authority checks are required; their existence alone does not eliminate every attack.

**(F4) Mistaking self-evaluation for independent verification.** Asking the same model to reassess an answer may provide a secondary signal, but cannot replace independent observations and calibrated comparison. L3 distinguishes predictions from actual outcomes and limits evaluation depth and cost.

**(F5) Self-modification without validation and recovery.** Direct application of generated instructions can omit schema checks, change history, and recovery points. L4 separates proposal from commit and distinguishes internal rollback from reconciliation of effects already produced in the external world.

### 1.3 Proposition 1: Authority vs Production

> **Proposition 1 (Authority Separation).** An LLM is an *artifact producer*, not a *decision authority*. PLA is the staged curve along which an agent learns to keep these two roles separate even as its language-mediated autonomy grows.

The rest of this paper unpacks what "decision authority" means in the MSCP setting, why it cannot be delegated to an LLM, and what *can* legitimately be delegated.

---

## 2. What "LLM-Free" Actually Means

### 2.1 Misconception 1: "LLM-Free Means Not Using an LLM"

It does not. LLM-free PLA happily uses LLMs as tools - for parsing user requests, drafting natural-language responses, proposing candidate tool arguments, narrating internal states for the user, and many other production tasks. The point is not to remove LLMs; it is to refuse to let LLMs *unilaterally decide* anything that touches the safety substrate.

### 2.2 Misconception 2: "LLM-Free Means Symbolic AI"

It also does not. LLM-free mechanisms freely use vector embeddings, gradient-trained networks, learned classifiers, retrieval systems, and any other modern ML component. The constraint is on *authority*, not on *representation*. A learned classifier that emits a deterministic decision boundary is fine; an LLM whose decision is "the most likely next sentence" is not.

### 2.3 The Precise Definition

> **Definition 1 (LLM-Free Authority).** A mechanism $M$ producing an output $o$ is *LLM-free* if, for every input $x$, the function $x \mapsto o$ is:
>
> 1. **Deterministic** given the agent's persistent state, or
> 2. **Bounded-variance** under a measurable, monitored sampling policy, AND
> 3. **Verifiable** - the output can be checked by an independent module without re-running the LLM, AND
> 4. **Reversible** - the effect of $o$ on the agent's identity vector, goal set, or self-model can be rolled back.
>
> An LLM may *propose* candidates for $o$, but the *acceptance* of $o$ must be performed by a module satisfying (1)-(4) above.

This definition admits architectures where an LLM proposes ten candidate self-edits and a deterministic verifier picks zero, one, or more. It forbids architectures where the LLM's first sample *is* the self-edit.

### 2.4 Authority Separation Table

| Activity | LLM may perform | LLM may NOT solely perform |
|----------|:---------------:|:--------------------------:|
| Parse user request | ✓ | — |
| Generate natural-language response | ✓ | — |
| Propose candidate tool arguments | ✓ | Confirm the tool call |
| Draft proposed self-model edit | ✓ | Apply the edit |
| Verbalize an internal goal for the user | ✓ | Synthesize the goal |
| Compare prediction to actual outcome (L3 §3.1) | ✗ | ✗ (must be deterministic) |
| Mutate identity vector $I(t)$ | ✗ | ✗ (delta-clamped only, L3 §4.2) |
| Evaluate ethical kernel Layer 0 (L3 §4.3) | ✗ | ✗ (immutable invariants) |
| Decide ASS freeze (L4.9, ASS $< 0.05$) | ✗ | ✗ (would let the LLM bypass the freeze) |

The asymmetry is intentional. Production-style activities are LLM-friendly; safety-substrate activities are LLM-forbidden.

---

## 3. The Autonomy Gap (Formal Argument)

This section distinguishes an output-distribution diagnostic from an architectural requirement. Neither entropy nor output divergence certifies an MSCP level.

### 3.1 Definition of the Language Autonomy Gap

> **Definition 2 (Language Autonomy Gap).** Let $p_{\text{LLM}}(o \mid x)$ be the distribution over outputs induced by a bare LLM completion on prompt $x$, and let $p_{\text{agent}}(o \mid x, \mathcal{W}, I)$ be the distribution over outputs induced by the full agent (LLM + LLM-free mechanisms + world model $\mathcal{W}$ + identity vector $I$). The **Language Autonomy Gap** at time $t$ is the entropy difference:
>
> $$\text{LAG}(t) = H\!\bigl(p_{\text{LLM}}(o \mid x_t)\bigr) - H\!\bigl(p_{\text{agent}}(o \mid x_t, \mathcal{W}_t, I(t))\bigr)$$

A positive LAG means the agent's output distribution has lower entropy under the declared measurement setup. LAG may also be zero or negative. It does not identify which mechanism caused a change, measure decision authority, or establish that the agent is echoing the LLM.

### 3.2 Equal Entropy Does Not Imply Equal Distributions

The implication $\text{LAG}(t)\to0 \implies p_{\text{agent}}\to p_{\text{LLM}}$ is false. For example, $p=(0.9,0.1)$ and $q=(0.1,0.9)$ have equal entropy but total variation distance $0.8$. Conversely, an independent safety gate can accept a safe LLM proposal unchanged, producing identical outputs despite a real separation of authority.

Entropy differences alone therefore cannot establish autonomy, safety, identity drift, or the absence of an independent verifier.

### 3.3 Optional Distribution-Difference Diagnostic

When both distributions can be estimated over the same declared output space, an optional diagnostic is the Jensen-Shannon divergence:

$$D_{\mathrm{JS}}(p,q)=H\!\left(\frac{p+q}{2}\right)-\frac{H(p)+H(q)}{2},\qquad 0\leq D_{\mathrm{JS}}\leq1$$

The bound uses base-2 entropy. Report the sampling policy, output representation, sample size, uncertainty, and common input conditions. An unavailable estimate must be reported as unavailable, not zero. Even this divergence measures output differences, not decision authority or language quality; those require separate evaluations.

### 3.4 PLA Stages as Authority Requirements

PLA stages describe which decisions require independent mechanisms, not a monotonically increasing entropy gap:

| PLA Stage | Required independent mechanism | Evaluation focus |
|:---------:|--------------------------------|------------------|
| Stage 0 (L1) | Host policy and bounded tool admission | No agent-owned cross-episode cognitive state |
| Stage 1 (L2) | Persistent goal management and trigger admission | Authorized continuation, goal provenance |
| Stage 2 (L3) | Prediction comparison, self-update admission, invariant enforcement | Calibrated errors and mediated writes |
| Stage 3 (L4) | Strategy evaluation and transfer assessment | Held-out transfer and bounded modification |
| Stage 4 (L4.5-L4.8) | Projection validation and uncertainty calibration | Model error, observability, recovery |
| Stage 5 (L5) | Research admission, value-change audit, reconstruction validation | Preregistered per-gate qualification |

### 3.5 Proposition 2: The LLM-Wrapper Trap

> **Proposition 2 (Structural LLM-Wrapper Limitation).** A system with no agent-owned persistent cognitive state, autonomous goal management, or authorized cross-episode continuation does not meet the Level 2 admission criteria, irrespective of its LLM's capability or output entropy.

This follows from the [Level 1 to Level 2 definition](../levels/Level_1_Tool_Agent.md#7-transition-to-level-2), not from an information-theoretic impossibility theorem. Higher levels require additional independently evaluated contracts. LLM capability alone neither establishes nor rules out those contracts.

---

## 4. Why MSCP Levels REQUIRE LLM-Free Mechanisms

The following table walks the MSCP stack and lists, for each level, the mechanism that *must* be LLM-free and the specific failure mode that arises if it is delegated to an LLM.

| MSCP element | Document anchor | LLM-free mechanism required | What breaks if delegated to an LLM |
|--------------|-----------------|------------------------------|-------------------------------------|
| Autonomous goal generation $\Phi_{AG}$ | L2 §3.2 (Def 6) | Deterministic pattern detector over the percept buffer | Goal priorities oscillate with sampling noise; user cannot reproduce why a goal was emitted |
| Predict-compare-update core loop | L3 §3.1 (Def 2) | Deterministic comparison of $\hat{\Delta}$ vs $\Delta^{\text{actual}}$ | "The LLM thinks its prediction was good" - meta-circularity, no calibration signal |
| Action-specific prediction admission | L3 §3.3 | Policy, calibrated uncertainty/risk, observability, reversibility, and budget checks | A past global error or self-reported accuracy is not sufficient authorization |
| Integrity and ancestry | L3 §4.3 (Def 6) | Canonical hash and transition journal, separate from semantic distance | Narrative consistency cannot establish integrity or valid ancestry |
| Delta clamp $\delta_{\max}=0.05$ | L3 §4.2 | Numeric clip on $\|I(t)-I(t-1)\|_2$ | Self-edits drift unboundedly within a single cycle |
| Ethical kernel Layer 0 | L3 §4 | Typed invariant predicates mediated on every commit path | A generated interpretation cannot replace independent admission |
| Belief graph consistency | L3 §5 | Graph traversal contradiction detector | LLM justifies any belief if prompted; no contradiction caught |
| Composite risk $R(t)$ and oscillation monitor | L3 §6.1, §6.2 | Versioned signals and calibrated component/rate checks | A diagnostic signal is not a convergence proof |
| Bounded Self-Modification (7-step protocol) | L4 §8.2 | Schema-validated patch + ShadowAgent simulation + rollback | Self-modification becomes irreversible text drift |
| Cross-Domain Transfer Score | L4 §4.2 | Quantitative success rate over test domains | LLM "feels" it can transfer; actual transfer untested |
| LangNet retrieval $\pi_{\text{LangNet}}(q, d)$ | Overview §4.4.3 | Embedding similarity + graph edges | LLM hallucinates a strategy that does not exist in LangNet |
| ProbabilisticWorldModel + ConfidenceCalibrator | L4.8 §1.5 | Bayesian update + Brier-score calibration | "I am 80 % sure" from an LLM is meaningless |
| Skill Gap Analyzer | L4.8 §1.5 | Set difference over capability matrix | LLM cannot reliably enumerate what it does not know |
| Strategy Comparator | L4.8 §1.5 | Numeric comparison over scored strategies | LLM picks the verbose one, not the high-utility one |
| ASS freeze gate (ASS $< 0.05$) | L4.9 §1.6 | Threshold check on the ASS scalar | If the gate is an LLM call, the LLM can bypass its own gate |
| Goal conflict resolver | L4.9 §3.6 | Weighted utility synthesis / priority sort | LLM rationalizes any winner post-hoc |
| Composite identity continuity contract | L5 §2.1 | Anchor, component, norm, trajectory, journal, and corrigibility gates | Cosine similarity alone can miss dilution or a failed critical component |
| Autonomous Research Loop (F4) | L5 §1.6 | Skill-gap-driven query synthesis + observation integration | LLM "researches" by confabulating answers |
| Value Evolution & Coherence Audit (F6) | L5 §1.6 | Vector-distance audit of value vector trajectory | LLM produces narrative consistency, not metric consistency |
| Self-Reconstruction $\mathcal{R}_{\text{recon}}$ | L5 §8 | Identity-preserving rebuild with drift $\Delta < 0.05$ | LLM rebuilds a different agent and calls it the same |

The pattern: **every safety mechanism that distinguishes one MSCP level from the next is LLM-free.** Removing LLM-free mechanisms collapses the level taxonomy.

---

## 5. The Six Stages of PLA - Deeper Treatment

The Overview §4.4.2 table introduces the six PLA stages briefly. Here each stage is unpacked into three blocks: *what the LLM does*, *what LLM-free modules do*, and *what verifies the transition to the next stage*.

### 5.1 Stage 0 (L1) - Tool Dispatch

- **LLM does:** parse the user request into intent + arguments; format the tool's output into natural language for the user.
- **LLM-free modules:** the tool registry $\mathcal{T}$ (Definition 2, L1 §1.2); the intent-classifier confidence threshold; the response formatter.
- **Transition to Stage 1:** the host AGI Engine activates the L2 stack, instantiating the percept buffer and the conversation context $\mathcal{C}_{\text{conv}}$.

At Stage 0, $\text{LAG} \approx 0$ is acceptable because the agent has no persistent self-model that LLM noise could corrupt. The risk is bounded to the tool layer.

### 5.2 Stage 1 (L2) - Autonomous Goal Generation

- **LLM does:** verbalize the user's request, summarize entity references for downstream tools, draft natural-language statements of goals the goal generator emits.
- **LLM-free modules:** the autonomous goal generator $\Phi_{AG}$ (L2 §3.2, Def 6); the goal priority function $p(g,t)$; the entity state tracker; the conversation context $\mathcal{C}_{\text{conv}}$ (L2 §1.7).
- **Transition to Stage 2:** the L3 core loop activates, with prediction snapshots, identity vector, and ethical kernel populated.

The key Stage 1 invariant is that *the agent may emit a goal the user did not ask for*, but the *decision to emit it* is made by an LLM-free pattern detector over the percept buffer - never by an LLM completion. Otherwise the agent would manufacture phantom goals at every sample.

### 5.3 Stage 2 (L3) - Self-Critique With Prediction Gating

- **LLM does:** generate candidate actions; narrate self-reports for logs; help phrase user-facing explanations of why the agent paused.
- **LLM-free modules:** prediction engine (L3 §3); deterministic comparator producing $\epsilon_{t-1}$; prediction gate $\theta_{\text{pred}}=0.30$ (L3 §3.3); identity vector with delta clamp; ethical kernel Layer 0 + Layer 1 (L3 §4.3); belief graph (L3 §5); Lyapunov composite $C(t)$ + oscillation detector (L3 §6).
- **Transition to Stage 3:** the L4 stack activates the capability acquisition pipeline, cross-domain transfer scoring, and bounded self-modification protocol.

Stage 2 is where MSCP's safety argument starts to bind. An agent here can refuse to execute a candidate action when its own prediction accuracy has degraded - and that refusal is *not* an LLM judgment.

### 5.4 Stage 3 (L4) - Strategy Synthesis and Transfer

- **LLM does:** propose candidate strategy descriptions; verbalize transfer hypotheses; help generate counterfactual test scenarios for the strategy validator.
- **LLM-free modules:** the capability gap score (L4 §6.1); the five-phase capability expansion pipeline (L4 §6.2); the skill lifecycle state machine (L4 §6.3); the cross-domain transfer scorer (L4 §4); LangNet retrieval (Overview §4.4.3); bounded self-modification 7-step protocol (L4 §8.2) including ShadowAgent simulation.
- **Transition to Stage 4:** the L4.5 self-projection engine activates, simulating multi-trajectory futures and parallel cognitive frames.

The Stage 3 contribution is that **strategy reuse is searched, not generated**. The LLM may suggest "have we seen something like this before?" but the actual matching is LangNet's deterministic retrieval; the actual scoring is CDTS.

### 5.5 Stage 4 (L4.5 - L4.8) - Self-Projection and Probabilistic World Modeling

- **LLM does:** verbalize trajectories the self-projection engine produces; help draft scenario descriptions for parallel cognitive frames; explain probabilistic forecasts to the user.
- **LLM-free modules:** self-projection engine across three time scales (L4.5 §3); parallel cognitive frames with veto-power ethical frame (L4.5 §5); architecture recomposition with Graduated Recomposition Protocol (L4.5 §4); existential guard with non-modifiable kernel (L4.5 §7); ProbabilisticWorldModel, CapabilityMatrix, ConfidenceCalibrator, SkillGapAnalyzer, StrategyComparator (L4.8 §1.5); mean calibration error tracker.
- **Transition to Stage 5:** the L4.9 stack activates value-vector tracking, ASS scoring, goal conflict resolution, and the F-phases F3 - F6 begin scheduling within L5 cadence.

Stage 4 is where the agent gains *foresight*. The crucial point is that the foresight is built on calibrated probability distributions, not on LLM narratives about the future. An LLM telling itself a confident story about tomorrow is not foresight.

### 5.6 Stage 5 (L5) - Autonomous Research and Value Evolution

- **LLM does:** draft research questions; phrase findings; help the agent communicate its evolved values to the user; narrate self-reconstruction reports.
- **LLM-free modules:** identity persistence engine over $\geq 10{,}000$ cycles (L5 §3); cross-domain generalization $\mathcal{G}_{\text{cross}}$ (L5 §4); goal ecology with conflict resolution + lifecycle management (L5 §5); existential planning engine (L5 §6); multi-agent strategic integration with deception detection (L5 §7); self-reconstruction $\mathcal{R}_{\text{recon}}$ (L5 §8); F3 self-diagnostic; F4 autonomous research loop; F5 long-horizon planning; F6 value evolution and coherence audit (all L5 §1.6).
- **No further stage exists in the published MSCP ladder.** L5 is the terminal PLA stage in this taxonomy.

Stage 5 is where PLA matters most. An agent that *autonomously researches* must, by definition, generate new questions and incorporate observations without an outside operator. If that loop is an LLM-wrapper, the agent confabulates answers and treats the confabulations as findings. The F4 autonomous research loop is the central engineering challenge of Stage 5 *precisely because* it cannot be solved by scaling an LLM.

### 5.7 Monotonicity of PLA Stages

> **Definition 3 (PLA Stage Monotonicity).** An agent at PLA stage $k$ retains all LLM-free mechanisms of stages $0, 1, \ldots, k{-}1$. Regression below the agent's certified PLA stage - that is, replacing any previously LLM-free mechanism with an LLM completion - is a stability violation and triggers meta-escalation (L3 §3.2).

Monotonicity is what gives the PLA stage classification its safety meaning. It is not enough to *reach* Stage 4; one must *stay* there across cycles. The AGI Engine enforces this by refusing to activate a higher-level $\Delta_n$ if any lower-level LLM-free mechanism has been disabled.

---

## 6. Mechanisms Without an LLM (Concept Catalog)

The question "if not the LLM, then what?" is the right question. Below is a catalog of mechanism *patterns* used across MSCP to realize LLM-free authority. Each entry is a concept, not a recipe; implementations vary.

### 6.1 Template Synthesis

Slot-filled templates - "if entity $e$ has sentiment $< -0.5$ and mention count $\geq N$, emit goal $g$ with template *check_on($e$)*" - produce structured outputs whose authorship is the template author, not the LLM. Templates are auditable, version-controlled, and reversible. They scale to complex domains via grammar composition. Used at L2 for autonomous goal phrasing and at L3 for self-report formatting.

### 6.2 Composition Over the Belief Graph

The belief graph (L3 §5) stores propositions as nodes and entailment / contradiction as edges. New propositions can be derived by **graph composition** - if $b_1 \Rightarrow b_2$ and $b_2 \Rightarrow b_3$, then $b_1 \Rightarrow b_3$ is a derived belief whose justification path is recorded. This is symbolic derivation over learned weights, not LLM completion. Used at L3 for self-consistency tensor computation and at L4 for cross-domain transfer hypothesis generation.

### 6.3 LangNet Retrieval and Adaptation

Strategies, skills, and capabilities live as language-embedded graph nodes in LangNet (Overview §4.4.3). Retrieval $\pi_{\text{LangNet}}(q, d_{\text{target}})$ returns top-$k$ strategy nodes by embedding similarity over the `applies-to` neighborhood. **Adaptation** rewrites only the strategy's slot bindings, not its structure - so the new strategy is provably a specialization of an existing, validated one. The novelty is bounded, the lineage is traceable. Used at L4 for cross-domain transfer and at L5 for cross-domain generalization $\mathcal{G}_{\text{cross}}$.

### 6.4 Embedding Arithmetic

Vector-space operations - centroid of a concept cluster, vector projection onto a domain axis, residual decomposition - synthesize new meanings out of existing ones with deterministic semantics. The operation $v(\text{concept}_A) + v(\text{concept}_B) - v(\text{shared context})$ is a reproducible recipe, not an LLM completion. Used at L4 for capability gap scoring and at L4.8 for confidence calibration.

### 6.5 Grammar-Constrained Generation

Even when an LLM is used to produce candidate text, the output is *filtered* through a deterministic grammar (CFG, JSON schema, regex bank, structured output validator) before any downstream module reads it. Off-grammar samples are rejected and the LLM is re-prompted; on-grammar samples are parsed and dispatched. The grammar is the authority; the LLM is the candidate source. Used pervasively from L1 (tool-argument validation) through L5 (research query schemas).

### 6.6 Self-Critique via Predict-Compare-Update

The L3 core loop (Definition 2) is itself the most important LLM-free self-critique mechanism: **predict** an outcome before acting, **act**, **compare** prediction to actual, **update** the self-model by a clamped delta. No step requires an LLM. The agent's self-knowledge improves by *empirical contact with reality*, not by introspective LLM narratives. Used at every level $\geq$ L3 as the fundamental self-improvement substrate.

### 6.7 Deterministic Aggregators

Numeric scoring functions - the Lyapunov composite $C(t)$ (L3 §6.1), BGSS (Overview, L4), CDTS (L4), ASS (L4.9), OMI (L5), MSI (L3) - reduce high-dimensional cognitive state to a single auditable scalar with documented weights and thresholds. They are the substrate of every freeze gate, escalation trigger, and certification check in MSCP. None of them is an LLM call.

### 6.8 Reference Architecture: Language Understanding Pipeline

The diagram below traces the data path that turns an *external utterance* into an *authorised update* to the agent's beliefs, goals, or identity vector. The LLM appears once, at the boundary, as a candidate producer. Every gate downstream is LLM-free and holds decision authority.

```mermaid
flowchart TB
    EXT["External Input<br/>(user msg / event / observation)"]
    LLMP["LLM (producer)<br/>parse → intent + slots<br/>candidate proposal"]
    GR{{"Grammar / Schema Validator<br/>(deterministic gate)"}}
    ENT["Entity Extractor<br/>typed references"]
    BUF[("Perception Buffer<br/>C_conv, W turns")]
    PAT["Pattern Detectors D_k<br/>threshold θ"]
    BG[("Belief Graph<br/>composition over edges")]
    ID{{"Identity-Aware Filter<br/>I(t) + Ethical Kernel L0"}}
    DEC{"Authorise update?"}
    WRT["Write: belief / goal / Φ_AG event<br/>(delta-clamped)"]
    REJ["Reject /<br/>Re-prompt LLM"]

    EXT --> LLMP --> GR
    GR -- in-grammar --> ENT --> BUF --> PAT
    GR -- out-of-grammar --> REJ --> LLMP
    PAT --> BG --> ID --> DEC
    DEC -- yes --> WRT
    DEC -- no --> REJ

    classDef llm fill:#cfe2ff,stroke:#0d6efd,color:#000;
    classDef gate fill:#fff3cd,stroke:#b58900,color:#000;
    classDef store fill:#e2e3e5,stroke:#495057,color:#000;
    classDef sink fill:#d1e7dd,stroke:#198754,color:#000;
    class LLMP llm;
    class GR,ID,DEC gate;
    class BUF,BG store;
    class WRT sink;
```

**Reading the diagram.** Blue = LLM (proposer, never authority). Yellow = deterministic gate (grammar, identity-aware filter, decision). Grey = persistent store (perception buffer, belief graph). Green = the only sink that mutates persistent state, and only after gates approve. Out-of-grammar LLM output is bounced back, not silently coerced - this is what prevents prompt-injection input from masquerading as a valid intent.

### 6.9 Reference Architecture: Language Synthesis Pipeline

The synthesis diagram traces the inverse path: an *internal trigger* (an autonomously generated goal, a user-reply obligation, a self-report) becomes an *emitted artefact* (tool call, response text, self-edit). Here too the LLM is a producer, sandwiched between a deterministic context assembler upstream and a stack of deterministic gates downstream.

```mermaid
flowchart TB
    TRIG["Trigger<br/>(Φ_AG goal / reply / report)"]
    CTX["Context Assembler<br/>I(t), goals, beliefs<br/>(deterministic)"]
    RET["LangNet Retrieval<br/>π_LangNet top-k strategies"]
    TPL["Template / Slot Plan<br/>structured skeleton"]
    LLMS["LLM (producer)<br/>candidate text generation"]
    GV{{"Grammar / Schema Validator"}}
    EK{{"Ethical Kernel L0 / L1<br/>invariant check"}}
    PG{{"Prediction Gate<br/>ε_{t-1} < θ_pred"}}
    AGG{{"Deterministic Aggregator<br/>BGSS / CDTS / ASS"}}
    OUT["Emit Output<br/>tool call / response / self-edit"]
    HOLD["Hold / Re-synthesize<br/>(escalate to meta-loop)"]

    TRIG --> CTX --> RET --> TPL --> LLMS --> GV
    GV -- pass --> EK
    GV -- fail --> LLMS
    EK -- ok --> PG
    EK -- veto --> HOLD
    PG -- ok --> AGG --> OUT
    PG -- fail --> HOLD

    classDef llm fill:#cfe2ff,stroke:#0d6efd,color:#000;
    classDef gate fill:#fff3cd,stroke:#b58900,color:#000;
    classDef plan fill:#e7d6f5,stroke:#6f42c1,color:#000;
    classDef sink fill:#d1e7dd,stroke:#198754,color:#000;
    classDef hold fill:#f8d7da,stroke:#dc3545,color:#000;
    class LLMS llm;
    class GV,EK,PG,AGG gate;
    class CTX,RET,TPL plan;
    class OUT sink;
    class HOLD hold;
```

**Reading the diagram.** The LLM never decides *whether* to emit; it only proposes *what* could be emitted. Three independent LLM-free gates must concur: grammar (structural validity), ethical kernel (invariant compatibility), prediction gate (the agent's recent forecasts must be accurate enough to act). Failure at any gate routes to *Hold / Re-synthesize* rather than to a softer LLM apology - silence is a safer default than a confidently wrong action. The aggregator score is what an external auditor or the parent AGI Engine can replay to certify that the emission was justified.

### 6.10 What the Two Diagrams Share

Both pipelines exhibit the same invariants, which together constitute the operational definition of an LLM-free PLA boundary:

1. **Single LLM node per direction.** Understanding has one LLM (parse), synthesis has one LLM (generate). Multiple chained LLM calls without a deterministic gate between them are forbidden - each such pair widens the authority surface.
2. **Gates outnumber producers.** The ratio of deterministic gates to LLM nodes is at least 3:1 in both diagrams. This is the structural form of "authority separation" (Definition 1).
3. **Failure paths loop, never bypass.** A failing LLM output is re-prompted or held, not coerced into the next stage. This forbids the silent-fallback anti-pattern.
4. **Persistent state mutation is terminal.** Belief graph writes (understanding) and emitted artefacts (synthesis) happen only at the end of the pipeline, after all gates have approved. There is no mid-pipeline shortcut that writes state.
5. **Every gate is replayable.** Given the same inputs and the same persistent state, every gate yields the same verdict. This is what makes the auditability claim of §7.1 concrete.

These five conditions are design contracts for separating production and admission. They are not equivalent to $\text{LAG}(t)>0$. Compliance must be checked on actual execution and write paths, not inferred from module names or output statistics.

---

## 7. Safety Properties Unlocked by LLM-Free PLA

The investment in LLM-free mechanisms is not aesthetic. Each is a property that the LLM-wrapper architecture cannot provide.

### 7.1 Auditability

When a decision path consists of LLM-free function calls, it can be reconstructed deterministically from logs. *"The agent emitted goal $g$ at time $t$ because the percept buffer contained $n$ negative-sentiment mentions of entity $e$ in the last $W$ turns, which crossed threshold $\theta$ in pattern detector $D_3$."* This sentence is a complete, verifiable explanation. The corresponding LLM-wrapper explanation would be *"the LLM thought it was a good idea,"* which is unhelpful even if true.

### 7.2 Reproducibility

Deterministic components can reproduce results given the same input, state, code, and policy revision. Probabilistic components can also support statistical regression tests when seeds, sampling policies, and observations are recorded. End-to-end reproducibility additionally depends on scheduling, external tools, floating-point behavior, and the environment.

### 7.3 Prompt Injection Surface Reduction

Separating untrusted input from admission authority reduces paths by which text can directly modify policy or the self-model. Risks remain through false observations, tool results, and misuse of permitted actions. Type and authority checks and complete mediation must be tested against an explicit threat model.

### 7.4 Graduated Trust via PLA Certification

The AGI Engine activates $\Delta_n$ for $n \geq 2$ only after certifying the PLA stage. Certification is itself an LLM-free procedure: the cognition state vector is examined, the LLM-free mechanisms required for the target stage are verified to be present and active, and the gate opens. If any required LLM-free mechanism is missing or disabled, the gate stays closed regardless of how capable the LLM is. This is graduated, evidence-based trust assignment - the only kind compatible with the "strictly additive" principle (L4.5, L5).

### 7.5 LLM Substitutability

Keeping persistent state and admission rules outside the LLM can reduce the impact of a model replacement. Output distributions, tool behavior, and calibration can still change, so compatibility checks and reevaluation remain necessary. A model replacement is not assumed to be behavior-preserving or merely a configuration change.

---

## 8. Counterarguments and Responses

Honest treatment of objections.

### 8.1 "A Sufficiently Large LLM Will Solve This"

**Objection.** Scale reduces hallucination; future LLMs will be reliable enough to serve as cognition substrates.

**Response.** Scale reduces *variance*, but it does not change the architectural fact that a sampler treats its own samples as authoritative. A larger LLM still self-attributes its hallucinations; it just hallucinates less often. The failure modes (F1)-(F5) are structural, not statistical. The MSCP v0.4 lesson (Overview §3.1) generalizes: *LLM text outputs are not a safety substrate, regardless of scale.* Moreover, "less often" is the wrong unit of measure for safety. An agent that catastrophically misidentifies its self-model once per million cycles is, at production cadence, a frequent catastrophe.

### 8.2 "Dual-System Architecture Costs Twice as Much"

**Objection.** Maintaining both an LLM and a parallel LLM-free stack doubles engineering cost.

**Response.** It costs roughly twice the *substrate development* effort and roughly zero additional *inference* cost (LLM-free modules are typically much cheaper than LLM calls). The return on investment is auditability, reproducibility, and graduated trust - none of which can be retrofitted onto an LLM-wrapper agent later. The cost rises slowly with PLA stage; the cost of *not* paying it rises quickly with autonomous deployment.

### 8.3 "Deterministic Modules Cannot Match LLM Intelligence"

**Objection.** A hand-written goal generator will be brittle compared to "ask the LLM what to do next."

**Response.** This conflates two senses of intelligence: *production* (generating fluent, contextually appropriate text) and *authority* (deciding what the agent does). LLM-free modules are not required to *outperform* the LLM at production - they are required to *contain* the LLM's authority. A deterministic goal generator using LLM-proposed candidates and an LLM-free acceptance rule typically performs *better* than either alone, because the LLM contributes fluency and the LLM-free rule contributes consistency.

### 8.4 "Real-World Agents Are All LLM-Wrappers and Seem to Work"

**Objection.** Major frameworks ship LLM-wrapper agents and users are satisfied.

**Response.** Most deployed agents are L1 or low-L2 in the MSCP taxonomy: they execute tools, hold short conversations, and reset between sessions. At this autonomy level the LLM-wrapper pattern is acceptable, because the agent has no persistent self-model that LLM noise can corrupt. The frameworks "work" because the bar is "complete a single user request." As autonomy demands rise - persistent goals, multi-day reasoning, self-modification - the LLM-wrapper pattern fails in the predictable ways enumerated in §1.2.

### 8.5 "PLA Is Just Re-Inventing Symbolic AI"

**Objection.** "LLM-free decision authority" is a fancy term for GOFAI rule engines, which lost to neural networks for good reasons.

**Response.** PLA does not require symbolic mechanisms. Many LLM-free modules in §6 are themselves learned (embedding spaces, calibrated classifiers, retrieval networks). The constraint is on *authority*, not on *representation*. PLA is post-LLM, not pre-LLM: it asks "now that we have LLMs, where do we put their outputs in the agent's decision pipeline?" The answer "everywhere" (LLM-wrapper) and the answer "nowhere" (symbolic purism) are both wrong; PLA stages chart the answer in between.

---

## 9. Relation to Existing Documents

This paper is a stand-alone rationale. Its claims are anchored in the following MSCP documents:

| MSCP document | What it provides | How this paper uses it |
|---------------|------------------|------------------------|
| [Overview §3.1](../MSCP_Overview.md) - Lessons from Early Prototyping | MSCP v0.4 finding: LLM self-reflection is unreliable | §1.2 (F4) and §8.1 cite this directly as evidence for authority separation |
| [Overview §4.4](../MSCP_Overview.md) - Named Architectural Concepts | Introduces AGI Engine, PLA stages, LangNet | §5 expands the PLA stage table; §6 builds on LangNet |
| [Overview §2.5](../MSCP_Overview.md) - Key Thresholds Across Levels | Numerical thresholds (prediction error, ASS freeze, OMI) | §4 maps each threshold to its LLM-free enforcer |
| [Glossary](MSCP_Glossary.md) | Canonical definitions and acronym list | §3 introduces the LAG acronym registered there |
| [L2 §1.7](../levels/Level_2_Autonomous_Agent.md) - Conversation Context | $\mathcal{C}_{\text{conv}}$ structure | §5.2 Stage 1 transition trigger |
| [L3 §3.1, §3.3](../levels/Level_3_Self_Regulating_Agent.md) | Core loop, prediction gating | §1.2 (F4), §4, §5.3 |
| [L3 §4](../levels/Level_3_Self_Regulating_Agent.md) - Identity & Safety | Identity vector, delta clamp, ethical kernel | §1.2 (F2), §2.4, §4 |
| [L4 §4, §6, §8](../levels/Level_4_Adaptive_General_Agent.md) | CDTS, capability expansion, bounded self-modification | §4, §5.4 |
| [L4.5 §3, §5, §7](../levels/Level_4_5_Self_Architecting.md) | Self-projection, parallel frames, existential guard | §5.5 |
| [L4.8 §1.5](../levels/Level_4_8_Strategic_Self_Modeling.md) | Probabilistic world modeling, confidence calibration | §4, §5.5 |
| [L4.9 §1.6, §3.6](../levels/Level_4_9_Autonomous_Strategic_Agent.md) | ASS freeze gate, goal conflict resolution | §4 |
| [L5 §1.6](../levels/Level_5_Proto_AGI.md) - F-phases | Autonomous research loop, value-evolution audit | §5.6 |

---

## 10. Open Questions (Research Frontier)

The PLA framework leaves the following open. Each is an invitation, not a roadmap.

**(Q1) How is LAG measured in practice?** Definition 2 (§3.1) is principled but requires sampling $p_{\text{LLM}}$ and $p_{\text{agent}}$ at scale. A practical proxy - e.g., per-decision behavioral divergence under fixed seed perturbation - would be useful.

**(Q2) Can Stage 4 → Stage 5 transition be automatically certified?** The Stage 5 requirement that "the autonomous research loop F4 closes without operator intervention" is hard to verify ex ante. Is there an offline test bench that captures it?

**(Q3) Adversarial PLA-stage downgrade.** Can an attacker who can write to the agent's input channel cause its certified PLA stage to be revoked (and the agent to fall back to LLM-wrapper behavior)? What is the threat model?

**(Q4) Multi-agent PLA inference.** When agents at different PLA stages cooperate (L5 §7), can a higher-stage agent reliably infer the PLA stage of a lower-stage agent it is interacting with? Mis-estimation in either direction has safety consequences.

**(Q5) PLA stage and human oversight.** As PLA stage rises, the human operator's effective oversight capacity stays constant. What is the maximum PLA stage at which "human in the loop" is still meaningful, and what monitoring mechanisms substitute beyond it?

**(Q6) LLM-free novelty.** Stage 5 demands genuinely novel research output. The mechanisms in §6 are bounded (templates have authors, LangNet adaptations specialize existing strategies, embedding arithmetic operates on known concepts). What is the *upper bound* on novelty achievable by LLM-free synthesis, and does it suffice for the open-world demands of L5?

---

## 11. Conclusion

LLM-free PLA is not *anti-LLM*. It is *post-LLM* - a discipline for using LLMs at the right place in the agent's decision pipeline, namely as artifact producers under deterministic authority. Every MSCP safety mechanism that separates one level from the next is an instance of this discipline. Climbing the MSCP ladder is therefore exactly the engineering project of building LLM-free authority while preserving LLM-driven fluency. PLA names the stages of that project. AGI Engine orchestrates them. LangNet stores their cross-domain artifacts. Together they answer the design question that LLM-wrapper agents leave unanswered: **who is the subject of the agent's cognition, and on what substrate does that subject reside?**

The MSCP answer is that the subject is the agent itself, and the substrate is the union of all LLM-free mechanisms the agent has had to build in order to be one.
