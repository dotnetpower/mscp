# MSCP Comprehensive Glossary

## Revision History

| Version | Date | Description |
|---------|------|-------------|
| 0.1.0 | 2025-06-20 | Initial document creation |
| 0.2.0 | 2025-06-20 | First verification pass - fixed 42 issues (8 content errors, 34 KaTeX) |
| 0.3.0 | 2025-06-20 | Second verification pass - fixed BGSS weights/term, CDSRR/SNI names, Deception Detection source, acronym count |

> Sorted by source document (Overview → L1 → L2 → L3 → L4 → L4.5 → L4.8 → L4.9 → L5), then alphabetically within each section.

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
| 1 | Bounded Growth Stability Score | BGSS | 8 | Quantifies stability under capability expansion: $BGSS = 1.0 - \alpha \cdot \frac{dC(t)}{dt} - \beta \cdot V\_{\text{identity}}(t) - \gamma \cdot R\_{\text{violation}}(t)$. Threshold $\geq 0.7$. |
| 2 | Composite Stability Function | $C(t)$ | 3 | Aggregates four volatility signals: $C(t) = w\_1 V\_{\text{identity}} + w\_2 H\_{\text{belief}} + w\_3 F\_{\text{goal}} + w\_4 V\_{\text{consistency}}$. Weights: 0.30, 0.25, 0.25, 0.20. |
| 3 | Cross-Domain Transfer Score | CDTS | 5 | Measures generalization to novel domains: $CDTS = \frac{1}{\lvert D\_{\text{novel}}\rvert}\sum\_{d} \frac{P\_{\text{transfer}}(d)}{P\_{\text{baseline}}(d)}$. Threshold $\geq 0.6$. |
| 4 | Goal Persistence Index | GPI | 6 | Sustained progress toward long-horizon goals: $GPI = \frac{\sum w\_g \cdot \text{progress}(g,T)}{\lvert G\_{\text{long}}\rvert \cdot T}$. Threshold $\geq 0.3$. |
| 5 | Identity Kinematics | $\delta\_{\text{id}}, v\_{\text{id}}, a\_{\text{id}}$ | 2 | Identity delta (distance), velocity (rate of change), and acceleration (jerk) tracking the motion of $I(t)$ through identity space. |
| 6 | Identity Vector | $I(t) \in \mathbb{R}^d$ | 1 | Agent's complete self-model as a continuous vector in $d$-dimensional space, updated each cognitive cycle. |
| 7 | Meta-Stability Index | $M(t)$ / MSI | 4 | Scalar summary of agent stability: $M(t) = 1.0 - 0.4 V\_{\text{id}} - 0.3 F\_{\text{goal}} - 0.3 \sigma^2\_{\text{pred}}$. Stabilization mode when $M(t) < 0.5$. |
| 8 | Strategy Evolution Fitness | SEF | 7 | Net improvement after strategy modification: $SEF = \frac{\overline{R}\_{\text{post}}}{\overline{R}\_{\text{pre}}} - \sigma\_{\text{oscillation}}$. Threshold $> 1.0$. |

### Level 1 - Tool Agent (`Level_1_Tool_Agent.md`)

| # | Term | Symbol / Acronym | Def # | Description |
|---|------|-----------------|:-----:|-------------|
| 1 | Intent Classification | $\phi$ | 3 | Maps request to probability distribution over tools: $\phi : \mathcal{R} \to [0,1]^{\lvert\mathcal{T}\rvert+1}$. |
| 2 | Level 1 Agent | $\mathcal{A}_1$ | 1 | Stateless function $\mathcal{A}_1 : \mathcal{R} \to \mathcal{O}$ mapping requests to responses via tool orchestration. |
| 3 | Level 1 to 2 Transition | $\mathcal{A}\_2 = \mathcal{A}\_1 \oplus \{\mathcal{W}, \mathcal{E}, \mathcal{G}, \Gamma\}$ | 4 | Requires world model, entity tracker, goal system, and temporal model. |
| 4 | Tool Set | $\mathcal{T} = \{T\_1, \ldots, T\_n\}$ | 2 | Finite set of available tools, each a partial function $T\_i : \mathcal{P}\_i \to \mathcal{O}\_i$. |

