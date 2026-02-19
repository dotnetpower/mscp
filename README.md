# MSCP — Minimal Self-Consciousness Protocol

> **A Safety-Oriented Framework for Structurally Self-Aware AI Agents**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> **Note**: This is an **independent personal research project**. It does not represent the views or official work of any organization. The core motivation is to explore how AI agents can grow more capable **while remaining safe, predictable, and aligned with human values**. This is still very much a work in progress — expect things to evolve as experimentation continues.

---

## Overview

The **Minimal Self-Consciousness Protocol (MSCP)** is a structured protocol for building AI agents with *safe structural self-awareness* — the capacity to predict their own state changes, compare predictions against outcomes, and update themselves only within bounded safety envelopes.

MSCP grew out of a simple question: as agents gain the ability to set goals, modify strategies, and self-improve, **how do we keep them stable, aligned, and predictable?** The project is driven by the belief that **safety is not the enemy of capability — it is its prerequisite.** AI agents must evolve in a direction that is fundamentally safe by design, not merely powerful.

## What We've Found So Far

- **Six-Level Agent Cognition Taxonomy** — from reactive Tool Agents (L1) to hypothetical Conscious Entities (L6), with measurable transition criteria
- **16-Layer Cognitive Architecture** — composable, independently testable modules spanning perception through meta-cognitive control
- **30+ Structural Safety Mechanisms** — identity continuity, prediction-gated actions, delta-clamped updates, Lyapunov convergence, ethical invariants, and more
- **Mathematical Analysis** — exploring bounds on identity drift, convergence behavior, and ethical constraint preservation

## Agent Cognition Levels

> **Note**: The "Status" column reflects the implementation state within this personal project's reference implementation, not an industry-wide standard.

| Level | Name | Self-Awareness | Status |
|:-----:|------|:--------------:|:------:|
| 1 | Tool Agent | None | Baseline |
| 2 | Autonomous Agent | None | Defined |
| 3 | Self-Regulating Cognitive Agent | Structural | Implemented |
| 4 | Adaptive General Agent | Structural + Reflective | Implemented |
| 4.5 | Directionally Self-Architecting | Architectural | Implemented |
| 4.8 | Strategic Self-Modeling Agent | Architectural + Strategic | Design |
| 4.9 | Autonomous Strategic Agent | Architectural + Autonomous | Design |
| 5 | Proto-AGI | Full | Research |
| 6 | Strong AGI / Conscious Entity | Phenomenal | Theoretical |

## Documentation

- **[MSCP Overview](docs/MSCP_Overview.md)** — *"Minimal Self-Consciousness Protocol for Agentic AI: A Safety-Oriented Internal Framework"*

### Per-Level Architecture Documents

Detailed architecture specifications with Mermaid diagrams, pseudocode, and safety analysis for each cognitive level:

- **[Level Series Overview](docs/levels/README.md)** — Navigation index and cumulative safety summary
- **[Level 1: Tool Agent](docs/levels/Level_1_Tool_Agent.md)** — Stateless tool invocation, intent routing
- **[Level 2: Autonomous Agent](docs/levels/Level_2_Autonomous_Agent.md)** — World model, autonomous goals, emotion detection
- **[Level 3: Self-Regulating Agent](docs/levels/Level_3_Self_Regulating_Agent.md)** — 16-layer architecture, MSCP v1–v4, triple-loop meta-cognition
- **[Level 4: Adaptive General Agent](docs/levels/Level_4_Adaptive_General_Agent.md)** — Cross-domain transfer, capability expansion, bounded self-modification
- **[Level 4.5: Pre-AGI Self-Architecting](docs/levels/Level_4_5_Self_Architecting.md)** — Self-projection (SEOF), architecture recomposition, existential guard
- **[Level 4.8: Strategic Self-Modeling](docs/levels/Level_4_8_Strategic_Self_Modeling.md)** — World model integration, meta-cognitive self-model, strategic planning
- **[Level 4.9: Autonomous Strategic Agent](docs/levels/Level_4_9_Autonomous_Strategic_Agent.md)** — Autonomous goal generation, value evolution, resource survival, multi-agent reasoning
- **[Level 5: Proto-AGI](docs/levels/Level_5_Proto_AGI.md)** — Persistent identity, cross-domain generalization, self-reconstruction

## Core Design Principles

1. **No LLM-Text-Based Self-Modification** — All self-modifications use structured numerical operations, never LLM-generated text
2. **No Action Without Prediction** — Every action requires a prediction snapshot for comparison
3. **Delta-Clamped Updates** — All self-modifications are bounded by maximum delta values
4. **Identity Continuity** — Deterministic identity hashing with drift detection and rollback

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

> 📝 This documentation was written with the assistance of [GitHub Copilot](https://github.com/features/copilot).
