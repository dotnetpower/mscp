---
title: "Documentation Status and Validation"
description: "Public evidence, qualification limits, terminology, and validation rules for the MSCP research specification."
---

# Documentation Status and Validation

**Documentation review date: 2026-11-03.** This date identifies a documentation revision, not a new experiment or a certification of the reference implementation.

## What the public documents establish

MSCP is an experimental architecture and protocol for **structural self-awareness**: representing, predicting, and regulating an agent's own state changes. The project name does not assert subjective experience, phenomenal consciousness, or achieved AGI. L4.5, L4.8, and L4.9 are intermediate research stages; L6 is a speculative boundary, not a documented engineering milestone.

| Scope | Design documented | Public implementation evidence | Qualification evidence |
|-------|:-----------------:|--------------------------------|------------------------|
| L1–L2 | Yes | Educational CLI samples in this repository | Samples illustrate mechanisms, not universal level certification |
| L3–L4.5 | Yes | Reference prototypes described in the research documents | No independent level qualification is established by these documents |
| L4.8–L5 | Research criteria | Internal implementation details are outside the public specification | No independently validated achievement is claimed |
| L6 | Speculative discussion | None established here | No consciousness or AGI qualification claimed |

Use four distinct labels when reporting progress:

- **Designed:** a contract or architecture is specified.
- **Implemented:** the mechanism exists in a named, reviewed implementation scope.
- **Tested:** named tests passed against a specified revision and environment.
- **Experimentally validated:** a preregistered evaluation reports its dataset, baseline, uncertainty, limitations, and results.

These labels are not interchangeable. Code availability, a passing test, or a composite score alone does not establish all admission criteria for a level. Unpublished evidence must be marked **not publicly established**, not inferred from private implementation activity.

## Reading mathematical claims

The defining section in each level document is authoritative; the glossary and home page are summaries.

- A bounded update limits a step or finite-horizon exposure. It does not imply convergence or bounded lifetime drift.
- A composite monitoring index is not automatically a Lyapunov function. A stability theorem needs a defined dynamical system, equilibrium, assumptions, and an appropriate decrease condition.
- A hash verifies canonical representation integrity and ancestry, not semantic similarity.
- Entropy differences and output divergence are diagnostics, not proofs of autonomy or independent decision authority.
- A diagnostic mean or geometric mean cannot override a failed mandatory gate.
- Numerical thresholds, weights, budgets, and windows are illustrative research settings unless accompanied by a declared calibration and evaluation profile.
- An invariant-preservation claim is conditional on complete mediation, validated initial state, and integrity of the policy, monitor, and recovery journal. It does not cover every deployment failure.

## Public disclosure boundary

Publish behavior contracts, assumptions, evaluation methodology, and limitations that have been approved for disclosure. Keep implementation locations, private identifiers, credentials, operational logs, raw evaluation data, deployment settings, internal tuning values, and unpublished capability claims outside this repository.

Draft updates from an approved public summary, not by copying private source or change logs. Before publication, review prose, diagrams, examples, generated HTML, and repository changes for accidental disclosure. Automated checks supplement this review; they cannot prove that a document contains no confidential information.

## Korean terminology

| English | Korean | Usage |
|---------|--------|-------|
| Minimal Self-Consciousness Protocol | 최소 자기의식 프로토콜 | Project name |
| Structural self-awareness | 구조적 자기인식 | Engineering property, not subjective consciousness |
| Self-model | 자기 모델 | Structured representation of the agent |
| Self-modification | 자기 수정 | Changes admitted under explicit constraints |
| Invariant | 불변 조건 | A predicate that must remain satisfied |
| Integrity / semantic continuity | 무결성 / 의미적 연속성 | Distinct properties; do not conflate them |
| Graceful degradation | 핵심 안전 기능을 유지하는 단계적 기능 축소 | Reduced capabilities under resource constraints |
| Persisted prediction | 저장된 예측 기록 | A prediction recorded before execution |

## Documentation checks

From the repository root:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-docs.txt
npm ci
.venv/bin/mkdocs build --strict
.venv/bin/python scripts/check_docs.py
.venv/bin/mkdocs serve --dev-addr 127.0.0.1:8000
```

The checker validates generated local links and fragments, parses every generated math item with the configured KaTeX version, checks bilingual equation parity, and runs numerical regression checks for the corrected diagnostics. These checks do not prove the protocol's safety or empirical performance.

For browser review, check both languages, desktop and narrow layouts, and instant navigation. No math error markers or unrendered math wrappers should remain after the page initializes.