### Level 2 - Autonomous Agent (`Level_2_Autonomous_Agent.md`)

| # | Term | Symbol / Acronym | Def # | Description |
|---|------|-----------------|:-----:|-------------|
| 1 | Autonomous Goal Generation | $\Phi_{AG}$ | 6 | Function $\Phi_{AG} : \mathcal{P}(\mathcal{S}) \times \mathcal{E} \to \mathcal{P}(\mathcal{G})$ generating goals from state patterns and entities. |
| 2 | Emotion Vector | $e(t) \in \mathbb{R}^2$ | 3 | Two-dimensional affect state with valence $v(t)$ and arousal $a(t)$. |
| 3 | Goal | $g$ | 4 | Structured tuple $g = \langle \text{id, type, desc, } p, w, \text{status, } g\_{\text{parent}}, \{g\_{\text{sub}}\}, \text{progress}\rangle$. |
| 4 | Goal Priority Function | $p(g,t)$ | 5 | Dynamic priority: $p(g,t) = \alpha \cdot p_{\text{base}} + \beta \cdot u(g,t) + \gamma \cdot \xi(g,e(t))$. |
| 5 | Level 2 Agent | $\mathcal{A}_2$ | 1 | Stateful 5-tuple process $\mathcal{A}_2 = \langle \mathcal{R}, \mathcal{O}, \mathcal{S}, \mathcal{G}, f \rangle$. |
| 6 | Level 2 to 3 Transition | $\mathcal{A}\_3 = \mathcal{A}\_2 \oplus \{M\_{\text{self}}, \Pi, \mathcal{C}, \Lambda\}$ | 7 | Requires self-model, prediction engine, ethical constraint kernel, and meta-cognition comparator. |
| 7 | World Model | $\mathcal{W} = \langle \mathcal{K}, \mathcal{E}, \Gamma \rangle$ | 2 | Knowledge graph + entity tracker + temporal model. |

### Level 3 - Self-Regulating Agent (`Level_3_Self_Regulating_Agent.md`)

| # | Term | Symbol / Acronym | Def # | Description |
|---|------|-----------------|:-----:|-------------|
| 1 | Identity Hash | $h(t)$ | 6 | Deterministic hash $h(t) = \text{SHA-256}(I(t))$. Drift detected when $h(t) \neq h(t-1) \wedge \delta\_{\text{id}}(t) > \theta\_{\text{drift}}$. |
| 2 | Identity Kinematics (L3) | $\delta\_{\text{id}}, v\_{\text{id}}, a\_{\text{id}}$ | 5 | L3-specific: $\delta\_{\text{id}}(t) = \lVert I(t) - I(t-1)\rVert\_2$, $v_{\text{id}} = \delta / \Delta t$, $a_{\text{id}} = v(t) - v(t-1)$. Instability if $a_{\text{id}} > 0.5$. |
| 3 | Identity Vector (L3) | $I(t) \in [0,1]^5$ | 4 | Five dimensions: persona consistency, value alignment, capability confidence, emotional stability, goal persistence. |
| 4 | Level 3 Agent | $\mathcal{A}_3$ | 1 | 8-tuple $\mathcal{A}\_3 = \langle \mathcal{R}, \mathcal{O}, \mathcal{S}, \mathcal{G}, M\_{\text{self}}, \Pi, \mathcal{C}, \Lambda \rangle$. |
| 5 | Lyapunov Composite Stability Function | $C(t)$ | 7 | $C(t) = 0.30 V\_{\text{id}} + 0.25 E\_{\text{belief}} + 0.25 M\_{\text{goal}} + 0.20 V\_{\text{cons}}$. Each component $\in [0,1]$. |
| 6 | Meta-Cognition Levels | $d_{\max} = 3$ | 3 | Triple-loop hierarchy: L1 (predict vs outcome), L2 (evaluate update logic), L3 (evaluate the evaluator). Bounded by $d_{\max} = 3$ to prevent infinite recursion. |
| 7 | Meta Stability Index (L3) | $\operatorname{MSI}(t)$ | 8 | $\operatorname{MSI}(t) = 1.0 - 0.4 V\_{\text{id}} - 0.3 M\_{\text{goal}} - 0.3 \sigma^2\_{\text{pred}}$. Escalation when $\operatorname{MSI} < 0.5$. |
| 8 | MSCP Core Loop | - | 2 | Predict-act-compare-update cycle with delta-clamped self-updates, convergence checking, and ethical gating. |

