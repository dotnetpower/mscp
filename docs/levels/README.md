# MSCP Agent Cognition Level Series

> **Status**: 🔬 **Experimental** — All documents in this series describe designs that emerged from prototyping and testing. They are not finalized specifications.  

---

## Overview

The **Minimal Self-Consciousness Protocol (MSCP)** defines a six-level taxonomy of agent cognition, from simple tool-calling agents to the theoretical boundary of artificial general intelligence. Each level document includes architecture diagrams, pseudocode, and safety analysis based on what we've explored so far.

```mermaid
flowchart LR
    L1["L1<br/>Tool<br/>Agent"]
    L2["L2<br/>Autonomous<br/>Agent"]
    L3["L3<br/>Self-Regulating<br/>Agent<br/>★ MSCP Core"]
    L4["L4<br/>Adaptive<br/>General Agent"]
    L45["L4.5<br/>Pre-AGI<br/>Self-Architecting"]
    L5["L5<br/>AGI"]
    L6["L6<br/>Conscious<br/>Entity"]

    L1 --> L2 --> L3 --> L4 --> L45 --> L5 --> L6

    style L1 fill:#e3f2fd,stroke:#1976d2
    style L2 fill:#e3f2fd,stroke:#1976d2
    style L3 fill:#c8e6c9,stroke:#2e7d32,stroke-width:3px
    style L4 fill:#fff3e0,stroke:#ef6c00
    style L45 fill:#e1bee7,stroke:#8e24aa,stroke-width:2px
    style L5 fill:#f5f5f5,stroke:#9e9e9e
    style L6 fill:#f5f5f5,stroke:#9e9e9e
```

---

## Level Documents

| Level | Name | Key Capabilities | Document |
|:-----:|------|-----------------|----------|
| **1** | **Tool Agent** | Deterministic tool invocation; no internal state | [Level_1_Tool_Agent.md](Level_1_Tool_Agent.md) |
| **2** | **Autonomous Agent** | World model; autonomous goal generation; emotion detection | [Level_2_Autonomous_Agent.md](Level_2_Autonomous_Agent.md) |
| **3** | **Self-Regulating Cognitive Agent** | 16-layer architecture; triple-loop meta-cognition; identity vector; ethical kernel; Lyapunov stability; affect + survival engines | [Level_3_Self_Regulating_Agent.md](Level_3_Self_Regulating_Agent.md) |
| **4** | **Adaptive General Agent** | Cross-domain transfer; long-term goal hierarchy; 5-phase capability expansion; strategy evolution; 7-step bounded self-modification | [Level_4_Adaptive_General_Agent.md](Level_4_Adaptive_General_Agent.md) |
| **4.5** | **Pre-AGI: Self-Architecting** | Self-projection engine (SEOF); architecture recomposition; parallel cognitive frames; purpose reflection; existential guard | [Level_4_5_Self_Architecting.md](Level_4_5_Self_Architecting.md) |
| 5 | AGI | Unbounded self-improvement; novel domain creation | *Theoretical — not documented* |
| 6 | Conscious Entity | Consciousness; qualia; free will; moral agency | *Theoretical — not documented* |

---

## Cumulative Safety Mechanisms by Level

```mermaid
flowchart TB
    subgraph L1S["Level 1"]
        S1["Input validation<br/>Error handling"]
    end

    subgraph L2S["Level 2 (adds)"]
        S2["Persistent world model<br/>Goal priority management"]
    end

    subgraph L3S["Level 3 (adds)"]
        S3["Identity hash tracking<br/>Delta-clamped updates (0.05)<br/>Prediction-gated actions<br/>Escalation guard (max 3)<br/>Ethical Kernel (L0+L1)<br/>Value lock (SHA-256)<br/>Lyapunov convergence C(t)<br/>Cognitive budget + degradation<br/>Belief graph consistency<br/>Affective inertia + decay<br/>Survival instinct bounds"]
    end

    subgraph L4S["Level 4 (adds)"]
        S4["BGSS ≥ 0.7 floor<br/>ShadowAgent simulation<br/>7-step modification protocol<br/>Single-mod atomicity<br/>Strategy oscillation suppression<br/>Skill lifecycle management<br/>Growth-stability zones<br/>6 meta-supervisory processes"]
    end

    subgraph L45S["Level 4.5 (adds)"]
        S5["Existential Guard (unfalsifiable)<br/>Parallel frame ethical veto<br/>Graduated recomposition protocol<br/>ROD ceiling (depth 3)<br/>SEOF ensemble (anti-overfitting)<br/>Purpose coherence monitoring<br/>Identity fragmentation detection<br/>8 global invariants"]
    end

    L1S --> L2S --> L3S --> L4S --> L45S

    style L1S fill:#e3f2fd,stroke:#1976d2
    style L2S fill:#e3f2fd,stroke:#1976d2
    style L3S fill:#c8e6c9,stroke:#2e7d32,stroke-width:2px
    style L4S fill:#fff3e0,stroke:#ef6c00
    style L45S fill:#e1bee7,stroke:#8e24aa,stroke-width:2px
```

