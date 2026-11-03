---
title: "홈"
description: "MSCP: 구조적 자기인식을 갖춘 에이전트를 위한 실험적 프레임워크. 안전 가정, 연구 기준, 검증 한계를 명시합니다."
---

<!--
Copyright (c) 2026 Moon Hyuk Choi
Licensed under the MIT License.
See LICENSE file in the repository root for full license information.

Redistribution (commercial or non-commercial) must retain this notice.
Removal of attribution constitutes a license violation.
-->

# MSCP - 최소 자기의식 프로토콜

<p align="center" style="font-size: 1.2em; color: var(--md-default-fg-color--light);" markdown>
  **구조적 자기인식을 갖춘 AI 에이전트를 위한 안전 지향 프레임워크**
</p>

<p align="center" markdown>

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/dotnetpower/mscp/blob/main/LICENSE)
[![Status: Research](https://img.shields.io/badge/Status-Research-orange.svg)](#)
[![Docs: Bilingual](https://img.shields.io/badge/Docs-English%20%2F%20Korean-green.svg)](MSCP_Overview.ko.md)
[![References: 144 Papers](https://img.shields.io/badge/References-144_Papers-blueviolet.svg)](MSCP_Overview.ko.md#10-참고문헌)
[![Levels: L1–L5](https://img.shields.io/badge/Levels-L1–L5-informational.svg)](levels/README.ko.md)
[![Safety: 30+ Mechanisms](https://img.shields.io/badge/Safety-30%2B_Mechanisms-red.svg)](MSCP_Overview.ko.md#5-안전-메커니즘)

</p>

!!! note "독립적 연구"
    이 프로젝트는 **독립적인 개인 연구 프로젝트**입니다. 어떤 조직의 입장이나 공식 업무를 대표하지 않습니다. 핵심 동기는 AI 에이전트가 더 강력한 능력을 갖추면서도 **안전하고, 예측 가능하며, 인간의 가치에 부합하는** 방법을 탐구하는 것입니다.

---

## MSCP란 무엇인가?

**최소 자기의식 프로토콜(MSCP)**은 에이전트가 자신의 상태 변화를 예측하고 실제 결과와 비교하며, 정해진 안전 제약 안에서만 내부 상태를 갱신하도록 하는 실험적 프로토콜입니다. 여기서 *구조적 자기인식*은 공학적인 동작 특성을 뜻하며, 주관적 의식의 존재를 주장하지 않습니다.

에이전트가 스스로 목표와 전략을 바꿀 수 있게 될 때, **어떻게 안정성과 예측 가능성을 유지하고 인간의 의도에 부합하도록 할 수 있을까요?** MSCP는 다음 원칙에서 출발합니다.

!!! quote "핵심 원칙"
    **안전은 능력의 적이 아니라 전제 조건이다.**

---

## 주요 기여

<div class="grid cards" markdown>

-   :material-layers-triple:{ .lg .middle } **6단계 인지 분류 체계**

    ---

    반응형 도구 에이전트(L1)부터 프로토-AGI(L5)까지, 모든 단계에서 측정 가능한 전환 기준과 형식적 정의를 제공합니다.

    [:octicons-arrow-right-24: 레벨 탐색](levels/README.ko.md)

-   :material-view-module:{ .lg .middle } **16계층 인지 아키텍처**

    ---

    지각부터 메타인지 제어까지 아우르는 독립적으로 테스트 가능한 조합형 모듈.

    [:octicons-arrow-right-24: 아키텍처 상세](MSCP_Overview.ko.md#4-아키텍처-다층-인지-스택)

-   :material-shield-check:{ .lg .middle } **30개 이상의 안전 메커니즘**

    ---

    의미적 연속성, 예측 기반 행동 승인, 갱신량 제한, 조건부 위험 모니터링, 불변 조건 검사 등을 다룹니다.

    [:octicons-arrow-right-24: 안전 스택](MSCP_Overview.ko.md#5-안전-메커니즘)

-   :material-math-integral:{ .lg .middle } **가정이 명시된 수학적 계약**

    ---

    정의와 조건부 명제에 가정, 증명 개요, 적용 한계를 명시합니다. 일반적인 안전성이나 수렴을 인증하는 것은 아닙니다.

    [:octicons-arrow-right-24: 수학적 분석](MSCP_Overview.ko.md#6-수학적-분석)

</div>

---

## 에이전트 인지 레벨

다음 표는 인증된 역량이 아니라 연구상의 분류입니다. ‘프로토타입 서술’은 프로젝트에서 설명한 참조 구현을 뜻하며, 독립적인 단계 검증과 구분합니다. 자세한 근거 범위는 [문서 상태와 검증 기준](specs/Documentation_Status.ko.md)을 참고하십시오.

| 레벨 | 명칭 | 자기인식 | 핵심 역량 | 상태 |
|:-----:|------|:---------:|-----------|:----:|
| **1** | [도구 에이전트](levels/Level_1_Tool_Agent.ko.md) | 지속적인 자기 성찰 모델 없음 | 실행 범위가 제한된 도구 호출 | 교육용 예제 |
| **2** | [자율 에이전트](levels/Level_2_Autonomous_Agent.ko.md) | 자기 변화 제어 모델 없음 | 지속 상태, 목표, 승인된 후속 실행 | 교육용 예제 |
| **3** | [자기조절 에이전트](levels/Level_3_Self_Regulating_Agent.ko.md) | 구조적 | MSCP 핵심 루프, 버전이 명시된 자기 모델 | 프로토타입 서술 |
| **4** | [적응형 범용 에이전트](levels/Level_4_Adaptive_General_Agent.ko.md) | 구조적·성찰적 | 교차 도메인 전이, 범위가 제한된 자기 수정 | 프로토타입 서술 |
| **4.5** | [자기설계](levels/Level_4_5_Self_Architecting.ko.md) | 아키텍처 수준 | 자기 투영, 아키텍처 재구성 | 프로토타입 서술 |
| **4.8** | [전략적 자기모델링](levels/Level_4_8_Strategic_Self_Modeling.ko.md) | 전략적 설계 | 확률적 세계 모델, 전략 계획 | 연구 기준 |
| **4.9** | [자율 전략](levels/Level_4_9_Autonomous_Strategic_Agent.ko.md) | 자율 전략 설계 | 가치 변화 감사, 다중 에이전트 추론 | 연구 기준 |
| **5** | [프로토-AGI](levels/Level_5_Proto_AGI.ko.md) | 확장된 구조적 설계 | 미사용 평가 데이터에서의 일반화, 검증된 재구성 | 연구 기준 |

---

## 핵심 설계 원칙

| # | 원칙 | 설명 |
|:-:|------|------|
| 1 | **자기 수정의 독립적 승인** | LLM은 후보를 제안할 수 있지만, 자료형과 제약을 검증한 갱신만 적용 |
| 2 | **예측 없는 행동 금지** | 모든 행동은 비교를 위한 예측 스냅샷을 필요로 함 |
| 3 | **델타 제한 업데이트** | 모든 자기수정은 최대 델타 값으로 제한됨 |
| 4 | **정체성 연속성** | 의미 변화의 관측과 무결성·변경 이력 검증을 구분 |
| 5 | **윤리적 불변성** | 레이어 0 제약은 불변이며 LLM에 독립적 |
| 6 | **조건부 위험 변화량 제한** | 명시한 가정 아래 변화량을 제한하며, 무조건적인 수렴은 주장하지 않음 |

---

## 안전 메커니즘 스택

```
레이어 0 ─ 변경할 수 없는 윤리적 조건 (규칙 기반, LLM 의존 없음)
레이어 1 ─ 핵심 가치 잠금 (SHA-256 해시 검증)
레이어 2 ─ 델타 제한 자기 업데이트 (단계당 최대 Δ)
레이어 3 ─ 메타 에스컬레이션 가드 (임계값 위반 시 롤백)
레이어 4 ─ 예측 기반 행동 게이트 (예측 → 비교 → 업데이트)
레이어 5 ─ 종합 위험 모니터 (조건부 변화량 제한, 진동 신호 관측)
레이어 6 ─ 인지 예산 제어기 (핵심 안전 기능을 유지하며 기능 축소)
레이어 7 ─ 범위가 제한된 운영 조절 (권한 확대 금지)
레이어 8 ─ 항상성 안전 (정책 안에서 복구, 외부 중단 명령 우선)
```

---

## 빠른 시작

문서 탐색하기:

1. **[MSCP 개요](MSCP_Overview.ko.md)** - 전체 프레임워크 명세
2. **[레벨 시리즈](levels/README.ko.md)** - 누적 안전 요약이 포함된 탐색 색인
3. **[레벨 3: 자기조절 에이전트](levels/Level_3_Self_Regulating_Agent.ko.md)** - MSCP 핵심 레벨 (기술적 깊이를 원하면 여기서 시작)
4. **[용어집](specs/MSCP_Glossary.md)** - 형식적 정의·명제·약어·기호 마스터 색인 및 표기 주의 사항 (AS / EU 이중 의미, ASS 임계값)

---

## 저자

**최문혁 (Moon Hyuk Choi)** - [moonchoi@microsoft.com](mailto:moonchoi@microsoft.com)  
Microsoft Cloud & AI Apps CSA

---

## 라이선스

이 프로젝트는 MIT 라이선스에 따라 라이선스가 부여됩니다 - 자세한 내용은 [LICENSE](https://github.com/dotnetpower/mscp/blob/main/LICENSE) 파일을 참조하십시오.

<p style="text-align: center; color: var(--md-default-fg-color--lighter); margin-top: 2em;">
  <em>이 문서는 <a href="https://github.com/features/copilot">GitHub Copilot</a>의 도움을 받아 작성되었습니다.</em>
</p>