### Level 4 - Adaptive General Agent (`Level_4_Adaptive_General_Agent.md`)

| # | Term | Symbol / Acronym | Def # | Description |
|---|------|-----------------|:-----:|-------------|
| 1 | Bounded Growth Safety Score | BGSS | 6 | Growth-stability balance: $BGSS = 1.0 - 0.4 \frac{dC}{dt} - 0.3 V\_{	ext{id}} - 0.3 R\_{	ext{ethical}}$. Threshold $\geq 0.7$. |
| 2 | Capability Acquisition Rate | CAR | 4 | Skill acquisition efficiency. Threshold $> 0$. |
| 3 | Cross-Domain Transfer Score | CDTS | 2 | Knowledge transfer to novel domains. Threshold $\geq 0.6$. |
| 4 | Extended Lyapunov Function | $C_{L4}(t)$ | 7 | 7-term composite: $0.15 V\_{\text{id}} + 0.15 H\_{\text{bel}} + 0.10 F\_{\text{mut}} + 0.10 \sigma\_{\text{con}} + 0.20 E\_v + 0.15 G\_c + 0.15 M\_s$. |
| 5 | Goal Progress Index | GPI | 3 | Sustained progress toward long-horizon goals. Threshold $\geq 0.3$. |
| 6 | Level 4 Agent | $\mathcal{A}_4$ | 1 | $\mathcal{A}\_4 = \mathcal{A}\_3 \oplus \langle \mathcal{D}, \mathcal{K}\_{\text{transfer}}, \Sigma, \mu, \mathcal{P}\_{\text{mod}} \rangle$. |
| 7 | Strategy Evolution Factor | SEF | 5 | Net improvement from mutations: $SEF = \overline{R}\_{\text{post}} / \overline{R}\_{\text{pre}} - \sigma\_{\text{oscillation}}$. Threshold $> 1.0$. |

### Level 4.5 - Self-Architecting Agent (`Level_4_5_Self_Architecting.md`)

| # | Term | Symbol / Acronym | Def # | Description |
|---|------|-----------------|:-----:|-------------|
| 1 | Adaptive Frame Weight Update | - | 8 | Frame influence evolution based on accuracy of frame-specific predictions. |
| 2 | Capability Diversity Index | CDI | 4 | Normalized Shannon entropy over capability domains. |
| 3 | Cognitive Topology | $\mathcal{T}_{\text{cog}} = (V, E, \omega)$ | 2 | Weighted directed graph of cognitive modules. |
| 4 | Identity Fragmentation Index | IFI | 10 | Cross-frame identity consistency. Critical threshold $\geq 0.5$. |
| 5 | Identity Integrity Score | IIS | 5 | Deviation from reference identity vector. Threshold $\geq 0.85$. |
| 6 | Impact Propagation Matrix | IPM | 7 | Propagation of topology change effects across modules. |
| 7 | Level 4.5 Agent | $\mathcal{A}_{4.5}$ | 1 | $\mathcal{A}\_{4.5} = \mathcal{A}\_4 \oplus \langle \mathcal{T}\_{\text{cog}}, \Psi, \mathcal{F}\_{\parallel}, \Xi, \Omega \rangle$. |
| 8 | Level 4.5 Composite Achievement Score | $L4.5_{\text{Score}}$ | 12 | $0.20 \text{SPA} + 0.20 \text{ARBR} + 0.15 \text{FCQ} + 0.15 \text{PCM} + 0.30 \text{ESR} \geq 0.65$. |
| 9 | Level 4.5 Lyapunov Stability Function | $V(\mathbf{X})$ | 11 | $V(\mathbf{X}) = a(1-S)^2 + bU^2 + cI_{\text{drift}}^2 + d(E - E^*)^2$. |
| 10 | Projection Confidence Decay | - | 6 | Exponential decay with $\lambda = 0.5$: confidence decreases with projection horizon. |
| 11 | Purpose Coherence Score | PCS | 9 | Goal landscape health. Threshold $\geq 0.6$. |
| 12 | Self-Evolution Optimization Fitness | SEOF | 3 | Composite scalar $\in [-1,1]$ measuring self-evolution quality. |

