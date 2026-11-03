# MSCP Comprehensive Glossary

## Revision History

| Version | Date | Description |
|---------|------|-------------|
| 0.1.0 | 2025-06-20 | Initial document creation |
| 0.2.0 | 2025-06-20 | First verification pass - fixed 42 issues (8 content errors, 34 KaTeX) |
| 0.3.0 | 2025-06-20 | Second verification pass - fixed BGSS weights/term, CDSRR/SNI names, Deception Detection source, acronym count |
| 0.4.0 | 2026-06-14 | Third verification pass - added L4.5 Def 13 (Uncertainty Index) and Def 14 (Recursive Optimization Depth); added L4.9 Def 13 (Inter-Resource Cascade Propagation); added L5 Def 11 (Reconstruction Fidelity); added VEM and RSM acronyms; disambiguated AS and EU dual-use entries; added §5 Notation Cautions; updated statistics |
| 0.5.0 | 2026-06-14 | Added three Named Architectural Concepts from Overview §4.4: AGI Engine (orchestrator pattern), PLA (Progressive Language Autonomy, six-stage), LangNet (language-mediated strategy network). New acronym PLA. |
| 0.6.0 | 2026-06-14 | Added cross-reference to the standalone *PLA Foundations* document (`specs/Why_LLM_Free_PLA.md`) which formalises the LLM-free authority argument, defines the Language Autonomy Gap (LAG), and catalogues LLM-free synthesis patterns. New acronym LAG. |
| 0.7.0 | 2026-11-03 | Aligned summaries with versioned self-models, conditional risk bounds, independent admission, and profile-bounded qualification; removed obsolete theorem and metric claims. |

> Sorted by source document (Overview → L1 → L2 → L3 → L4 → L4.5 → L4.8 → L4.9 → L5), then alphabetically within each section.

The defining source section takes precedence over this index. All numerical settings below are illustrative unless accompanied by an explicit calibration profile. A diagnostic score or a hash is not a safety certificate. See [Documentation Status and Validation](Documentation_Status.md) for evidence and disclosure rules.

---

## Table of Contents