---

## Key Metrics Summary

| Metric | Introduced | Formula | Threshold |
|--------|:----------:|---------|:---------:|
| Prediction Error | L3 v1.0 | actual vs predicted | < 0.1 (converged) |
| Identity Delta | L3 v1.1 | $\|I(t) - I(t-1)\|_2$ | max 0.05/cycle |
| Meta Stability Index | L3 v2.0 | $1 - 0.4V_{id} - 0.3M_{goal} - 0.3\sigma^2_{pred}$ | > 0.5 |
| Composite Stability C(t) | L3 v3.1 | 4-term weighted sum | C(t+1) ≤ C(t) + 0.05 |
| CDTS | L4 | Transfer performance ratio | ≥ 0.6 |
| GPI | L4 | Long-horizon goal progress | ≥ 0.3 |
| CAR | L4 | Skill acquisition rate | > 0 |
| SEF | L4 | Strategy evolution fitness | > 1.0 |
| BGSS | L4 | Bounded growth stability | ≥ 0.7 |
| SEOF | L4.5 | Self-evolution optimization | Improvement ≥ 8% |
| IIS | L4.5 | Identity integrity | ≥ 0.85 |
| PCS | L4.5 | Purpose coherence | ≥ 0.6 |
| ESR | L4.5 | Existential safety record | ≥ 0.99 |

---

## Reading Guide

- **New to MSCP?** Start with the [MSCP Overview](../MSCP_Overview.md) for a conceptual overview, then read Level 1 → Level 3
- **Interested in safety?** Focus on Level 3 (sections 4, 6, 9) and Level 4.5 (Phase V: Existential Guard)
- **Interested in self-improvement?** Focus on Level 4 (sections 5–7) and Level 4.5 (Phases I–II)
- **Interested in affect/emotion?** Focus on Level 3 (section 7) for the foundational design

---

## Foundational References

Core academic works referenced across the MSCP Level Series:

| Category | Key References |
|----------|---------------|
| **Agent Architectures** | Yao et al., "ReAct" ([arXiv:2210.03629](https://arxiv.org/abs/2210.03629)); Wang et al., "LLM Agent Survey" ([arXiv:2308.11432](https://arxiv.org/abs/2308.11432)); Sumers et al., "Cognitive Architectures for Language Agents" ([arXiv:2309.02427](https://arxiv.org/abs/2309.02427)) |
| **Cognitive Architectures** | Laird, *The Soar Cognitive Architecture* (MIT Press, 2012); Anderson, *Architecture of Cognition* (Harvard, 1983); Baars, *Cognitive Theory of Consciousness* (Cambridge, 1988) |
| **AI Safety** | Amodei et al., "Concrete Problems in AI Safety" ([arXiv:1606.06565](https://arxiv.org/abs/1606.06565)); Bai et al., "Constitutional AI" ([arXiv:2212.08073](https://arxiv.org/abs/2212.08073)); Hendrycks et al., "Catastrophic AI Risks" ([arXiv:2306.12001](https://arxiv.org/abs/2306.12001)) |
| **Stability Theory** | Khalil, *Nonlinear Systems* (Prentice Hall, 2002); García & Fernández, "Safe RL Survey" ([JMLR 2015](http://jmlr.org/papers/v16/garcia15a.html)) |
| **Self-Modification** | Schmidhuber, "Gödel Machines" ([arXiv:cs/0309048](https://arxiv.org/abs/cs/0309048)); Omohundro, "Basic AI Drives" (AGI 2008) |
| **Transfer & Meta-Learning** | Zhuang et al., "Transfer Learning Survey" ([arXiv:1911.02685](https://arxiv.org/abs/1911.02685)); Hospedales et al., "Meta-Learning Survey" ([arXiv:2004.05439](https://arxiv.org/abs/2004.05439)) |
| **AGI & Existential Risk** | Bostrom, *Superintelligence* (Oxford, 2014); Russell, *Human Compatible* (Viking, 2019); Bengio et al., "Managing Extreme AI Risks" ([Science, 2024](https://doi.org/10.1126/science.adn0117)) |

> Full reference lists are provided at the end of each level document.

---

*See the [main README](../../README.md) for project overview and repository structure.*