### Level 4.8 - Strategic Self-Modeling Agent (`Level_4_8_Strategic_Self_Modeling.md`)

| # | Term | Symbol / Acronym | Def # | Description |
|---|------|-----------------|:-----:|-------------|
| 1 | Bayesian Belief Update | - | 8 | Recursive Bayes rule with particle filter ($N_p = 100$). |
| 2 | Compound Severity Index | - | 12 | $\text{CompoundSeverity} = \sum\_{i \in \text{violated}} \frac{\text{ViolationMagnitude}\_i}{\text{Priority}\_i}$. Catastrophic if $> 2.0$. |
| 3 | Environmental Uncertainty | EU | 2 | Mean posterior variance. Target $< 0.15$. |
| 4 | Extended Value with Reward | EVR | 6 | Immediate + discounted future rewards with $\gamma = 0.95$. |
| 5 | Level 4.8 Agent | $\mathcal{A}_{4.8}$ | 1 | $\mathcal{A}\_{4.8} = \mathcal{A}\_{4.5} \oplus \langle \mathcal{W}\_{\text{prob}}, \mathcal{M}\_{\text{cap}}, \mathcal{S}\_{\text{strat}}, \mathcal{V}\_{\text{stab}} \rangle$. |
| 6 | Level 4.8 Lyapunov Function | $V(\mathbf{X})$ | 11 | Inherits L4.5 structure: $a(1-S)^2 + bU^2 + c(I_{\text{drift}})^2 + d(E-E^*)^2$. |
| 7 | Mean Calibration Error | MCE | 5 | Confidence-performance gap. Target $< 0.10$. |
| 8 | Multi-Scenario Strategy Score | - | 7 | $0.40 \cdot EV + 0.35 \cdot RA + 0.25 \cdot (1 - SI)$ composite. |
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
| 3 | Autonomy Stability Score | ASS | 7 | Product of normalized safety margins: $\text{ASS} = \prod\_{c=1}^{5} \frac{\text{margin}\_c}{\text{threshold}\_c}$. Target $\geq 0.20$. |
| 4 | Goal Approval Rate | - | 2 | $N\_{\text{approved}} / N\_{\text{generated}}$. Target $\geq 0.30$. |
| 5 | Goal Novelty | - | 3 | $1 - \max(\text{similarity to existing goals})$. Minimum $0.30$. |
| 6 | Goal Similarity | - | 8 | Weighted composite: SkillOverlap + HorizonMatch + OriginMatch. |
| 7 | Level 4.9 Agent | $\mathcal{A}_{4.9}$ | 1 | $\mathcal{A}\_{4.9} = \mathcal{A}\_{4.8} \oplus \langle \mathcal{G}\_{\text{gen}}, \vec{V}, \mathcal{R}\_{\text{surv}}, \mathcal{M}\_{\text{agent}}, \mathcal{V}\_{\text{auto}} \rangle$. |
| 8 | Linear Depletion Time | - | 6 | Estimated cycles until resource dimension reaches critical threshold. |
| 9 | Total Value Drift | - | 5 | Cumulative absolute deviation from baseline. Target $< 0.25$. |
| 10 | Value Coherence | - | 4 | Absence of internal contradictions in value system. Target $\geq 0.80$. |
| 11 | Value Tension | - | 9 | Competing value pair saturation measure. |