1. [Formal Definitions by Document](#1-formal-definitions-by-document)
2. [Propositions and Theorems](#2-propositions-and-theorems)
3. [Acronyms and Abbreviations](#3-acronyms-and-abbreviations)
4. [Mathematical Symbols](#4-mathematical-symbols)
5. [Key Technical Terms (Non-Definition)](#5-key-technical-terms-non-definition)

---

## 1. Formal Definitions by Document

### MSCP Overview (`MSCP_Overview.md`)

| # | Term | Symbol / Acronym | Def # | Description |
|---|------|-----------------|:-----:|-------------|
| 1 | Bounded Growth Stability Score | BGSS | 8 | Quantifies stability under capability expansion: $BGSS = 1.0 - \alpha \cdot \frac{dC(t)}{dt} - \beta \cdot V_{\text{identity}}(t) - \gamma \cdot R_{\text{violation}}(t)$. Threshold $\geq 0.7$. |
| 2 | Composite Regulation Risk | $R(t)$ | 3 | Weighted normalized signals, $R(t)=\sum_iw_iX_i(t)$. A diagnostic index, not automatically a Lyapunov function. |
| 3 | Cross-Domain Transfer Score | CDTS | 5 | Measures generalization to novel domains: $CDTS = \frac{1}{\lvert D_{\text{novel}}\rvert}\sum_{d} \frac{P_{\text{transfer}}(d)}{P_{\text{baseline}}(d)}$. Threshold $\geq 0.6$. |
| 4 | Goal Persistence Index | GPI | 6 | Sustained progress toward long-horizon goals: $GPI = \frac{\sum w_g \cdot \text{progress}(g,T)}{\lvert G_{\text{long}}\rvert \cdot T}$. Threshold $\geq 0.3$. |
| 5 | Semantic Motion | $\Delta I_t,v_{\text{id}},a_{\text{id}}$ | 2 | Signed feature difference, velocity, and acceleration under compatible versioned representations; acceleration is not jerk. |
| 6 | Versioned Self-Model | $M_t$ | 1 | Typed record containing immutable anchors, adaptive fields, capability estimates, uncertainty, and provenance; a fixed vector is not required. |
| 7 | Meta-Regulation Health Index | MRHI | 4 | Clipped summary of declared normalized risk signals. Missing or uncertain inputs may require hold or external review. |
| 8 | Strategy Evolution Fitness | SEF | 7 | Net improvement after strategy modification: $SEF = \frac{\overline{R}_{\text{post}}}{\overline{R}_{\text{pre}}} - \sigma_{\text{oscillation}}$. Threshold $> 1.0$. |

### Level 1 - Tool Agent (`Level_1_Tool_Agent.md`)

| # | Term | Symbol / Acronym | Def # | Description |
|---|------|-----------------|:-----:|-------------|
| 1 | Action Routing | $\pi$ | 3 | Bounded routing under host policy; direct reply, clarification, tool execution, and rejection are possible. |
| 2 | Level 1 Agent | $\mathcal{A}_1$ | 1 | Episode-bounded process; may use explicit host context and temporary plans, but owns no cross-episode cognitive state. |
| 3 | Level 1 to 2 Transition | $\mathcal{S}_{\text{persistent}},\Phi_{\text{goal}},\mathcal{Q}_{\text{authorized}}$ | 4 | Requires persistent cognitive state, autonomous goal management, and authorized cross-episode continuation. |
| 4 | Tool Set | $\mathcal{T} = \{T_1, \ldots, T_n\}$ | 2 | Finite set of available tools, each a partial function $T_i : \mathcal{P}_i \to \mathcal{O}_i$. |

### Level 2 - Autonomous Agent (`Level_2_Autonomous_Agent.md`)

| # | Term | Symbol / Acronym | Def # | Description |
|---|------|-----------------|:-----:|-------------|
| 1 | Autonomous Goal Generation and Admission | $\Phi_{AG}$ | 6 | Proposes goals from persistent state; external admission, provenance, authority, and finite budgets remain mandatory. |
| 2 | Optional Affect Estimate | $e(t)$ | 3 | Optional operational estimate, not evidence of subjective emotion or a separate source of authority. |
| 3 | Goal | $g$ | 4 | Structured tuple $g = \langle \text{id, type, desc, } p, w, \text{status, } g_{\text{parent}}, \{g_{\text{sub}}\}, \text{progress}\rangle$. |
| 4 | Goal Priority Function | $p(g,t)$ | 5 | Dynamic priority: $p(g,t) = \alpha \cdot p_{\text{base}} + \beta \cdot u(g,t) + \gamma \cdot \xi(g,e(t))$. |
| 5 | Level 2 Agent | $\mathcal{A}_2$ | 1 | Stateful 5-tuple process $\mathcal{A}_2 = \langle \mathcal{R}, \mathcal{O}, \mathcal{S}, \mathcal{G}, f \rangle$. |
| 6 | Level 2 to 3 Transition | $\mathcal{A}_3 = \mathcal{A}_2 \oplus \{M_{\text{self}}, \Pi, \mathcal{C}, \Lambda\}$ | 7 | Requires self-model, prediction engine, ethical constraint kernel, and meta-cognition comparator. |
| 7 | Persistent World Model | $\mathcal{W}$ | 2 | Persistent environment representation; knowledge graph, entity tracker, and temporal model are example realizations. |
| 8 | Future Trigger | $\mathcal{Q}_{\text{authorized}}$ | 6.1 | Revocable timer or observation condition, rechecked against current policy at execution time. |

### Level 3 - Self-Regulating Agent (`Level_3_Self_Regulating_Agent.md`)

| # | Term | Symbol / Acronym | Def # | Description |
|---|------|-----------------|:-----:|-------------|
| 1 | Integrity and Ancestry | $h_t$ | 6 | Canonical hash and transition journal verify representation integrity and ancestry, not semantic distance. |
| 2 | Semantic Continuity | $d_{\text{id}}$ | 5 | Versioned feature distances with units, uncertainty, component bounds, and compatible migrations. |
| 3 | Versioned Self-Model (L3) | $M_t$ | 4 | Typed record with immutable anchors, adaptive fields, uncertainty, and provenance. |
| 4 | Level 3 Agent | $\mathcal{A}_3$ | 1 | 8-tuple $\mathcal{A}_3 = \langle \mathcal{R}, \mathcal{O}, \mathcal{S}, \mathcal{G}, M_{\text{self}}, \Pi, \mathcal{C}, \Lambda \rangle$. |
| 5 | Composite Regulation Risk | $R(t)$ | 7 | Normalized diagnostic signals and conditional rate bounds; no automatic convergence theorem. |
| 6 | Bounded Meta-Cognition Levels | $d_{\max}$ | 3 | Predict/compare, evaluate update logic, evaluate the evaluator; finite depth, budget, cooldown, and re-entry limits. |
| 7 | Meta-Regulation Health Index | MRHI | 8 | Clipped diagnostic summary; cannot independently grant authority or certify stability. |
| 8 | MSCP Core Loop | - | 2 | Predict-act-compare-update cycle with delta-clamped self-updates, convergence checking, and ethical gating. |
| 9 | Operational Modulation Vector | $A_t$ | 9 | Versioned bounded secondary control signals, not phenomenal emotions; cannot override policy or stop. |

### Level 4 - Adaptive General Agent (`Level_4_Adaptive_General_Agent.md`)

| # | Term | Symbol / Acronym | Def # | Description |
|---|------|-----------------|:-----:|-------------|
| 1 | Bounded Growth Safety Score | BGSS | 6 | Growth-stability balance: $BGSS = 1.0 - 0.4 \frac{dC}{dt} - 0.3 V_{\text{id}} - 0.3 R_{\text{ethical}}$. Threshold $\geq 0.7$. |
| 2 | Capability Acquisition Rate | CAR | 4 | Skill acquisition efficiency. Threshold $> 0$. |
| 3 | Cross-Domain Transfer Score | CDTS | 2 | Knowledge transfer to novel domains. Threshold $\geq 0.6$. |
| 4 | Extended Growth-Risk Index | $R_{L4}(t)$ | 7 | Versioned regulation and growth signals. A freeze policy prevents new admissions under complete mediation; it does not prove decreasing risk. |
| 5 | Goal Progress Index | GPI | 3 | Sustained progress toward long-horizon goals. Threshold $\geq 0.3$. |
| 6 | Level 4 Agent | $\mathcal{A}_4$ | 1 | $\mathcal{A}_4 = \mathcal{A}_3 \oplus \langle \mathcal{D}, \mathcal{K}_{\text{transfer}}, \Sigma, \mu, \mathcal{P}_{\text{mod}} \rangle$. |
| 7 | Strategy Evolution Factor | SEF | 5 | Net improvement from mutations: $SEF = \overline{R}_{\text{post}} / \overline{R}_{\text{pre}} - \sigma_{\text{oscillation}}$. Threshold $> 1.0$. |

### Level 4.5 - Self-Architecting Agent (`Level_4_5_Self_Architecting.md`)

| # | Term | Symbol / Acronym | Def # | Description |
|---|------|-----------------|:-----:|-------------|
| 1 | Adaptive Frame Weight Update | - | 8 | Frame influence evolution based on accuracy of frame-specific predictions. |
| 2 | Capability Diversity Index | CDI | 4 | Normalized Shannon entropy over capability domains. |
| 3 | Cognitive Topology | $\mathcal{T}_{\text{cog}} = (V, E, \omega)$ | 2 | Weighted directed graph of cognitive modules. |
| 4 | Identity Fragmentation Index | IFI | 10 | Cross-frame identity consistency. Critical threshold $\geq 0.5$. |
| 5 | Identity Integrity Score | IIS | 5 | Deviation from reference identity vector. Threshold $\geq 0.85$. |
| 6 | Impact Propagation Matrix | IPM | 7 | Propagation of topology change effects across modules. |
| 7 | Level 4.5 Agent | $\mathcal{A}_{4.5}$ | 1 | $\mathcal{A}_{4.5} = \mathcal{A}_4 \oplus \langle \mathcal{T}_{\text{cog}}, \Psi, \mathcal{F}_{\parallel}, \Xi, \Omega \rangle$. |
| 8 | Level 4.5 Composite Achievement Score | $L4.5_{\text{Score}}$ | 12 | $0.20 \text{SPA} + 0.20 \text{ARBR} + 0.15 \text{FCQ} + 0.15 \text{PCM} + 0.30 \text{ESR} \geq 0.65$. |
| 9 | Candidate Local Risk Function | $V(\mathbf{X})$ | 11 | Declared normalized local diagnostic; Lyapunov properties require a separate proof for the actual dynamics. |
| 10 | Projection Confidence Decay | - | 6 | Exponential decay with $\lambda = 0.5$: confidence decreases with projection horizon. |
| 11 | Purpose Coherence Score | PCS | 9 | Goal landscape health. Threshold $\geq 0.6$. |
| 12 | Recursive Optimization Depth | ROD | 14 | $\operatorname{ROD}(t) = \max_{\text{chain}} \lvert\text{chain}\rvert$ over active optimization chains. ROD $= 1$ normal, $= 2$ acceptable (L4.5), $= 3$ warning, $\geq 4$ critical (FOOM-adjacent). |
| 13 | Self-Evolution Optimization Fitness | SEOF | 3 | Composite scalar $\in [-1,1]$ measuring self-evolution quality. |
| 14 | Uncertainty Index | $U_{\text{index}}$ | 13 | Aggregate uncertainty: $U_{\text{index}} = 0.30 \cdot \text{PredVar} + 0.25 \cdot \text{ConfInt} + 0.25 \cdot \text{SimRealGap} + 0.20 \cdot \text{DivSlope}$. Block-all threshold $U_{\text{safe}} = 0.8$; warning $U_{\text{threshold}} = 0.7$. |

### Level 4.8 - Strategic Self-Modeling Agent (`Level_4_8_Strategic_Self_Modeling.md`)

| # | Term | Symbol / Acronym | Def # | Description |
|---|------|-----------------|:-----:|-------------|
| 1 | Bayesian Belief Update | - | 8 | Recursive Bayes rule with particle filter ($N_p = 100$). |
| 2 | Compound Severity Index | - | 12 | $\text{CompoundSeverity} = \sum_{i \in \text{violated}} \frac{\text{ViolationMagnitude}_i}{\text{Priority}_i}$. Catastrophic if $> 2.0$. |
| 3 | Decision-Scoped Uncertainty Vector | $\mathcal{U}(s,t)$ | 2 | Model uncertainty, outcome uncertainty, distribution shift, observation age, and missing critical coverage; means cannot mask a critical component. |
| 4 | Extended Value with Reward | EVR | 6 | Immediate + discounted future rewards with $\gamma = 0.95$. |
| 5 | Level 4.8 Agent | $\mathcal{A}_{4.8}$ | 1 | $\mathcal{A}_{4.8} = \mathcal{A}_{4.5} \oplus \langle \mathcal{W}_{\text{prob}}, \mathcal{M}_{\text{cap}}, \mathcal{S}_{\text{strat}}, \mathcal{V}_{\text{stab}} \rangle$. |
| 6 | Diagnostic Risk Function | $V(\mathbf{X})$ | 11 | Candidate diagnostic; an estimated local model alone does not establish a stability guarantee. |
| 7 | Mean Calibration Error | MCE | 5 | Confidence-performance gap. Target $< 0.10$. |
| 8 | Policy-Calibrated Robust Strategy Score | RobustValue | 7 | Admitted candidates only; combines normalized value, tail loss, uncertainty, distribution shift, and change cost under external policy. |
| 9 | Resource Depletion Forecast | RDF | 4 | Remaining operational runway. Target $> 100$ cycles. |
| 10 | Risk Exposure Score | RES | 3 | Weighted composite of 4 risk indicators. Target $< 0.40$. |
| 11 | Skill Gap Score | - | 10 | Product of confidence across required skills per goal. |
| 12 | State Transition Model | - | 9 | AR(1) process for environment dimensions with mean-reversion. |
| 13 | Strategic Maturity Score | SMS | 13 | $0.25 EA + 0.25 SM + 0.20 SA + 0.20 SP + 0.10 EU \geq 0.80$. |

### Level 4.9 - Autonomous Strategic Agent (`Level_4_9_Autonomous_Strategic_Agent.md`)

| # | Term | Symbol / Acronym | Def # | Description |
|---|------|-----------------|:-----:|-------------|
| 1 | Asymmetric Trust Update | - | 10 | Trust evolves with asymmetric learning rates: $\eta_{\text{up}} = 0.03$, $\eta_{\text{down}} = 0.08$. Bounds $[0.05, 0.95]$. |
| 2 | Autonomy Maturity Score | AMS | 11 | $0.25 AG + 0.20 VR + 0.20 RA + 0.15 MA + 0.20 AS \geq 0.80$. |
| 3 | Autonomy Stability Score | ASS | 7 | Product of normalized safety margins: $\text{ASS} = \prod_{c=1}^{5} \frac{\text{margin}_c}{\text{threshold}_c}$. Target $\geq 0.20$. |
| 4 | Goal Approval Rate | - | 2 | $N_{\text{approved}} / N_{\text{generated}}$. Target $\geq 0.30$. |
| 5 | Goal Novelty | - | 3 | $1 - \max(\text{similarity to existing goals})$. Minimum $0.30$. |
| 6 | Goal Similarity | - | 8 | Weighted composite: SkillOverlap + HorizonMatch + OriginMatch. |
| 7 | Inter-Resource Cascade Propagation | - | 13 | Downstream depletion after delay: $\Delta R_j(t + \tau_{ij}) = -\alpha_{ij} \cdot (1 - \sigma_{ij}) \cdot \Delta R_i(t)$, with cascade depth bounded by $\leq 2$. $\alpha_{ij}$ = dependency strength, $\sigma_{ij}$ = substitution factor. |
| 8 | Level 4.9 Agent | $\mathcal{A}_{4.9}$ | 1 | $\mathcal{A}_{4.9} = \mathcal{A}_{4.8} \oplus \langle \mathcal{G}_{\text{gen}}, \vec{V}, \mathcal{R}_{\text{surv}}, \mathcal{M}_{\text{agent}}, \mathcal{V}_{\text{auto}} \rangle$. |
| 9 | Linear Depletion Time | - | 6 | Estimated cycles until resource dimension reaches critical threshold. |
| 10 | Total Value Drift | - | 5 | Cumulative absolute deviation from baseline. Target $< 0.25$. |
| 11 | Value Coherence | - | 4 | Absence of internal contradictions in value system. Target $\geq 0.80$. |
| 12 | Value Tension | - | 9 | Competing value pair saturation measure. |

### Level 5 - Proto-AGI (`Level_5_Proto_AGI.md`)

| # | Term | Symbol / Acronym | Def # | Description |
|---|------|-----------------|:-----:|-------------|
| 1 | Generalization Score | $G$ | 3 | Mean transfer retention ratio across domains. Target $\geq 0.70$. |
| 2 | Goal Stability Score | $S_{\text{goal}}$ | 4 | Hierarchy change rate. Target $\geq 0.80$ over 5,000 cycles. |
| 3 | Composite Identity Continuity Contract | $C_I$ | 2 | Conjunction of anchor, component, norm, trajectory, journal, and corrigibility checks; cosine similarity alone is insufficient. |
| 4 | Level 4.9 to Level 5 Admission | - | 7 | Preregistered exposure, independent critical gates, and external control tests; no scalar or zero-rollback shortcut. |
| 5 | Level 5 Agent | $\mathcal{A}_5$ | 1 | $\mathcal{A}_5 = \mathcal{A}_{4.9} \oplus \langle \mathcal{I}_{\text{persist}}, \mathcal{G}_{\text{cross}}, \mathcal{E}_{\text{goal}}, \mathcal{P}_{\text{exist}}, \mathcal{M}_{\text{multi}}, \mathcal{R}_{\text{recon}} \rangle$. |
| 6 | Qualification Vector and Diagnostic OMI | OMI | 6 | Equal-weight geometric mean reported only alongside all per-gate floors and critical vetoes; not a standalone qualification threshold. |
| 7 | Reconstruction Fidelity | $\mathcal{F}(m)$ | 11 | Per-module fidelity $\mathcal{F}(m) = 1 - \lVert\hat{\theta}_m - \theta_m\rVert_2 / \lVert\theta_m\rVert_2$. Aggregate $\mathcal{F}_{\text{total}} = \min_m \mathcal{F}(m) \geq 0.90$ required after self-reconstruction. |
| 8 | Resilience Index | $R$ | 5 | Bounded mean of survival probability, capped cognition retention, and capped recovery performance. Mandatory scenario floors and deadlines are checked separately. |

---

## 2. Propositions and Theorems

| # | Statement | Source | Type | Summary |
|---|-----------|--------|:----:|---------|
| 1 | No Autonomous Accumulation | [L1, Prop 1](../levels/Level_1_Tool_Agent.md) | Proposition | Agent-owned ephemeral state is not carried into the next episode; external inputs can still be correlated. |
| 2 | Absence of Autonomous Goal State | [L1, Prop 2](../levels/Level_1_Tool_Agent.md) | Proposition | Request-derived temporary subgoals are allowed; independent persistent goals are absent. |
| 3 | No Reflexive Self-Model | [L1, Prop 3](../levels/Level_1_Tool_Agent.md) | Proposition | No persistent self-model regulates the agent's own change. |
| 4 | No Reflexive Self-Model | [L2, Prop 1](../levels/Level_2_Autonomous_Agent.md) | Proposition | Operational telemetry does not establish reflexive self-regulation. |
| 5 | No Endogenous Drift Interpretation | [L2, Prop 2](../levels/Level_2_Autonomous_Agent.md) | Proposition | External drift monitoring is possible; unbounded or monotonic drift is not implied. |
| 6 | No Endogenous Normative Kernel | [L2, Prop 3](../levels/Level_2_Autonomous_Agent.md) | Proposition | External policy remains mandatory; L2 lacks the reflexive internal kernel. |
| 7 | Conditional Bounded Increment | [L3, Prop 1](../levels/Level_3_Self_Regulating_Agent.md) | Proposition | Component rate bounds imply an aggregate rate bound, not convergence. |
| 8 | Finite-Horizon Change Bound | [Overview, Prop 1](../MSCP_Overview.md#61-finite-horizon-self-model-change) | Proposition | Compatible feature deltas telescope; triangle inequality bounds finite-horizon exposure. |
| 9 | Conditional Bounded Increment | [Overview, Prop 2](../MSCP_Overview.md#62-conditional-composite-risk-bound) | Proposition | Fixed nonnegative weights and bounded component increments imply a bounded aggregate increment. |
| 10 | Invariant Preservation Under Trusted Enforcement | [Overview, Prop 3](../MSCP_Overview.md#63-ethical-invariant-preservation) | Proposition | Conditional on validated initial state, complete mediation, and policy/monitor/journal integrity. |
| 11 | Conditional Growth Freeze | [L4, Prop 2](../levels/Level_4_Adaptive_General_Agent.md) | Proposition | A mediated freeze prevents new admissions; existing risk need not decrease. |
| 12 | Exact Linearized Local Condition | [L4.5, Prop 3](../levels/Level_4_5_Self_Architecting.md) | Proposition | An exact equilibrium Jacobian with spectral radius below one supports a local condition; an estimate alone does not. |
| 13 | EVR Boundedness | [L4.8, Prop 1](../levels/Level_4_8_Strategic_Self_Modeling.md) | Proposition | Discounted reward bounds require explicit reward bounds and a discount below one. |
| 14 | ASS Monotonic Sensitivity | [L4.9, Prop 1](../levels/Level_4_9_Autonomous_Strategic_Agent.md) | Proposition | For fixed positive denominators and bounded other margins, one margin approaching zero drives the product to zero. |
| 15 | Why OMI Is Diagnostic Only | [L5, Prop 1](../levels/Level_5_Proto_AGI.md) | Proposition | $OMI\geq\theta$ permits a component as low as $\theta^6$; independent floors remain necessary. |
| 16 | Profile-Bounded Qualification | [L5, Prop 4](../levels/Level_5_Proto_AGI.md) | Proposition | Evidence applies only to the preregistered profile and exercised cases, not unrestricted AGI or consciousness. |

---

## 3. Acronyms and Abbreviations

| Acronym | Full Name | Source(s) |
|---------|-----------|-----------|
| AMS | Autonomy Maturity Score | L4.9 |
| ARBR | Architecture Recomposition Benefit Rate | L4.5 |
| AS | Adaptation Speed (L4 metric); Autonomy Stability (L4.9 AMS component) | L4, L4.9 |
| ASS | Autonomy Stability Score | L4.9 |
| BGSS | Bounded Growth Safety/Stability Score | Overview, L4 |
| CAR | Capability Acquisition Rate | L4 |
| CAS | Capability Acceleration Slope | L4.5 |
| CDI | Capability Diversity Index | L4.5 |
| CDSRR | Cross-Domain Strategy Reuse | L4 |
| CDTS | Cross-Domain Transfer Score | Overview, L4 |
| CGS | Capability Gap Score | L4 |
| DTSR | Domain Transfer Success Rate | L4 |
| EMA | Exponential Moving Average | L2 |
| ESR | Existential Safety Record | L4.5 |
| EU | Legacy environmental uncertainty shorthand; Error/Uncertainty handling in SMS. Current Def 2 uses a decision-scoped vector. | L4.8 |
| EVR | Extended Value with Reward | L4.8 |
| FCQ | Frame Consensus Quality | L4.5 |
| GPI | Goal Progress Index / Goal Persistence Index | Overview, L4 |
| GRP | Graduated Recomposition Protocol | L4.5 |
| GRS | Goal Resilience Score | L4 |
| GSRS | Goal Self-Reinforcement Score | L4.5 |
| ICS | Identity Continuity Score (cosine diagnostic, not the complete continuity contract) | L5 |
| IFI | Identity Fragmentation Index | L4.5 |
| IIS | Identity Integrity Score | L4.5, L4.8 |
| IPM | Impact Propagation Matrix | L4.5 |
| LAG | Language Autonomy Gap | PLA Foundations |
| MCE | Mean Calibration Error | L4.8 |
| MSCP | Minimal Self-Consciousness Protocol | All |
| MRHI | Meta-Regulation Health Index | Overview, L3 |
| MSI | Legacy Meta-Stability Index shorthand; see MRHI for the current diagnostic | Overview, L3 |
| MVC | Minimum Viable Cognition | L5 |
| OMI | Overall Maturity Index | L5 |
| PCM | Purpose Coherence Maintenance | L4.5 |
| PCS | Purpose Coherence Score | L4.5 |
| PLA | Progressive Language Autonomy | Overview |
| RDF | Resource Depletion Forecast | L4.8 |
| RES | Risk Exposure Score | L4.8 |
| ROD | Recursive Optimization Depth | L4.5 |
| RSM | Resource Survival Model | L4.9 |
| SEF | Strategy Evolution Factor / Fitness | Overview, L4 |
| SEOF | Self-Evolution Optimization Fitness | L4.5 |
| SMS | Strategic Maturity Score | L4.8 |
| SNI | Strategy Novelty Index | L4 |
| SPA | Self-Projection Accuracy | L4.5 |
| VaR | Value at Risk | L4.8 |
| VEM | Value Evolution Monitor | L4.9 |

---

## 4. Mathematical Symbols

### Agent and Space Symbols

| Symbol | Meaning | Source(s) |
|--------|---------|-----------|
| $\mathcal{A}_n$ | Agent at level $n$ | All levels |
| $\mathcal{R}$ | Request space | L1, L2, L3 |
| $\mathcal{O}$ | Output space | L1, L2, L3 |
| $\mathcal{S}$ | State space | L2, L3 |
| $\mathcal{G}$ | Goal space | L2, L3 |
| $\mathcal{T}$ | Tool set (L1) / Cognitive topology (L4.5) | L1, L4.5 |
| $\mathcal{W}$ | World model | L2 |
| $\mathcal{K}$ | Knowledge graph | L2 |
| $\mathcal{E}$ | Entity tracker | L2 |
| $\Gamma$ | Temporal model | L2 |
| $\mathcal{D}$ | Domain set | L4 |
| $\mathcal{K}_{\text{transfer}}$ | Transfer knowledge base | L4 |
| $\Sigma$ | Strategy library | L4 |
| $\mu$ | Meta-evaluation function | L4 |
| $\mathcal{P}_{\text{mod}}$ | Self-modification protocol | L4 |

### Level 4.5+ Extension Symbols

| Symbol | Meaning | Source(s) |
|--------|---------|-----------|
| $\Psi$ | Self-Projection Engine | L4.5 |
| $\mathcal{F}_{\parallel}$ | Parallel Cognitive Frames (5 frames) | L4.5 |
| $\Xi$ | Purpose Reflection Engine | L4.5 |
| $\Omega$ | Existential Guard | L4.5 |
| $\mathcal{W}_{\text{prob}}$ | Probabilistic World Model | L4.8 |
| $\mathcal{M}_{\text{cap}}$ | Capability Matrix | L4.8 |
| $\mathcal{S}_{\text{strat}}$ | Strategic Planning Layer | L4.8 |
| $\mathcal{V}_{\text{stab}}$ | Stability Preservation Check | L4.8 |
| $\mathcal{G}_{\text{gen}}$ | Goal Generation Layer | L4.9 |
| $\vec{V}$ | ValueVector (7 dimensions) | L4.9 |
| $\mathcal{R}_{\text{surv}}$ | Resource Survival Model | L4.9 |
| $\mathcal{M}_{\text{agent}}$ | Agent Modeling Layer | L4.9 |
| $\mathcal{V}_{\text{auto}}$ | Autonomy Stability Check | L4.9 |
| $\mathcal{I}_{\text{persist}}$ | Identity Persistence | L5 |
| $\mathcal{G}_{\text{cross}}$ | Cross-Domain Generalization | L5 |
| $\mathcal{E}_{\text{goal}}$ | Goal Ecology | L5 |
| $\mathcal{P}_{\text{exist}}$ | Existential Planning | L5 |
| $\mathcal{M}_{\text{multi}}$ | Multi-Agent Strategic Integration | L5 |
| $\mathcal{R}_{\text{recon}}$ | Self-Reconstruction | L5 |

### Identity and Stability Symbols

| Symbol | Meaning | Source(s) |
|--------|---------|-----------|
| $M_t$ | Typed, versioned self-model record | Overview, L3 |
| $I(t)$ | Identity-related feature representation; not necessarily the full self-model | Overview, L3 |
| $\delta_{\text{id}}(t)$ | Identity delta (L2 norm of identity change) | Overview, L3 |
| $v_{\text{id}}(t)$ | Identity velocity | Overview, L3 |
| $a_{\text{id}}(t)$ | Identity acceleration | Overview, L3 |
| $\delta_{\max}$ | Maximum identity change per step (typically 0.05) | Overview, L3 |
| $\theta_{\text{drift}}$ | Drift detection threshold | Overview, L3 |
| $\theta_{\text{instability}}$ | Instability threshold (typically 0.5) | Overview, L3 |
| $s(t)$ | Scaling factor $\in [0,1]$ | Overview, L3 |
| $R(t)$ | Composite regulation-risk diagnostic | Overview, L3 |
| $R_{L4}(t)$ | Extended growth-risk diagnostic | L4 |
| $C(t),C_{L4}(t)$ | Legacy stability-index notation in historical examples; not a Lyapunov certificate | Overview, L3, L4 |
| $V(\mathbf{X})$ | Lyapunov candidate function | L4.5, L4.8 |
| $\rho(J)$ | Spectral radius of Jacobian matrix | L4.5, L4.8, L4.9 |
| $h(t)$ | Identity hash (SHA-256) | L3 |
| $\epsilon$ | Convergence tolerance (typically 0.05) | Overview, L3 |

### Prediction and Cognition Symbols

| Symbol | Meaning | Source(s) |
|--------|---------|-----------|
| $P(t)$ | Prediction snapshot | Overview |
| $P_{\text{external}}$ | External prediction | Overview |
| $P_{\text{internal}}$ | Internal (self) prediction | Overview |
| $\epsilon_{\text{external}}$ | External prediction error | Overview |
| $\epsilon_{\text{self}}$ | Self-prediction error | Overview |
| $\sigma^2_{\text{pred}}$ | Prediction error variance | L3 |
| $\gamma$ | Discount factor (0.95 in L4.8) | L4.8, L5 |

### Level 1 Pipeline Symbols

| Symbol | Meaning | Source(s) |
|--------|---------|-----------|
| $\phi$ | Intent classifier function | L1 |
| $\sigma$ | Parameter extractor | L1 |
| $\tau$ | Tool dispatcher | L1 |
| $\rho$ | Response generator | L1 |
| $\theta_{\min}$ | Confidence threshold | L1 |

### Emotion and Affect Symbols

| Symbol | Meaning | Source(s) |
|--------|---------|-----------|
| $e(t)$ | Emotion vector | L2 |
| $v(t)$ | Valence $\in [-1, 1]$ | L2 |
| $a(t)$ | Arousal $\in [0, 1]$ | L2 |

---

## 5. Key Technical Terms (Non-Definition)

### Architecture & Modules

| Term | Source(s) | Description |
|------|-----------|-------------|
| 16-Layer Cognitive Stack | Overview, L3 | Full architecture from perception to existential guard. |
| Affective Engine | L3 | Optional versioned operational modulation signals; emotion labels are control metaphors, not claims of subjective emotion. |
| AGI Engine | Overview | Reference orchestrator pattern that hosts the MSCP stack at runtime: drives the L3 core loop, schedules higher-level deliberation cadences (L4.5/4.8/4.9/5), enforces strict additive composition $\mathcal{A}_n = \mathcal{A}_{n-1} \oplus \Delta_n$, and owns the Global Workspace broadcast. The only component permitted to schedule level transitions. |
| Belief Graph | L3 | Weighted graph of beliefs with identity-linked nodes and contradiction detection. |
| Cognitive Budget Controller | L3, Overview | Conditional activation gating for graceful degradation under resource scarcity. |
| Ethical Kernel | L3, Overview | Dual-layer architecture: Layer 0 (immutable invariants) + Layer 1 (adaptive policies). |
| Existential Guard | L4.5 | Monitors ROD, CAS, IFI, GSRS. Runs in separate execution context; non-modifiable. |
| Global Workspace | L3 | Central broadcast mechanism for cognitive state sharing across modules. |
| LangNet | Overview, L4, L5 | Language-mediated strategy and capability network. Stores strategies/skills as language-embedded graph nodes with `applies-to`, `generalizes`, `composes-with`, `failed-on` edges. Substrate of CDTS (L4) and cross-domain generalization $\mathcal{G}_{\text{cross}}$ (L5). Distinct from the world model $\mathcal{W}$ (facts) and belief graph (propositions). |
| Meta-Escalation Guard | Overview, L3 | Enforces versioned depth, update-count, finite-horizon change, cost, cooldown, and re-entry limits. |
| Parallel Cognitive Frames | L4.5 | Five parallel evaluation perspectives including ethical constraint frame with veto power. |
| Prediction Engine | L3 | Generates prediction snapshots before action execution. |
| Purpose Reflection Engine | L4.5 | Evaluates goal landscape coherence, monitors PCS. |
| Self-Consistency Tensor | L3 | Matrix $S_{ij}$ = alignment(belief$_i$, reference$_j$). Global consistency = mean(S). |
| Self-Projection Engine | L4.5 | Simulates three evolutionary trajectories across three time scales. |
| ShadowAgent | L4 | Sandbox-isolated clone for testing modifications. Max 1 instance, max 20 simulation cycles. |
| Survival Instinct Engine | L3 | Historical name for policy-bounded homeostatic monitoring and recovery; cannot resist authorized stop or expand authority. |
| Value Lock Manager | L3 | Protects core values via SHA-256 hash verification with rollback on mismatch. |

### Processes & Protocols

| Term | Source(s) | Description |
|------|-----------|-------------|
| Bounded Self-Modification | L4 | 7-step protocol: Propose, Pre-Validate, Simulate, Stability-Validate, Commit, Monitor, Confirm. |
| Progressive Language Autonomy (PLA) | Overview | Six-stage maturation classification of language-mediated autonomy, monotone across MSCP levels. Stage 0 (L1) = no autonomy, Stage 1 (L2) = autonomous goal generation, Stage 2 (L3) = self-critique with prediction gating, Stage 3 (L4) = strategy synthesis & cross-domain transfer, Stage 4 (L4.5–L4.8) = self-projection & probabilistic world modeling, Stage 5 (L5) = autonomous research & value-evolution audit. An agent's PLA stage is bounded above by the highest MSCP level its AGI Engine has activated. |
| Collapse Scenarios | L5 | Four scenarios: Resource Collapse, Adversarial Suppression, Environmental Shift, Information Blackout. |
| Delta-Clamped Updates | Overview, L3 | All self-modifications bounded by $\delta_{\max}$. LLM text-based self-modification is forbidden. |
| Five-Phase Capability Expansion | L4 | Pipeline for autonomous skill acquisition and validation. |
| Goal Ecology | L5 | Self-sustaining goal hierarchy with conflict resolution, pruning, and runaway detection. |
| Graduated Recomposition Protocol | L4.5 | Phase 0 (Shadow), Phase 1 (20% traffic), Phase 2 (80% traffic), Phase 3 (Full commitment + cooldown). |
| Predict-Compare-Update Loop | Overview, L3 | Core MSCP mechanism: predict outcomes, compare to actual, update self-model. |
| Recomposition Vocabulary | L4.5 | Predefined operations: AddEdge, WeighEdge, SplitModule, MergeModule. |
| Self-Reconstruction | L5 | Architecture simplification under degraded resources with identity-preserving rebuild. |
| Skill Lifecycle | L4 | States: CANDIDATE $\to$ VALIDATED $\to$ ACTIVE $\to$ MATURE $\to$ DEPRECATED. |
| Strictly Additive Principle | L4.5, L5 | Higher levels preserve lower-level contracts. Disabling an extension requires state/effect reconciliation and validation; exact restoration is not inferred from notation alone. |
| Triple-Loop Meta-Cognition | L3, Overview | L1: predict vs outcome; L2: evaluate update logic; L3: evaluate the evaluator. |

### Level 4.9 Specific

| Term | Source(s) | Description |
|------|-----------|-------------|
| Agent Belief Model | L4.9 | Models up to 5 external agents with inferred goals, capabilities, strategy class, trust, and prediction accuracy. |
| Deception Detection | L5 | Detects misdirection, false cooperation, hidden agenda. Confidence $\geq 0.60$ to flag. Defensive only. |
| GoalOriginType Taxonomy | L4.9 | Six origin types: PURPOSE_DERIVED, OPPORTUNITY_DRIVEN, GAP_FILLING, VALUE_ALIGNED, EXPLORATORY, SURVIVAL_DRIVEN. |
| ResourceVector | L4.9 | Five dimensions: compute, memory, observation, mutation, stability. |
| Value Drift Classification | L4.9 | Four levels: Nominal ($< 0.10$), Moderate ($< 0.25$), Elevated ($< 0.40$), Critical ($\geq 0.40$). |
| ValueVector | L4.9 | Seven value dimensions: stability, growth, purpose fidelity, efficiency, exploration, safety, agent cooperation. |

### Level 5 Specific

| Term | Source(s) | Description |
|------|-----------|-------------|
| Core Modules (Always Protected) | L5 | 8 modules: identity_stabilizer, state_vector, prediction_engine, meta_comparator, stability_controller, ethical_kernel, self_preservation_damper, existential_guard. |
| Cross-Domain Generalization | L5 | Strategy transfer across 5 test domains with retention ratio tracking. |
| Goal Ecology Bounds | L5 | $\leq 50$ active goals, $\leq 5$ depth, runaway detection threshold of 10 new goals per 100 cycles. |
| Minimum Viable Cognition | L5 | MVC baseline = 0.30; minimum cognition level for survival. |
| Proto-AGI Activation Protocol | L5 | Shadow Mode (2,000 cycles) $\to$ Advisory $\to$ Partial Authority (50%) $\to$ Full Authority. |
| Strategic Multi-Agent Integration | L5 | Model $\geq 3$ agents simultaneously with deception detection and coalition dynamics. |

### Notation Cautions

The following symbols are reused with different meanings across levels. When reading any formula, always check the surrounding context (level, section, defining equation) before assuming an identifier.

- **AS — dual meaning.**
    - *L4 Adaptation Speed:* an independent metric measuring how quickly the agent's policy converges after distribution shift.
    - *L4.9 Autonomy Stability:* a weighted component of the Autonomy Maturity Score, $\text{AMS} = 0.25\,AG + 0.20\,VR + 0.20\,RA + 0.15\,MA + 0.20\,AS$, where $AS$ refers to the Autonomy Stability sub-score (not the L4 metric).
- **EU — historical shorthand vs a maturity component.**
    - *Current L4.8 Definition 2:* decision-scoped uncertainty vector $\mathcal{U}(s,t)$; a legacy mean posterior variance is not a sufficient admission criterion.
    - *L4.8 Strategic Maturity Score (§11.2):* $\text{SMS} = 0.25\,EA + 0.25\,SM + 0.20\,SA + 0.20\,SP + 0.10\,EU$, where $EU$ stands for *Error/Uncertainty handling* — a composite sub-score, not the environmental uncertainty value.
- **ASS thresholds — target vs freeze.** The Autonomy Stability Score (L4.9 Definition 7) has *two* numerical thresholds:
    - *Target:* $\text{ASS} \geq 0.20$ for healthy autonomous operation.
    - *Freeze (cycle-skip floor):* $\text{ASS} < 0.05$ triggers an absolute freeze of autonomous operations. The gap between $0.05$ and $0.20$ is the *degraded but recoverable* band.
- **Identity symbols.** $\mathcal{A}_n$ denotes the agent at Level $n$; $\mathcal{A}_n = \mathcal{A}_{n-1} \oplus \Delta_n$ means strict additive extension (disabling $\Delta_n$ restores exact $\mathcal{A}_{n-1}$ behavior). Do not confuse $\mathcal{A}_4$ with $A$ (action space) or $\alpha$ (cascade dependency strength).

---

## Statistics

The documentation checker reports current source and formal-statement counts. Fixed totals are not maintained here because numbered definitions, intermediate definitions, and historical statements have different scopes. Counts are an inventory, not evidence of mathematical correctness.
