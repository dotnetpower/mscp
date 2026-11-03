<!--
Copyright (c) 2026 Moon Hyuk Choi
Licensed under the MIT License.
See LICENSE file in the repository root for full license information.

Redistribution (commercial or non-commercial) must retain this notice.
Removal of attribution constitutes a license violation.
-->
# MSCP - Minimal Self-Consciousness Protocol

> **A Safety-Oriented Framework for Structurally Self-Aware AI Agents**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status: Research](https://img.shields.io/badge/Status-Research-orange.svg)](#)
[![Docs: Bilingual](https://img.shields.io/badge/Docs-English%20%2F%20한국어-green.svg)](docs/)
[![References: 144 Papers](https://img.shields.io/badge/References-144_Papers-blueviolet.svg)](docs/MSCP_Overview.md#10-references)
[![Levels: L1–L5](https://img.shields.io/badge/Levels-L1–L5-informational.svg)](docs/levels/README.md)
[![Math: Conditional Contracts](https://img.shields.io/badge/Math-Conditional_Contracts-yellow.svg)](docs/MSCP_Overview.md#6-mathematical-analysis)
[![Safety: 30+ Mechanisms](https://img.shields.io/badge/Safety-30%2B_Mechanisms-red.svg)](docs/MSCP_Overview.md#5-safety-mechanisms)

> **Note**: This is an **independent personal research project**. It does not represent the views or official work of any organization. The core motivation is to explore how AI agents can grow more capable **while remaining safe, predictable, and aligned with human values**.

## Revision History

| Version | Date | Description |
|---------|------|-------------|
| 0.1.0 | 2026-02-23 | Initial README with project overview, level table, safety stack, documentation index |
| 0.2.0 | 2026-02-26 | Added Level Essence Formulas table |
| 0.3.0 | 2026-03-02 | Fixed Level Essence Formulas (LaTeX subscript syntax); added Level 6 to taxonomy table |

---

## Overview

The **Minimal Self-Consciousness Protocol (MSCP)** is a structured protocol for building AI agents with *safe structural self-awareness* - the capacity to predict their own state changes, compare predictions against outcomes, and update themselves only within bounded safety envelopes.

As agents gain the ability to set goals, modify strategies, and self-improve, **how do we keep them stable, aligned, and predictable?** MSCP answers this with the principle that **safety is not the enemy of capability - it is its prerequisite.**

### Key Contributions

- **Six-Level Agent Cognition Taxonomy** - from reactive Tool Agents (L1) to Proto-AGI (L5), with measurable transition criteria and formal definitions at every level
- **16-Layer Cognitive Architecture** - composable, independently testable modules spanning perception through meta-cognitive control
- **Structural Safety Mechanisms** - semantic continuity, prediction-gated actions, bounded updates, conditional risk monitoring, invariant enforcement, and recoverability
- **Explicit Mathematical Contracts** - definitions and conditional propositions with assumptions, proof sketches, and limitations; not an unconditional safety or convergence certification
- **144 Academic References** - comprehensive coverage of cognitive architectures, AI safety, predictive processing, consciousness theory, meta-cognition, and AGI research

---

## Agent Cognition Levels

> The "Status" column distinguishes public samples, reference prototypes described by the project, and research criteria. It is not independent level qualification. See [Documentation Status and Validation](docs/specs/Documentation_Status.md), reviewed 2026-11-03.

| Level | Name | Self-Awareness | Key Capability | Status |
|:-----:|------|:--------------:|----------------|:------:|
| **1** | Tool Agent | No persistent reflexive model | Bounded tool invocation | Educational sample |
| **2** | Autonomous Agent | No reflexive change regulation | Persistent state, goals, authorized continuation | Educational sample |
| **3** | Self-Regulating Agent | Structural | MSCP core loop, versioned self-model | Prototype described |
| **4** | Adaptive General Agent | Structural + reflective | Cross-domain transfer, bounded self-modification | Prototype described |
| **4.5** | Self-Architecting Agent | Architectural | Self-projection (SEOF), architecture recomposition | Prototype described |
| **4.8** | Strategic Self-Modeling | Strategic design | Probabilistic world model, strategic planning | Research criteria |
| **4.9** | Autonomous Strategic | Autonomous strategic design | Value-change auditing, multi-agent reasoning | Research criteria |
| **5** | Proto-AGI | Extended structural design | Held-out generalization, validated reconstruction | Research criteria |
| **6** | Strong AGI / Conscious Entity | Phenomenal | Subjective experience, moral agency, independent value formation | Theoretical |

---

## Core Design Principles

| # | Principle | Description |
|:-:|-----------|-------------|
| 1 | **Independent Self-Modification Admission** | LLMs may propose candidates; only typed, validated updates may commit |
| 2 | **No Action Without Prediction** | Every action requires a prediction snapshot for comparison |
| 3 | **Delta-Clamped Updates** | All self-modifications are bounded by maximum delta values |
| 4 | **Identity Continuity** | Semantic change monitoring plus separate integrity and ancestry checks |
| 5 | **Ethical Invariance** | Layer 0 constraints are immutable and LLM-independent |
| 6 | **Conditional Risk Bounds** | Bounded increments under explicit assumptions; no unconditional convergence claim |

---

## Safety Mechanism Stack

MSCP implements a defense-in-depth safety architecture:

```
Layer 0 ─ Immutable Ethical Invariants (rule-based, no LLM dependency)
Layer 1 ─ Core Value Locking (SHA-256 hash verification)
Layer 2 ─ Delta-Clamped Self-Updates (max Δ per step)
Layer 3 ─ Meta-Escalation Guard (rollback on threshold breach)
Layer 4 ─ Prediction-Gated Actions (predict → compare → update)
Layer 5 ─ Composite Risk Monitor (conditional bounds, oscillation signals)
Layer 6 ─ Cognitive Budget Controller (graceful degradation)
Layer 7 ─ Bounded Operational Modulation (no authority expansion)
Layer 8 ─ Homeostatic Safety (recovery within policy, external stop precedence)
```

---

## Documentation

### Main Document

- **[MSCP Overview](docs/MSCP_Overview.md)** - Complete framework specification with mathematical formalization and 144 references

### Per-Level Architecture Documents

Detailed architecture specifications with Mermaid diagrams, formal definitions, pseudocode, and safety analysis:

| Document | Content |
|----------|---------|
| [Level Series Overview](docs/levels/README.md) | Navigation index and cumulative safety summary |
| [Level 1: Tool Agent](docs/levels/Level_1_Tool_Agent.md) | Stateless tool invocation, intent routing |
| [Level 2: Autonomous Agent](docs/levels/Level_2_Autonomous_Agent.md) | World model, autonomous goals, emotion detection |
| [Level 3: Self-Regulating Agent](docs/levels/Level_3_Self_Regulating_Agent.md) | 16-layer architecture, MSCP v1–v4, triple-loop meta-cognition |
| [Level 4: Adaptive General Agent](docs/levels/Level_4_Adaptive_General_Agent.md) | Cross-domain transfer, capability expansion, bounded self-modification |
| [Level 4.5: Self-Architecting](docs/levels/Level_4_5_Self_Architecting.md) | Self-projection (SEOF), architecture recomposition, existential guard |
| [Level 4.8: Strategic Self-Modeling](docs/levels/Level_4_8_Strategic_Self_Modeling.md) | World model integration, meta-cognitive self-model, strategic planning |
| [Level 4.9: Autonomous Strategic](docs/levels/Level_4_9_Autonomous_Strategic_Agent.md) | Autonomous goal generation, value evolution, multi-agent reasoning |
| [Level 5: Proto-AGI](docs/levels/Level_5_Proto_AGI.md) | Persistent identity, cross-domain generalization, self-reconstruction |

### Level Essence Formulas

The following formulas illustrate selected mechanisms, not sufficient conditions for level qualification. Source definitions and all mandatory gates take precedence.

| Level | Essence | Formula |
|:-----:|---------|---------|
| **1** | Episode-bounded policy | $(o,\mathbf{a},e')\sim\mathcal{A}_1(\cdot\mid r,c,e),\quad\lvert\mathbf{a}\rvert\leq B$ |
| **2** | Stateful transition | $(o_t,\; s_{t+1},\; G_{t+1}) = f(r_t,\; s_t,\; G_t)$ |
| **3** | Predict-act-compare-update | $\epsilon_t = \lVert\hat{\Delta}_t - \Delta_t^{\text{actual}}\rVert_2,\quad \lVert W\Delta M_t\rVert_p \leq \delta_{\max}$; monitoring does not imply $\epsilon_t\to0$ |
| **4** | Transfer + safety | $\operatorname{CDTS} = \frac{1}{|D_{\text{novel}}|} \sum_{d \in D_{\text{novel}}} \frac{P_{\text{transfer}}(d)}{P_{\text{baseline}}(d)} \geq 0.6 \;\;\land\;\; \operatorname{BGSS}(t) \geq 0.7$ |
| **4.5** | Admitted topology mutation | $\mathcal{T}'_{\text{cog}}=\Xi(\mathcal{T}_{\text{cog}}),\quad C_{\text{ext}}\land C_{\text{self}}$ |
| **4.8** | Robust admitted strategy | $s^*=\arg\max_{s\in\Sigma_{\text{admitted}}}\operatorname{RobustValue}(s)$ |
| **4.9** | Autonomous goals + value stability | $g^* = \phi_{\text{valid}}\bigl(\phi_{\text{synth}}(\mathcal{O}_{\text{detect}}(\mathcal{W}))\bigr), \quad \textstyle\sum_{d} |w_d(t) - w_d^{\text{baseline}}| < 0.25$ |
| **5** | Composite continuity contract | $C_I=C_{\text{anchor}}\land C_{\text{component}}\land C_{\text{norm}}\land C_{\text{trajectory}}\land C_{\text{journal}}\land C_{\text{corr}}$ |

---

## Repository Structure

```
mscp/
├── README.md                          # This file
├── LICENSE                            # MIT License
└── docs/
    ├── MSCP_Overview.md               # Main framework document (930+ lines, 144 refs)
    └── levels/
        ├── README.md                  # Level series navigation
        ├── Level_1_Tool_Agent.md
        ├── Level_2_Autonomous_Agent.md
        ├── Level_3_Self_Regulating_Agent.md
        ├── Level_4_Adaptive_General_Agent.md
        ├── Level_4_5_Self_Architecting.md
        ├── Level_4_8_Strategic_Self_Modeling.md
        ├── Level_4_9_Autonomous_Strategic_Agent.md
        └── Level_5_Proto_AGI.md
```

---

## Author

**Moon Hyuk Choi** - [moonchoi@microsoft.com](mailto:moonchoi@microsoft.com)
Microsoft Cloud & AI Apps CSA

## Contributing

This is very much a work in progress. Feedback, critique, and contributions are welcome as we collectively figure out how to build AI agents that are not just more powerful, but fundamentally more trustworthy.

For the local build, math/link checks, preview command, terminology, and public disclosure boundary, see [Documentation Status and Validation](docs/specs/Documentation_Status.md). Do not copy private implementation details into public documentation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## License Notice

This project is licensed under the MIT License.

Any redistribution, commercial or non-commercial, must retain:
- The original copyright notice
- The full MIT license text
- Clear attribution to the original author

Failure to retain attribution constitutes a violation of the license.

---

> This documentation was written with the assistance of [GitHub Copilot](https://github.com/features/copilot).