### Level 5 - Proto-AGI (`Level_5_Proto_AGI.md`)

| # | Term | Symbol / Acronym | Def # | Description |
|---|------|-----------------|:-----:|-------------|
| 1 | Generalization Score | $G$ | 3 | Mean transfer retention ratio across domains. Target $\geq 0.70$. |
| 2 | Goal Stability Score | $S_{\text{goal}}$ | 4 | Hierarchy change rate. Target $\geq 0.80$ over 5,000 cycles. |
| 3 | Identity Continuity Score | ICS | 2 | Cosine similarity over 10,000 cycles. Target $\geq 0.95$. |
| 4 | Level 4.9 to Level 5 Transition | - | 7 | $\text{AMS} \geq 0.80 \wedge \text{ASS} \geq 0.20 \wedge \text{TotalDrift} < 0.10 \wedge N_{\text{rollback}} = 0$. Four-stage activation protocol. |
| 5 | Level 5 Agent | $\mathcal{A}_5$ | 1 | $\mathcal{A}\_5 = \mathcal{A}\_{4.9} \oplus \langle \mathcal{I}\_{\text{persist}}, \mathcal{G}\_{\text{cross}}, \mathcal{E}\_{\text{goal}}, \mathcal{P}\_{\text{exist}}, \mathcal{M}\_{\text{multi}}, \mathcal{R}\_{\text{recon}} \rangle$. |
| 6 | Overall Maturity Index | OMI | 6 | Weighted geometric mean: $OMI = \prod\_{i=1}^{6} C\_i^{1/6}$. Target $\geq 0.75$. |
| 7 | Resilience Index | $R$ | 5 | Weighted mean over survival probability, cognition retention, and recovery speed across collapse scenarios. Target: survive $\geq 3$ scenarios. |

---

## 2. Propositions and Theorems

| # | Statement | Source | Type | Summary |
|---|-----------|--------|:----:|---------|
| 1 | Zero Mutual Information | L1, Prop 1 | Proposition | $I(o\_t; o\_{t-1}) = 0$ - outputs have zero mutual information (stateless). |
| 2 | Absence of Goal State | L1, Prop 2 | Proposition | No internal goal space exists at Level 1. |
| 3 | No Self-Model (L1) | L1, Prop 3 | Proposition | $M_{\text{self}} = \emptyset$ - no self-representation. |
| 4 | No Self-Model (L2) | L2, Prop 1 | Proposition | $M_{\text{self}} = \emptyset \implies$ no self-impact prediction. |
| 5 | Undetectable Drift | L2, Prop 2 | Proposition | Goal drift $\delta(t) = \lVert G\_t - G\_0\rVert\_2$ accumulates silently without bound. |
| 6 | No Ethical Constraints | L2, Prop 3 | Proposition | $\forall g \in \Phi_{AG}$: unconditionally accepted (no constraint set $\mathcal{C}$). |
| 7 | Bounded Stability | L3, Thm 1 | Theorem | Under delta clamping and $d_{\max} = 3$: $C(t+1) \leq C(t) + \epsilon$ with $\epsilon = 0.05$. |
| 8 | Bounded Identity Motion | Overview, Prop 1 | Proposition | $\lVert I(t) - I(0)\rVert\_2 \leq t \cdot \delta\_{\max}$. |
| 9 | Single-Cycle Drift Bound | Overview, Cor 1.1 | Corollary | Effective identity drift within any single cycle $\leq \Theta = 0.15$. |
| 10 | Lyapunov Convergence | Overview, Prop 2 | Proposition | $\lim_{t \to \infty} C(t) \leq C^* + \frac{\epsilon}{1 - \gamma}$ under stabilization. |
| 11 | Layer 0 Inviolability | Overview, Prop 3 | Proposition | Layer 0 ethical constraints cannot be violated by any MSCP-compliant operation. |
| 12 | Bounded Growth-Stability Trade-off | L4, Thm 2 | Theorem | $C_{L4}(t) < 0.8 \implies$ growth permitted; $C_{L4}(t) \geq 0.8 \implies$ growth frozen. |
| 13 | Level 4.5 Asymptotic Stability | L4.5, Thm 3 | Theorem | Equilibrium $\mathbf{X}^*$ is asymptotically stable if spectral radius $\rho(J) < 1.0$. |
| 14 | EVR Boundedness | L4.8, Prop 1 | Proposition | $\lvert\text{EVR}(G)\rvert \leq \lvert R\_{\text{immediate}}\rvert + \frac{2\lvert R\_{\text{immediate}}\rvert}{1-\gamma}$. |
| 15 | ASS Monotonic Sensitivity | L4.9, Prop 1 | Proposition | Multiplicative ASS structure: as any margin $\to 0$, ASS $\to 0$. |
| 16 | OMI Phase Coupling | L5, Prop 1 | Proposition | $OMI \geq \theta \implies \forall i: C_i \geq \theta^6$. If any $C_j = 0$, then $OMI = 0$. |
| 17 | Proto-AGI Completeness | L5, Thm 4 | Theorem | Identity invariance ($ICS \geq 0.95$), graceful degradation ($\geq 85\%$ core), and fallback safety (zero-degradation revert to $\mathcal{A}_{4.9}$). |

