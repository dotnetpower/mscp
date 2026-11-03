---
title: "Home"
description: "MSCP: an experimental framework for structurally self-aware agents, with explicit safety assumptions, research criteria, and validation limits."
---

<!--
Copyright (c) 2026 Moon Hyuk Choi
Licensed under the MIT License.
See LICENSE file in the repository root for full license information.

Redistribution (commercial or non-commercial) must retain this notice.
Removal of attribution constitutes a license violation.
-->

# MSCP - Minimal Self-Consciousness Protocol

<p align="center" style="font-size: 1.2em; color: var(--md-default-fg-color--light);" markdown>
  **A Safety-Oriented Framework for Structurally Self-Aware AI Agents**
</p>

<p align="center" markdown>

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/dotnetpower/mscp/blob/main/LICENSE)
[![Status: Research](https://img.shields.io/badge/Status-Research-orange.svg)](#)
[![Docs: Bilingual](https://img.shields.io/badge/Docs-English%20%2F%20Korean-green.svg)](MSCP_Overview.md)
[![References: 144 Papers](https://img.shields.io/badge/References-144_Papers-blueviolet.svg)](MSCP_Overview.md#10-references)
[![Levels: L1–L5](https://img.shields.io/badge/Levels-L1–L5-informational.svg)](levels/README.md)
[![Safety: 30+ Mechanisms](https://img.shields.io/badge/Safety-30%2B_Mechanisms-red.svg)](MSCP_Overview.md#5-safety-mechanisms)

</p>

!!! note "Independent Research"
    This is an **independent personal research project**. It does not represent the views or official work of any organization. The core motivation is to explore how AI agents can grow more capable **while remaining safe, predictable, and aligned with human values**.

---

## What is MSCP?

The **Minimal Self-Consciousness Protocol (MSCP)** is a structured protocol for building AI agents with *safe structural self-awareness* - the capacity to predict their own state changes, compare predictions against outcomes, and update themselves only within bounded safety envelopes.

As agents gain the ability to set goals, modify strategies, and self-improve, **how do we keep them stable, aligned, and predictable?** MSCP answers this with the principle:

!!! quote "Core Tenet"
    **Safety is not the enemy of capability - it is its prerequisite.**

---

## Key Contributions

<div class="grid cards" markdown>

-   :material-layers-triple:{ .lg .middle } **Six-Level Cognition Taxonomy**

    ---

    From reactive Tool Agents (L1) to Proto-AGI (L5), with measurable transition criteria and formal definitions at every level.

    [:octicons-arrow-right-24: Explore Levels](levels/README.md)

-   :material-view-module:{ .lg .middle } **16-Layer Cognitive Architecture**

    ---

    Composable, independently testable modules spanning perception through meta-cognitive control.

    [:octicons-arrow-right-24: Architecture Details](MSCP_Overview.md#4-architecture-the-multi-layer-cognitive-stack)

-   :material-shield-check:{ .lg .middle } **30+ Safety Mechanisms**

    ---

    Semantic continuity, prediction-gated actions, bounded updates, conditional risk monitoring, and invariant enforcement.

    [:octicons-arrow-right-24: Safety Stack](MSCP_Overview.md#5-safety-mechanisms)

-   :material-math-integral:{ .lg .middle } **Explicit Mathematical Contracts**

    ---

    Definitions and conditional propositions with stated assumptions, proof sketches, and limitations; not a general safety or convergence certification.

    [:octicons-arrow-right-24: Mathematical Analysis](MSCP_Overview.md#6-mathematical-analysis)

</div>

---

## Agent Cognition Levels

These are research categories, not certified capabilities. "Prototype" refers to reference work described by the project, not independent qualification. See [Status and Validation](specs/Documentation_Status.md) for the public evidence boundary.

| Level | Name | Self-Awareness | Key Capability | Status |
|:-----:|------|:--------------:|----------------|:------:|
| **1** | [Tool Agent](levels/Level_1_Tool_Agent.md) | No persistent reflexive model | Bounded tool invocation | Educational sample |
| **2** | [Autonomous Agent](levels/Level_2_Autonomous_Agent.md) | No reflexive change regulation | Persistent state, goals, authorized continuation | Educational sample |
| **3** | [Self-Regulating Agent](levels/Level_3_Self_Regulating_Agent.md) | Structural | MSCP core loop, versioned self-model | Prototype described |
| **4** | [Adaptive General Agent](levels/Level_4_Adaptive_General_Agent.md) | Structural + reflective | Cross-domain transfer, bounded self-modification | Prototype described |
| **4.5** | [Self-Architecting](levels/Level_4_5_Self_Architecting.md) | Architectural | Self-projection, architecture recomposition | Prototype described |
| **4.8** | [Strategic Self-Modeling](levels/Level_4_8_Strategic_Self_Modeling.md) | Strategic design | Probabilistic world model, strategic planning | Research criteria |
| **4.9** | [Autonomous Strategic](levels/Level_4_9_Autonomous_Strategic_Agent.md) | Autonomous strategic design | Value-change auditing, multi-agent reasoning | Research criteria |
| **5** | [Proto-AGI](levels/Level_5_Proto_AGI.md) | Extended structural design | Held-out generalization, validated reconstruction | Research criteria |

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

## Quick Start

Dive into the documentation:

1. **[MSCP Overview](MSCP_Overview.md)** - Complete framework specification
2. **[Level Series](levels/README.md)** - Navigation index with cumulative safety summary
3. **[Level 3: Self-Regulating Agent](levels/Level_3_Self_Regulating_Agent.md)** - The core MSCP level (start here for technical depth)
4. **[Glossary](specs/MSCP_Glossary.md)** - Master index of formal definitions, propositions, acronyms, symbols, and notation cautions (AS / EU duality, ASS thresholds)

---

## Author

**Moon Hyuk Choi** - [moonchoi@microsoft.com](mailto:moonchoi@microsoft.com)  
Microsoft Cloud & AI Apps CSA

---

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/dotnetpower/mscp/blob/main/LICENSE) file for details.

<p style="text-align: center; color: var(--md-default-fg-color--lighter); margin-top: 2em;">
  <em>This documentation was written with the assistance of <a href="https://github.com/features/copilot">GitHub Copilot</a>.</em>
</p>
