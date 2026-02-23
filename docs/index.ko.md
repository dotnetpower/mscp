---
title: "홈"
description: "MSCP - 구조적 자기인식 AI 에이전트를 위한 안전 지향 프레임워크. 6단계 인지 분류 체계, 16계층 인지 아키텍처, 30개 이상의 안전 메커니즘, 144편의 학술 참고문헌."
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
  **구조적 자기인식 AI 에이전트를 위한 안전 지향 프레임워크**
</p>

<p align="center" markdown>

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/dotnetpower/mscp/blob/main/LICENSE)
[![Status: Research](https://img.shields.io/badge/Status-Research-orange.svg)](#)
[![Docs: 9 Documents](https://img.shields.io/badge/Docs-9_Documents-green.svg)](MSCP_Overview.ko.md)
[![References: 144 Papers](https://img.shields.io/badge/References-144_Papers-blueviolet.svg)](MSCP_Overview.ko.md#10-참고문헌)
[![Levels: L1–L5](https://img.shields.io/badge/Levels-L1–L5-informational.svg)](levels/README.ko.md)
[![Safety: 30+ Mechanisms](https://img.shields.io/badge/Safety-30%2B_Mechanisms-red.svg)](MSCP_Overview.ko.md#5-안전-메커니즘)

</p>

!!! note "독립적 연구"
    이 프로젝트는 **독립적인 개인 연구 프로젝트**입니다. 어떤 조직의 입장이나 공식 업무를 대표하지 않습니다. 핵심 동기는 AI 에이전트가 더 강력한 능력을 갖추면서도 **안전하고, 예측 가능하며, 인간의 가치에 부합하는** 방법을 탐구하는 것입니다.

---

## MSCP란 무엇인가?

**최소 자기의식 프로토콜(MSCP)**은 *안전한 구조적 자기인식*을 갖춘 AI 에이전트를 구축하기 위한 구조화된 프로토콜입니다 - 자신의 상태 변화를 예측하고, 예측을 결과와 비교하며, 제한된 안전 범위 내에서만 자기 자신을 업데이트하는 능력을 말합니다.

에이전트가 목표를 설정하고, 전략을 수정하며, 자기 개선하는 능력을 갖추게 되면, **어떻게 안정적이고, 정렬되며, 예측 가능하게 유지할 수 있을까요?** MSCP는 다음 원칙으로 이에 답합니다:

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

    정체성 연속성, 예측 기반 행동 게이트, 델타 제한 업데이트, 리아프노프 수렴, 윤리적 불변량 등.

    [:octicons-arrow-right-24: 안전 스택](MSCP_Overview.ko.md#5-안전-메커니즘)

-   :material-math-integral:{ .lg .middle } **엄밀한 형식화**

    ---

    71개의 형식적 정의, 7개의 명제, 4개의 정리와 증명 스케치 - 출판 수준의 수학적 엄밀성.

    [:octicons-arrow-right-24: 수학적 분석](MSCP_Overview.ko.md#6-수학적-분석)

</div>

---

## 에이전트 인지 레벨

| 레벨 | 명칭 | 자기인식 | 핵심 역량 | 상태 |
|:-----:|------|:---------:|-----------|:----:|
| **1** | [도구 에이전트](levels/Level_1_Tool_Agent.ko.md) | 없음 | 결정적 도구 호출 | 기준선 |
| **2** | [자율 에이전트](levels/Level_2_Autonomous_Agent.ko.md) | 없음 | 세계 모델, 자율 목표 | 정의됨 |
| **3** | [자기조절 에이전트](levels/Level_3_Self_Regulating_Agent.ko.md) | 구조적 | 16계층 아키텍처, MSCP 핵심 루프 | 구현됨 |
| **4** | [적응형 범용 에이전트](levels/Level_4_Adaptive_General_Agent.ko.md) | 구조적 + 반영적 | 교차 도메인 전이, 자기수정 | 구현됨 |
| **4.5** | [자기설계](levels/Level_4_5_Self_Architecting.ko.md) | 아키텍처적 | 자기투영, 아키텍처 재구성 | 구현됨 |
| **4.8** | [전략적 자기모델링](levels/Level_4_8_Strategic_Self_Modeling.ko.md) | 아키텍처적 + 전략적 | 확률적 세계 모델, 전략 계획 | 설계 |
| **4.9** | [자율 전략](levels/Level_4_9_Autonomous_Strategic_Agent.ko.md) | 아키텍처적 + 자율적 | 가치 진화, 다중 에이전트 추론 | 설계 |
| **5** | [프로토-AGI](levels/Level_5_Proto_AGI.ko.md) | 완전 | 교차 도메인 일반화, 자기재구성 | 연구 |

---

## 핵심 설계 원칙

| # | 원칙 | 설명 |
|:-:|------|------|
| 1 | **LLM 텍스트 기반 자기수정 금지** | 모든 자기수정은 구조화된 수치 연산을 사용하며, LLM 생성 텍스트는 사용하지 않음 |
| 2 | **예측 없는 행동 금지** | 모든 행동은 비교를 위한 예측 스냅샷을 필요로 함 |
| 3 | **델타 제한 업데이트** | 모든 자기수정은 최대 델타 값으로 제한됨 |
| 4 | **정체성 연속성** | 결정적 정체성 해싱과 드리프트 탐지 및 롤백 |
| 5 | **윤리적 불변성** | 레이어 0 제약은 불변이며 LLM에 독립적 |
| 6 | **리아프노프 수렴** | 자기수정이 수렴한다는 수학적 보장 |

---

## 안전 메커니즘 스택

```
레이어 0 ─ 불변 윤리적 불변량 (규칙 기반, LLM 의존 없음)
레이어 1 ─ 핵심 가치 잠금 (SHA-256 해시 검증)
레이어 2 ─ 델타 제한 자기 업데이트 (단계당 최대 Δ)
레이어 3 ─ 메타 에스컬레이션 가드 (임계값 위반 시 롤백)
레이어 4 ─ 예측 기반 행동 게이트 (예측 → 비교 → 업데이트)
레이어 5 ─ 리아프노프 수렴 모니터 (진동 감지)
레이어 6 ─ 인지 예산 컨트롤러 (우아한 성능 저하)
레이어 7 ─ 정서 안전 (감정 범위, 의사결정 지배 방지)
레이어 8 ─ 생존 본능 범위 (우선순위 상한, 윤리적 검증)
```

---

## 빠른 시작

문서 탐색하기:

1. **[MSCP 개요](MSCP_Overview.ko.md)** - 전체 프레임워크 명세
2. **[레벨 시리즈](levels/README.ko.md)** - 누적 안전 요약이 포함된 탐색 색인
3. **[레벨 3: 자기조절 에이전트](levels/Level_3_Self_Regulating_Agent.ko.md)** - MSCP 핵심 레벨 (기술적 깊이를 원하면 여기서 시작)

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