---

## 3. Acronyms and Abbreviations

| Acronym | Full Name | Source(s) |
|---------|-----------|-----------|
| AMS | Autonomy Maturity Score | L4.9 |
| ARBR | Architecture Recomposition Benefit Rate | L4.5 |
| AS | Adaptation Speed | L4 |
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
| EU | Environmental Uncertainty | L4.8 |
| EVR | Extended Value with Reward | L4.8 |
| FCQ | Frame Consensus Quality | L4.5 |
| GPI | Goal Progress Index / Goal Persistence Index | Overview, L4 |
| GRP | Graduated Recomposition Protocol | L4.5 |
| GRS | Goal Resilience Score | L4 |
| GSRS | Goal Self-Reinforcement Score | L4.5 |
| ICS | Identity Continuity Score | L5 |
| IFI | Identity Fragmentation Index | L4.5 |
| IIS | Identity Integrity Score | L4.5, L4.8 |
| IPM | Impact Propagation Matrix | L4.5 |
| MCE | Mean Calibration Error | L4.8 |
| MSCP | Minimal Self-Consciousness Protocol | All |
| MSI | Meta-Stability Index | Overview, L3 |
| MVC | Minimum Viable Cognition | L5 |
| OMI | Overall Maturity Index | L5 |
| PCM | Purpose Coherence Maintenance | L4.5 |
| PCS | Purpose Coherence Score | L4.5 |
| RDF | Resource Depletion Forecast | L4.8 |
| RES | Risk Exposure Score | L4.8 |
| ROD | Recursive Optimization Depth | L4.5 |
| SEF | Strategy Evolution Factor / Fitness | Overview, L4 |
| SEOF | Self-Evolution Optimization Fitness | L4.5 |
| SMS | Strategic Maturity Score | L4.8 |
| SNI | Strategy Novelty Index | L4 |
| SPA | Self-Projection Accuracy | L4.5 |
| VaR | Value at Risk | L4.8 |

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
| $I(t)$ | Identity vector at time $t$ | Overview, L3 |
| $\delta_{\text{id}}(t)$ | Identity delta (L2 norm of identity change) | Overview, L3 |
| $v_{\text{id}}(t)$ | Identity velocity | Overview, L3 |
| $a_{\text{id}}(t)$ | Identity acceleration | Overview, L3 |
| $\delta_{\max}$ | Maximum identity change per step (typically 0.05) | Overview, L3 |
| $\theta_{\text{drift}}$ | Drift detection threshold | Overview, L3 |
| $\theta_{\text{instability}}$ | Instability threshold (typically 0.5) | Overview, L3 |
| $s(t)$ | Scaling factor $\in [0,1]$ | Overview, L3 |
| $C(t)$ | Composite stability function | Overview, L3, L4 |
| $C_{L4}(t)$ | Extended Lyapunov function (7-term) | L4 |
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
| Affective Engine | L3 | 5-dimensional internal emotion vector (curiosity, frustration, satisfaction, anxiety, excitement). |
| Belief Graph | L3 | Weighted graph of beliefs with identity-linked nodes and contradiction detection. |
| Cognitive Budget Controller | L3, Overview | Conditional activation gating for graceful degradation under resource scarcity. |
| Ethical Kernel | L3, Overview | Dual-layer architecture: Layer 0 (immutable invariants) + Layer 1 (adaptive policies). |
| Existential Guard | L4.5 | Monitors ROD, CAS, IFI, GSRS. Runs in separate execution context; non-modifiable. |
| Global Workspace | L3 | Central broadcast mechanism for cognitive state sharing across modules. |
| Meta-Escalation Guard | Overview, L3 | Limits consecutive self-updates (max 3), cumulative delta threshold (0.15), and enforces cooldown. |
| Parallel Cognitive Frames | L4.5 | Five parallel evaluation perspectives including ethical constraint frame with veto power. |
| Prediction Engine | L3 | Generates prediction snapshots before action execution. |
| Purpose Reflection Engine | L4.5 | Evaluates goal landscape coherence, monitors PCS. |
| Self-Consistency Tensor | L3 | Matrix $S_{ij}$ = alignment(belief$_i$, reference$_j$). Global consistency = mean(S). |
| Self-Projection Engine | L4.5 | Simulates three evolutionary trajectories across three time scales. |
| ShadowAgent | L4 | Sandbox-isolated clone for testing modifications. Max 1 instance, max 20 simulation cycles. |
| Survival Instinct Engine | L3 | Monitors homeostatic indicators and generates bounded survival goals (priority cap 0.85, max 3 goals). |
| Value Lock Manager | L3 | Protects core values via SHA-256 hash verification with rollback on mismatch. |

