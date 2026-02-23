# MSCP — Minimal Self-Consciousness Protocol

> **A Safety-Oriented Framework for Structurally Self-Aware AI Agents**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status: Research](https://img.shields.io/badge/Status-Research-orange.svg)](#)
[![Docs: 9 Documents](https://img.shields.io/badge/Docs-9_Documents-green.svg)](docs/)
[![References: 144 Papers](https://img.shields.io/badge/References-144_Papers-blueviolet.svg)](docs/MSCP_Overview.md#10-references)
[![Levels: L1–L5](https://img.shields.io/badge/Levels-L1–L5-informational.svg)](docs/levels/README.md)
[![Math: 8 Definitions · 4 Theorems](https://img.shields.io/badge/Math-8_Defs_·_4_Theorems-yellow.svg)](docs/MSCP_Overview.md#6-mathematical-analysis)
[![Safety: 30+ Mechanisms](https://img.shields.io/badge/Safety-30%2B_Mechanisms-red.svg)](docs/MSCP_Overview.md#5-safety-mechanisms)

> **Note**: This is an **independent personal research project**. It does not represent the views or official work of any organization. The core motivation is to explore how AI agents can grow more capable **while remaining safe, predictable, and aligned with human values**.

---

## Overview

The **Minimal Self-Consciousness Protocol (MSCP)** is a structured protocol for building AI agents with *safe structural self-awareness* — the capacity to predict their own state changes, compare predictions against outcomes, and update themselves only within bounded safety envelopes.

As agents gain the ability to set goals, modify strategies, and self-improve, **how do we keep them stable, aligned, and predictable?** MSCP answers this with the principle that **safety is not the enemy of capability — it is its prerequisite.**

### Key Contributions

- **Six-Level Agent Cognition Taxonomy** — from reactive Tool Agents (L1) to Proto-AGI (L5), with measurable transition criteria and formal definitions at every level
- **16-Layer Cognitive Architecture** — composable, independently testable modules spanning perception through meta-cognitive control
- **30+ Structural Safety Mechanisms** — identity continuity, prediction-gated actions, delta-clamped updates, Lyapunov convergence, ethical invariants, affective safety, and survival instinct bounds
- **Rigorous Mathematical Formalization** — 71 formal definitions, 7 propositions, 4 theorems with proof sketches across all level documents
- **144 Academic References** — comprehensive coverage of cognitive architectures, AI safety, predictive processing, consciousness theory, meta-cognition, and AGI research

---

## Agent Cognition Levels

> The "Status" column reflects the implementation state within this project's reference implementation.

| Level | Name | Self-Awareness | Key Capability | Status |
|:-----:|------|:--------------:|----------------|:------:|
| **1** | Tool Agent | None | Deterministic tool invocation | Baseline |
| **2** | Autonomous Agent | None | World model, autonomous goals | Defined |
| **3** | Self-Regulating Agent | Structural | 16-layer architecture, MSCP core loop, identity vector | Implemented |
| **4** | Adaptive General Agent | Structural + Reflective | Cross-domain transfer, bounded self-modification | Implemented |
| **4.5** | Self-Architecting Agent | Architectural | Self-projection (SEOF), architecture recomposition | Implemented |
| **4.8** | Strategic Self-Modeling | Architectural + Strategic | Probabilistic world model, strategic planning | Design |
| **4.9** | Autonomous Strategic | Architectural + Autonomous | Value evolution, multi-agent reasoning | Design |
| **5** | Proto-AGI | Full | Cross-domain generalization, self-reconstruction | Research |

---

## Core Design Principles

| # | Principle | Description |
|:-:|-----------|-------------|
| 1 | **No LLM-Text-Based Self-Modification** | All self-modifications use structured numerical operations, never LLM-generated text |
| 2 | **No Action Without Prediction** | Every action requires a prediction snapshot for comparison |
| 3 | **Delta-Clamped Updates** | All self-modifications are bounded by maximum delta values |
| 4 | **Identity Continuity** | Deterministic identity hashing with drift detection and rollback |
| 5 | **Ethical Invariance** | Layer 0 constraints are immutable and LLM-independent |
| 6 | **Lyapunov Convergence** | Mathematical guarantee that self-modification converges |

---

## Safety Mechanism Stack

MSCP implements a defense-in-depth safety architecture:

```
Layer 0 ─ Immutable Ethical Invariants (rule-based, no LLM dependency)
Layer 1 ─ Core Value Locking (SHA-256 hash verification)
Layer 2 ─ Delta-Clamped Self-Updates (max Δ per step)
Layer 3 ─ Meta-Escalation Guard (rollback on threshold breach)
Layer 4 ─ Prediction-Gated Actions (predict → compare → update)
Layer 5 ─ Lyapunov Convergence Monitor (oscillation detection)
Layer 6 ─ Cognitive Budget Controller (graceful degradation)
Layer 7 ─ Affective Safety (emotion bounds, no decision domination)
Layer 8 ─ Survival Instinct Bounds (priority capping, ethical validation)
```

---

## Documentation

### Main Document

- **[MSCP Overview](docs/MSCP_Overview.md)** — Complete framework specification with mathematical formalization and 144 references

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

**Moon Hyuk Choi** — [moonchoi@microsoft.com](mailto:moonchoi@microsoft.com)
Microsoft Cloud & AI Apps CSA

## Contributing

This is very much a work in progress. Feedback, critique, and contributions are welcome as we collectively figure out how to build AI agents that are not just more powerful, but fundamentally more trustworthy.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

> This documentation was written with the assistance of [GitHub Copilot](https://github.com/features/copilot).