### Processes & Protocols

| Term | Source(s) | Description |
|------|-----------|-------------|
| Bounded Self-Modification | L4 | 7-step protocol: Propose, Pre-Validate, Simulate, Stability-Validate, Commit, Monitor, Confirm. |
| Collapse Scenarios | L5 | Four scenarios: Resource Collapse, Adversarial Suppression, Environmental Shift, Information Blackout. |
| Delta-Clamped Updates | Overview, L3 | All self-modifications bounded by $\delta_{\max}$. LLM text-based self-modification is forbidden. |
| Five-Phase Capability Expansion | L4 | Pipeline for autonomous skill acquisition and validation. |
| Goal Ecology | L5 | Self-sustaining goal hierarchy with conflict resolution, pruning, and runaway detection. |
| Graduated Recomposition Protocol | L4.5 | Phase 0 (Shadow), Phase 1 (20% traffic), Phase 2 (80% traffic), Phase 3 (Full commitment + cooldown). |
| Predict-Compare-Update Loop | Overview, L3 | Core MSCP mechanism: predict outcomes, compare to actual, update self-model. |
| Recomposition Vocabulary | L4.5 | Predefined operations: AddEdge, WeighEdge, SplitModule, MergeModule. |
| Self-Reconstruction | L5 | Architecture simplification under degraded resources with identity-preserving rebuild. |
| Skill Lifecycle | L4 | States: CANDIDATE $\to$ VALIDATED $\to$ ACTIVE $\to$ MATURE $\to$ DEPRECATED. |
| Strictly Additive Principle | L4.5, L5 | Higher levels extend lower levels ($\oplus$) without modifying them. Disabling $\Delta_n$ restores exact $\mathcal{A}_{n-1}$ behavior. |
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

---

## Statistics

| Metric | Count |
|--------|:-----:|
| Formal Definitions | 77 |
| Propositions | 12 |
| Theorems | 4 |
| Corollaries | 1 |
| Acronyms / Abbreviations | 41 |
| Mathematical Symbols | 50+ |
| Key Technical Terms | 40+ |
| Source Documents | 9 |
