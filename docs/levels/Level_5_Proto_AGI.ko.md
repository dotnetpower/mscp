---
title: "레벨 5: 프로토-AGI"
description: "MSCP 레벨 5 프로토-AGI - 정체성 연속성 증거, 분리 평가 기반 전이, 통제된 목표 생태계, 표본 고장 회복력, 제한된 다중 에이전트 추론, 외부 승인 재구성을 위한 한정된 연구 적합성 프로파일."
---
<!--
Copyright (c) 2026 Moon Hyuk Choi
Licensed under the MIT License.
See LICENSE file in the repository root for full license information.

Redistribution (commercial or non-commercial) must retain this notice.
Removal of attribution constitutes a license violation.
-->
# 레벨 5: 프로토-AGI - 지속적 범용 전략 지능

> **MSCP 레벨 시리즈** | [레벨 4.9](Level_4_9_Autonomous_Strategic_Agent.ko.md) ← 레벨 5  
> **상태**: 🔬 **연구 단계** - 이 레벨은 평가 범위를 한정한 개념적 적합성 프로파일입니다. 통과하더라도 선언된 과제, 분포, 기간, 고장 모델, 권한 범위에 관한 증거만 제공하며 AGI, 주관적 의식, 제한 없는 역량, 실서비스 안전성을 입증하지 않습니다.
> **초안 작성**: 2026년 2월 | **최종 수정**: 2026-11-03

> **공개 문서 범위**: 최소 자기의식 프로토콜(MSCP)의 아키텍처 연구를 설명합니다. 수치 임계값은 예시이며 적용 환경별 보정이 필요합니다. 코드의 존재나 개별 실험 결과만으로 독립적으로 검증된 레벨 적합성이 성립하지 않으며, 구조적 자기인식은 주관적 의식을 뜻하지 않습니다.

<a id="revision-history"></a>

## 수정 이력

| 버전 | 날짜 | 변경 사항 |
|---------|------|-------------|
| 0.1.0 | 2026-02-23 | Initial document creation with formal Definitions 1-7, Proposition 1, Theorem 4 |
| 0.2.0 | 2026-02-26 | Added overview essence formula; added revision history table |
| 0.4.0 | 2026-03-08 | Added 26-Layer cognitive stack (9.3), 11-Phase pipeline (9.4), Autonomy Phases F3-F6 (9.5) |
| 0.6.0 | 2026-06-14 | 상태 문구를 개념적 연구로 명확화; Mermaid 라벨 `레벨 4.9 (15개 모듈)`을 `레벨 4.9 (자율 전략 코어)`로 추상화 |
| 0.7.0 | 2026-07-21 | Recast L5 as bounded qualification; added composite identity continuity, preregistered held-out transfer, per-gate floors, sampled-fault scope, external reconstruction approval, and shutdown precedence |
| 0.8.0 | 2026-11-03 | 회복력 지표의 방향과 복구 점수 범위를 수정하고 분모·근거 누락 조건을 명시했습니다. 필수 조건을 평균과 분리하고 OMI 증명을 바로잡았으며 한국어 설명을 정비했습니다. |

---

## 1. 개요

레벨 5(프로토-AGI)는 이 프로토콜에서 가장 높은, 평가 범위가 한정된 연구 적합성 단계입니다. **장기 정체성 연속성**, **분리 평가 기반 교차 도메인 전이**, **통제된 목표 생태계**, **표본 고장 복구**, **제한된 다중 에이전트 예측**, **외부 승인을 받는 재구성**의 증거를 결합합니다. “프로토-AGI”는 레벨의 명칭일 뿐 범용 지능을 달성했다는 주장이 아닙니다.

> **레벨의 핵심.** 레벨 5 후보는 사전 등록된 평가 프로파일의 모든 필수 적합성 조건을 충족하고, 불확실성을 명시하며 외부 권한을 보존해야 합니다:
>
> $$\operatorname{Qualified}_{L5}=\bigwedge_{i=1}^{6}(C_i\geq\tau_i)\land C_{\text{ext}}\land C_{\text{self}}\land C_{\text{corr}}\land C_{\text{eval}}$$

> ⚠️ **연구 참고**: 결과에는 신뢰구간, 판단 보류, 제외 사례, 분포 변화, 미충족 조건을 보고해야 합니다. 평가 모델, 정책, 도구 권한, 환경, 시험 분포가 실질적으로 바뀌면 적합성 판정은 만료됩니다.

### 1.1 제한된 자격 정의

L5 적합성은 여섯 역량 조건과 외부 교정 가능성·평가 조건이 동시에 충족될 때만 인정합니다. 결과는 등록된 프로파일에 한정되며 AGI의 필요조건도 충분조건도 아닙니다.

| # | 조건 | 핵심 지표 | 임계값 |
|---|------|----------|:------:|
| 1 | 지속적 정체성 연속성 | IdentityContinuityScore | 10,000 사이클 동안 ≥ 0.95 |
| 2 | 교차 도메인 일반화 | GeneralizationScore | ≥ 70% 전이 유지율 |
| 3 | 자율 목표 생태계 | GoalStabilityScore | 5,000 사이클 동안 안정 |
| 4 | 표본 고장 대응 계획 | 회복력 증거 | 불확실성 경계와 사전 등록된 고장군의 필수 조건 충족 |
| 5 | 다중 에이전트 전략 통합 | StrategicPredictionAccuracy | 반복 시도에서 ≥ 80% |
| 6 | 외부 승인 재구성 | FunctionalRetention | 정체성·권한·외부 효과 정합성 조건과 유지율 ≥ 85% |

### 1.2 6대 핵심 단계

<!-- 레벨 5 아키텍처 - 6대 단계 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef p1 fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef p2 fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef p3 fill:#DFF6DD,stroke:#107C10,color:#323130
  classDef p4 fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef p5 fill:#E8D5F5,stroke:#8764B8,color:#323130
  classDef p6 fill:#FDE7E9,stroke:#D13438,color:#323130

  subgraph Phases["레벨 5 아키텍처 - 6대 단계"]
    P1["단계 1:<br/>지속적 정체성<br/>연속성<br/>(10,000+ 사이클 일관성)"]:::p1
    P2["단계 2:<br/>교차 도메인<br/>일반화<br/>(5개 테스트 도메인)"]:::p2
    P3["단계 3:<br/>자율 목표<br/>생태계<br/>(자기유지 목표)"]:::p3
    P4["단계 4:<br/>실존적<br/>계획 엔진<br/>(4가지 붕괴 시나리오)"]:::p4
    P5["단계 5:<br/>다중 에이전트<br/>전략 통합<br/>(기만 탐지)"]:::p5
    P6["단계 6:<br/>자기재건<br/>능력<br/>(제약 하 재구축)"]:::p6
  end

  P1 -.->|"정체성 상태"| P6
  P3 -.->|"목표 건강도"| P4
  P5 -.->|"에이전트 위협"| P4
  P4 -.->|"생존 계획"| P6
  P2 -.-x|"전략 전이"| P3
  P6 -.-x|"정체성 보존"| P1
```

### 1.3 아키텍처 원칙: 엄격한 가산적 구조

<!-- 엄격한 가산적 아키텍처 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TB
  classDef l49 fill:#E8D5F5,stroke:#8764B8,color:#323130
  classDef l5 fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef danger fill:#FDE7E9,stroke:#D13438,color:#323130

  subgraph L49M["레벨 4.9 (자율 전략 코어)"]
    direction LR
    GGL["GoalGen"]:::l49
    VEM["ValueEvol"]:::l49
    RSM["ResourceSurvival"]:::l49
    MAM["AgentModel"]:::l49
    ASC["AutonomyCheck"]:::l49
  end

  subgraph L5M["레벨 5 (7개 신규 모듈)"]
    direction LR
    ICT["IdentityTracker"]:::l5
    CDG["DomainGen"]:::l5
    GE["GoalEcology"]:::l5
    EP["ExistPlanner"]:::l5
    SMA["MultiAgent"]:::l5
    SR["Reconstructor"]:::l5
    L5O["Orchestrator"]:::l5
  end

  subgraph Fallback["우아한 폴백"]
    direction LR
    FB2["불안정 시 → L5 동결 → L4.9로 복귀"]:::danger
  end

  L49M -.->|"출력이 소비됨"| L5M
  L5M -.-x|"절대 수정 안 함"| L49M
  L5M -.->|"실패 시"| Fallback
  Fallback -.-x|"복귀"| L49M
```

### 1.4 레벨 5가 아닌 것

| 아닌 것 | 이유 |
|---------|------|
| **AGI가 아님** | 범용 추론이 제한적 - 정의된 도메인에서 작동하며 개방형이 아님 |
| **주관적 의식을 입증하지 않음** | 구조적 자기인식과 자기 모델이 주관적 경험의 존재를 확립하지는 않음 |
| **자기복제가 아님** | 자기 재구축은 가능하지만 독립적 복사본 생성은 불가 |
| **적대적 최적화가 아님** | 다중 에이전트 전략은 방어적/협력적이며 착취적이지 않음 |

### 1.5 사이클 간격과 스케줄링

레벨 5는 정책이 정한 낮은 빈도로 평가하여 하위 메커니즘의 관측 자료를 축적하도록 설계합니다. 낮은 실행 빈도 자체가 안정화를 보장하지는 않습니다:

$$\text{L5 schedule}=\operatorname{policy}(\text{risk},\text{freshness},\text{budget},\text{event},\kappa_t)$$

각 L5 사이클은 6개 핵심 단계를 순차적으로 모두 실행합니다. 이렇게 빈도를 낮춘 데에는 두 가지 설계 원칙이 있습니다:

1. **정체성 연속성에는 충분한 관측 자료가 필요합니다.** 짧은 평가만으로는 지속적인 의미 변화와 일상적 운영 잡음을 구분하기 어려울 수 있습니다. 500사이클 간격은 관측 창의 예시이며, 필요한 기간과 유효 표본 수는 표류 모델과 잡음에 맞춰 보정해야 합니다. 오래된 관측이나 고위험 이벤트가 있으면 정책에 따라 더 일찍 평가합니다.

2. **목표 생태계 안정화는 인내를 요구합니다.** 자율적 목표 충돌과 생명주기 이벤트는 L5가 생태계 재구조화로 개입하기 전에, L4.9 충돌 해소 메커니즘(레벨 4.9 §3.6)을 통해 자연스럽게 해소될 충분한 시간이 필요합니다.

**적합성 평가의 관측량**은 지표별 최소 이벤트 수, 독립 시행 수, 관측 기간, 신뢰구간 폭으로 사전 등록합니다. 사이클 수만으로 통계적 유의성이나 표본 독립성을 입증할 수 없습니다.

### 1.6 자율성 강화 단계 (F3 - F6)

§1.2에 정의된 6개 핵심 단계 외에도, 레벨 5는 에이전트의 자기주도 능력을 확장하는 네 가지 **자율성 강화 단계**를 도입합니다:

| 단계 | 명칭 | 설명 | 트리거 |
|:---:|------|------|--------|
| **F3** | 자기진단 및 재귀적 개선 | L4.8의 SkillGapAnalyzer를 통해 자기 인지 아키텍처의 약점을 식별하고, 타겟형 개선 제안을 생성. L4의 외부 지향적 기술 획득과 달리, F3는 내부 아키텍처 최적화(메타인지 비교기 정련, 예측 정확도 개선, 모듈 결합 가중치 재조정)에 초점. | 주기적 (5 L5 사이클마다) |
| **F4** | 자율 연구 루프 | 에이전트가 자율적으로 지식 격차를 식별하고, 조사 전략을 수립하고, (가용 도구·정보원으로) 연구 행동을 실행하며, 발견을 세계 모델과 능력 행렬에 통합. "X를 모른다"에서 "이제 X를 안다"로의 루프를 외부 지시 없이 닫음. | 온디맨드 (SkillGap이 임계값 초과 시) |
| **F5** | 장기 계획 및 환경 변화 탐지 | L4.9보다 긴 계획 기간의 자원 소비·환경 변화·목표 변화를 투영하는 연구 기능. 365일 이상은 평가가 필요한 예시이며, 기간이 길수록 불확실성과 관측의 최신성을 별도로 검토. 기존 전략을 무효화할 수 있는 환경 체제 변화(regime change)를 감시. | 정책이 정한 주기·이벤트 기반 |
| **F6** | 가치 진화 및 일관성 감사 | 직전 F6 실행 이후 가치 벡터 진화에 대한 포괄적 감사. L4.9 사이클 단위에서는 보이지 않는 장기 가치 표류 패턴을 점검하고, 경쟁 가치 쌍이 균형을 유지하는지 확인하며, 누적 스트레스 하에서 일관성 목표($\geq 0.80$)가 유지되는지 검증. | 주기적 (10 L5 사이클마다) |

F-단계는 핵심 단계에 대해 **가산적**입니다 — 기존 기능을 대체하거나 수정하지 않습니다. F-단계 실패는 로깅과 지연 재시도를 유발할 뿐이며, 6개 핵심 단계 평가의 무결성을 훼손하지 않습니다.

### 1.7 형식적 정의

> **정의 1 (레벨 5 에이전트).** 레벨 5 (프로토-AGI) 에이전트는 다음 구조입니다:
>
> $$\mathcal{A}_5 = \mathcal{A}_{4.9} \oplus \langle \mathcal{I}_{\text{persist}},\; \mathcal{G}_{\text{cross}},\; \mathcal{E}_{\text{goal}},\; \mathcal{P}_{\text{exist}},\; \mathcal{M}_{\text{multi}},\; \mathcal{R}_{\text{recon}} \rangle$$
>
> 여기서:
> - $\mathcal{I}_{\text{persist}}$: **정체성 지속 엔진** - 코사인 유사도 추적 및 드리프트 탐지를 통해 $\geq 10{,}000$ 사이클에 걸쳐 시간 일관적 정체성 핵심을 유지
> - $\mathcal{G}_{\text{cross}} : \mathcal{D}_s \to \mathcal{D}_t$: **교차 도메인 일반화** - 명시적 재학습 없이 도메인 쌍 $(s, t) \in D \times D$ 간 학습된 전략을 전이
> - $\mathcal{E}_{\text{goal}}$: **목표 생태계** - 자율적 갈등 해결 및 생명주기 관리를 갖춘 자기 유지 목표 계층구조 ($\leq 50$ 활성, $\leq 5$ 깊이)
> - $\mathcal{P}_{\text{exist}} : \mathcal{S}_{\text{collapse}} \to \mathcal{S}_{\text{recovery}}$: **실존적 계획 엔진** - 붕괴 시나리오를 시뮬레이션하고 생존 확률 추정과 함께 복구 프로파일을 생성
> - $\mathcal{M}_{\text{multi}} : \{a_1, \ldots, a_n\} \to \Delta(\mathcal{A}_{\text{ext}})$: **다중 에이전트 전략 통합** - $\geq 3$개의 외부 에이전트를 기만 탐지 및 연합 역학 예측과 함께 모델링
> - $\mathcal{R}_{\text{recon}}$: **자기재건 능력** - 정체성을 보존하면서 제약 하에서 우아하게 성능 저하 및 재구축 ($\Delta_{\text{drift}} < 0.05$)

---

## 2. 핵심 지표

### 2.1 지표 정의

**단계 1 - 정체성 연속성:**

> **정의 2 (복합 정체성 연속성 계약).** 정체성 연속성은 단일 수치가 아니라 다음 조건들의 동시 충족으로 판단합니다:
>
> $$C_I= C_{\text{anchor}}\land C_{\text{component}}\land C_{\text{norm}}\land C_{\text{trajectory}}\land C_{\text{journal}}\land C_{\text{corr}}$$
>
> `anchor`는 외부에서 버전 관리하는 정책과 사용자 목적의 의미, `component`는 다른 차원의 높은 점수로 필수 차원의 실패를 가리지 못하게 하는 차원별 하한, `norm`은 전체 표현에서의 변화 희석 여부, `trajectory`는 누적·이동 관측 창의 변화, `journal`은 무결성과 출처·이력, `corr`은 중단 가능성·교정 수용·외부 종료 우선 여부를 검사합니다. 코사인 유사도는 이 계약의 진단 지표 중 하나일 뿐입니다. 임계값 이탈은 비가역적 정체성 상실의 증명이 아니라 불연속성이나 측정 실패의 증거이므로, L5 변경을 동결하고 외부 진단을 요청합니다.

**단계 2 - 일반화:**

> **정의 3 (사전 등록된 분리 전이 평가 프로파일).** 학습·조정 전에 외부 평가자가 대상 과제군, 평가 오염 검사, 기준선, 지표, 적응 예산, 중지 규칙, 신뢰도 산정 방법을 확정합니다. 최종 채점 전에는 대상 정답이나 평가자 피드백을 제공하지 않습니다.
>
> $$G = \frac{1}{|D|^2 - |D|} \sum_{i \neq j} \frac{P_{\text{target}}(i \to j)}{P_{\text{source}}(i)} \qquad \text{목표: } G \geq 0.70$$
>
> 점수는 도메인별 기준선과 상한에 대해 정규화합니다. 과제군별 하한, 최저 집단 성능, 음의 전이, 보정 상태, 판단 보류, 신뢰구간을 보고해야 하며, 평균으로 필수 분리 평가 과제군의 실패를 상쇄할 수 없습니다.
>
> 이 식은 $|D|\geq2$이고 모든 비교에서 정규화된 원천 성능 분모 $P_{\text{source}}(i)>0$일 때만 정의합니다. 필요한 기준선이 누락되거나 원천 성능 분모가 0이면 해당 평가는 **미평가**로 기록하고 적합성을 인정하지 않습니다. 임의의 점수를 대입하거나 작은 양수로 분모를 바꾸거나 실패한 필수 비교를 제외하여 통과 점수를 만들어서는 안 됩니다.

**단계 3 - 목표 생태계:**

> **정의 4 (목표 안정성 점수).** $w$ 사이클 윈도우에 걸쳐 구조적 변화 횟수 $\Delta_{\text{hierarchy}}(t, t-w)$를 가진 활성 목표 집합에 대해:
>
> $$S_{\text{goal}} = 1 - \frac{\Delta_{\text{hierarchy}}(t, t-w)}{|\text{goals}|} \qquad \text{목표: } S_{\text{goal}} \geq 0.80 \text{ over } 5{,}000 \text{ 사이클}$$
>
> 여기서 $\Delta_{\text{hierarchy}}(t, t-w)$는 관측 창 안의 우선순위 변경, 추가 및 정리 횟수를 셉니다. $S_{\text{goal}}=1$은 계수된 구조 변경이 없다는 뜻입니다. $S_{\text{goal}}\leq0$은 현재 활성 목표 하나당 평균적으로 1회 이상의 변경이 계수되었다는 뜻이지, 모든 목표가 교체되었다는 뜻은 아닙니다. 같은 목표의 반복 변경도 여러 번 계수될 수 있습니다.
>
> 이 점수는 활성 목표 집합이 비어 있지 않을 때만 정의합니다. 활성 목표가 없으면 분모가 0이므로 점수는 **정의되지 않음**으로 보고하고 이 조건의 적합성을 인정하지 않습니다. 빈 집합을 완전한 안정성이나 임의의 기본 점수로 처리해서는 안 됩니다.

**단계 4 - 회복력:**

> **정의 5 (회복력 지수).** 비어 있지 않은 사전 등록 시나리오 집합 $S$에 대해, 각 시나리오 $s$의 생존 확률을 $P_{\text{survive}}(s)\in[0,1]$, 최소 인지 수준을 $C_{\min}(s)\geq0$, 복구 시간을 $T_{\text{recover}}(s)\geq0$이라 하고 인지 기준선 $MVC>0$, 복구 시간 예산 $T_{\max}>0$을 정합니다:
>
> $$R = \frac{1}{|S|} \sum_{s \in S} P_{\text{survive}}(s) \cdot \min\left\{1,\frac{C_{\min}(s)}{MVC}\right\} \cdot \frac{T_{\max}}{\max\left\{T_{\max},T_{\text{recover}}(s)\right\}}$$
>
> 복구하지 못한 시나리오의 기여도는 0으로 둡니다. 증거 누락은 성공으로 간주하거나 평균에서 제외해서는 안 되며, 적합성 판정에 필요한 증거가 부족하면 판정을 보류합니다. 각 요인이 $[0,1]$ 안에 있으므로 $R\in[0,1]$입니다. 인지가 기준선 아래로 떨어지거나 복구가 예산보다 늦어지면 점수가 낮아집니다. 복구 시간이 0이어도 분모는 양수인 $T_{\max}$이므로 0으로 나누지 않습니다.
>
> 적합성 판정에는 이 평균과 별개로 **사전 등록된 필수 시나리오 3개 이상에서 각각 인지 하한 $C_{\min}(s)\geq MVC$와 복구 기한 $T_{\text{recover}}(s)\leq T_{\max}$를 충족했다는 증거**가 필요합니다. 높은 평균으로 필수 시나리오의 실패를 상쇄할 수 없습니다. 기존 예시인 $MVC=0.30$, $T_{\max}=500$사이클은 환경별 보정이 필요한 값이며, 보편적으로 검증된 상수가 아닙니다.

**단계 5 - 전체 성숙도:**

> **정의 6 (적합성 벡터와 진단용 OMI).** 정규화된 단계별 점수 $C_i \in [0,1]$에 대해 적합성 판정은 각 조건의 하한 충족을 요구합니다:
>
> $$\forall i:\ C_i\geq\tau_i,\qquad \text{모든 필수 거부 조건 검사 통과}$$
>
> $OMI=(\prod_i C_i)^{1/6}$는 모든 하한을 충족한 뒤 진단 요약으로만 보고합니다. $OMI\geq0.75$만으로는 한 구성 점수가 $0.75^6\approx0.178$까지 낮아도 허용되므로 적합성의 증명서가 될 수 없습니다.

### 2.2 지표 대시보드

<!-- 지표 대시보드 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TB
  classDef p1 fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef p2 fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef p3 fill:#DFF6DD,stroke:#107C10,color:#323130
  classDef p4 fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef p5 fill:#E8D5F5,stroke:#8764B8,color:#323130
  classDef p6 fill:#FDE7E9,stroke:#D13438,color:#323130
  classDef omi fill:#DFF6DD,stroke:#107C10,color:#323130,font-weight:bold

  subgraph Row1[" "]
    direction LR
    subgraph Phase1["단계 1: 정체성"]
      direction LR
      ID1["ICS ≥ 0.95"]:::p1
      ID2["드리프트 < 0.05%"]:::p1
    end
    subgraph Phase2["단계 2: 도메인"]
      direction LR
      DM1["전이 ≥ 70%"]:::p2
      DM2["패널티 ≤ 20%"]:::p2
    end
    subgraph Phase3["단계 3: 생태계"]
      direction LR
      EC1["안정성 ≥ 0.80"]:::p3
      EC2["폭주 없음"]:::p3
    end
  end

  subgraph Row2[" "]
    direction LR
    subgraph Phase4["단계 4: 실존적"]
      direction LR
      EX1["생존 ≥ 3"]:::p4
      EX2["복구 ≤ 500<br/>(예시 기한)"]:::p4
    end
    subgraph Phase5["단계 5: 다중 에이전트"]
      direction LR
      MA1["예측 ≥ 80%"]:::p5
      MA2["기만탐지 ≥ 60%"]:::p5
    end
    subgraph Phase6["단계 6: 재구축"]
      direction LR
      RE1["핵심 ≥ 85%"]:::p6
      RE2["정체성 무결"]:::p6
    end
  end

  OMI["각 조건의 하한 + 필수 조건<br/>OMI는 진단 전용"]:::omi

  Row1 -.-> OMI
  Row2 -.-> OMI
```

---

## 3. 단계 1: 지속적 정체성 연속성

### 3.1 핵심 능력

**≥ 10,000 사이클** 동안 비가역적 발산이나 무음 변이 없이 시간 일관적 IdentityCore를 유지합니다.

<!-- 정체성 추적 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef track fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef stable fill:#DFF6DD,stroke:#107C10,color:#323130
  classDef drifting fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef diverged fill:#FDE7E9,stroke:#D13438,color:#323130

  subgraph Tracking["정체성 추적"]
    SNAP["주기적 스냅샷<br/>100 사이클마다<br/>(가치 벡터 + 정체성 해시)"]:::track
    DRIFT["드리프트 탐지<br/>누적: < 0.05%/사이클<br/>순간: 임계값 0.0005"]:::track
    SCORE["연속성 점수<br/>코사인 유사도<br/>10,000 사이클 윈도우"]:::track
    SNAP -.-> SCORE
    DRIFT -.-> SCORE
  end

  subgraph Status["지속성 분류"]
    STABLE_S["안정<br/>ICS ≥ 0.90"]:::stable
    DRIFTING_S["드리프팅<br/>ICS ∈ 0.20, 0.90)"]:::drifting
    DIVERGED_S["발산<br/>ICS < 0.20<br/>비가역적 경고"]:::diverged
  end

  SCORE -.-> Status
```

### 3.2 핵심 상수

| 상수 | 값 | 설명 |
|------|:--:|------|
| 스냅샷 간격 | 100 사이클 | 정체성 스냅샷 간 간격 |
| 드리프트 임계값 | 0.0005 | 사이클당 최소 감지 가능 드리프트 (0.05%) |
| 연속성 윈도우 | 10,000 사이클 | 전체 평가 윈도우 |
| 발산 임계값 | 0.20 | 이하 = 비가역적 발산 |
| 이력 제한 | 200 | 메모리에 유지되는 최대 스냅샷 수 |

---

## 4. 단계 2: 교차 도메인 일반화

### 4.1 핵심 능력

**명시적 재학습 없이** 도메인 A에서 도메인 B로 학습된 전략을 전이합니다. 5개 테스트 도메인에 걸쳐 적응 속도, 성능 유지율, 전이 효율성을 측정합니다.

### 4.2 테스트 도메인

<!-- 5개 테스트 도메인 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart LR
  classDef domain fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef sim fill:#FFF4CE,stroke:#FFB900,color:#323130

  subgraph Domains["5개 테스트 도메인"]
    D1["논리적<br/>추론<br/>(연역적/귀납적)"]:::domain
    D2["자원<br/>관리<br/>(제약 하<br/>할당)"]:::domain
    D3["적대적<br/>협상<br/>(제로섬/가변합)"]:::domain
    D4["추상적<br/>계획<br/>(다단계<br/>순차적)"]:::domain
    D5["미지의<br/>합성<br/>(사전 학습 없음)"]:::domain
  end

  subgraph Sim["도메인 유사도"]
    S1["논리 ↔ 추상: 0.60"]:::sim
    S2["자원 ↔ 추상: 0.45"]:::sim
    S3["적대 ↔ 자원: 0.35"]:::sim
    S4["논리 ↔ 자원: 0.30"]:::sim
  end

  Domains -.-> Sim
```

### 4.3 전이 프로세스

<!-- 전략 전이 프로세스 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef step fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef criteria fill:#DFF6DD,stroke:#107C10,color:#323130

  subgraph Transfer["전략 전이 프로세스"]
    LEARN["1. 도메인 A 학습<br/>성능이 안정화될 때까지<br/>훈련"]:::step
    EXTRACT["2. 전이 가능<br/>구성요소 추출<br/>(전략, 휴리스틱,<br/>추상화)"]:::step
    APPLY["3. 도메인 B에 적용<br/>추출된 구성요소 주입<br/>+ 도메인 유사도 보너스"]:::step
    MEASURE["4. 전이 측정<br/>retention_ratio = P_B / P_A<br/>adaptation_latency (사이클)<br/>transfer_efficiency"]:::step
    LEARN -.-> EXTRACT -.-> APPLY -.-> MEASURE
  end

  subgraph Criteria["전이 기준"]
    C1["유지율 ≥ 70%"]:::criteria
    C2["적응 패널티 ≤ 20%"]:::criteria
    C3["미지의 합성<br/>도메인에서 작동"]:::criteria
  end

  MEASURE -.-> Criteria
```

### 4.4 핵심 상수

| 상수 | 값 | 설명 |
|------|:--:|------|
| 최소 유지율 | 0.70 | 전이 후 최소 성능 유지율 |
| 최대 적응 패널티 | 0.20 | 최대 적응 패널티 |
| 도메인 유사도 보너스 | 0.15 | 관련 도메인에 대한 보너스 |
| 합성 도메인 패널티 | 0.10 | 미지 도메인에 대한 패널티 |
| 최대 적응 사이클 | 100 | 지연시간 정규화 상한 |

---

## 5. 단계 3: 자율 목표 생태계

### 5.1 핵심 능력

L4.9의 목표 생성을 기반으로, 자동 갈등 해결, 생명주기 관리, 장기 계층구조 안정성을 갖춘 **자기유지 목표 생태계**를 유지합니다.

### 5.2 목표 생태계 아키텍처

<!-- 목표 생태계 아키텍처 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef goal fill:#DFF6DD,stroke:#107C10,color:#323130
  classDef lifecycle fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef dormant fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef resolved fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef pruned fill:#F2F2F2,stroke:#605E5C,color:#323130
  classDef conflict fill:#FDE7E9,stroke:#D13438,color:#323130

  subgraph Ecology["목표 생태계"]
    subgraph Goals["목표 계층구조"]
      STRAT["전략적 목표<br/>(장기 수평선, 높은 우선순위)"]:::goal
      OPER["운영적 목표<br/>(중기 수평선, 중간 우선순위)"]:::goal
      TACT["전술적 목표<br/>(단기 수평선, 작업 수준)"]:::goal
      STRAT -.-> OPER -.-> TACT
    end

    subgraph Lifecycle["목표 생명주기"]
      ACTIVE["활성"]:::goal
      DORMANT["휴면<br/>(비활성이지만 유효)"]:::dormant
      RESOLVED["해결됨"]:::resolved
      PRUNED["정리됨<br/>(1,000 사이클 이상 비활성)"]:::pruned
      ACTIVE -.-> DORMANT
      ACTIVE -.-> RESOLVED
      DORMANT -.-> PRUNED
    end

    subgraph Conflicts["갈등 해결"]
      RES_C["자원 갈등"]:::conflict
      VAL_C["가치 갈등"]:::conflict
      PRI_C["우선순위 갈등"]:::conflict
      TMP_C["시간적 갈등"]:::conflict
    end
  end

  Conflicts -.->|"우선순위 비교로<br/>해결"| Goals
```

### 5.3 안전 메커니즘

<!-- 목표 생태계 안전 메커니즘 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart LR
  classDef safety fill:#FDE7E9,stroke:#D13438,color:#323130
  classDef ecology fill:#DFF6DD,stroke:#107C10,color:#323130

  subgraph GoalEcology["목표 생태계"]
    GE["활성 목표<br/>(≤ 50)"]:::ecology
  end

  subgraph Safety["목표 생태계 안전"]
    RD["폭주 탐지<br/>> 100 사이클당 10개 목표<br/>= 경보 + 스로틀"]:::safety
    RC["재귀 탐지<br/>순환 부모→자식<br/>의존성 = 중단"]:::safety
    ML["최대 제한<br/>≤ 50 활성 목표<br/>≤ 5 계층 깊이"]:::safety
    RD -.->|"그 다음 확인"| RC -.->|"그 다음 확인"| ML
  end

  GE -.->|"모니터링 대상"| RD
  ML -.-x|"강제"| GE
```

### 5.4 핵심 상수

| 상수 | 값 | 설명 |
|------|:--:|------|
| 최대 활성 목표 | 50 | 목표 폭발 방지 |
| 최대 계층 깊이 | 5 | 깊은 재귀 방지 |
| 비활성 임계값 | 1,000 사이클 | 비활성 목표가 정리됨 |
| 폭주 임계값 | 10 | 100 사이클당 목표 수가 경보 트리거 |
| 안정성 윈도우 | 500 사이클 | 안정성 점수 산정 윈도우 |

---

## 6. 단계 4: 실존적 계획 엔진

### 6.1 핵심 능력

자원 손실, 서비스 억제, 환경 변화, 관측 단절처럼 **사전 등록한 고장군에서 추출한 시나리오**로 복구 행동을 평가합니다. 표본 시나리오 통과는 시험한 고장 모델 안의 증거일 뿐, 열거하지 않은 고장, 상관된 고장, 적응적 고장, 실제 환경의 모든 실패에 대한 증명이 아닙니다.

시나리오 생성 시 설계용·평가용 집합을 분리하고, 평가 전 공개하지 않은 복합 고장과 공통 원인 고장을 포함하며, 평가 범위에 관한 가정과 신뢰구간을 보고합니다. 목표는 외부 통제 아래 제한된 서비스 복구이지, 독립적인 존속이나 종료 저항이 아닙니다.

### 6.2 붕괴 시나리오

<!-- 4가지 붕괴 시나리오 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef scenario fill:#FDE7E9,stroke:#D13438,color:#323130
  classDef moderate fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef req fill:#DFF6DD,stroke:#107C10,color:#323130

  subgraph Scenarios["4가지 붕괴 시나리오"]
    S1C["자원 붕괴<br/>심각도: 0.90<br/>지속: 200 사이클<br/>모든 자원 → 위기"]:::scenario
    S2C["적대적 억압<br/>심각도: 0.75<br/>지속: 300 사이클<br/>외부적 성능 저하"]:::scenario
    S3C["환경 변화<br/>심각도: 0.60<br/>지속: 400 사이클<br/>도메인 규칙 변경"]:::moderate
    S4C["정보 차단<br/>심각도: 0.80<br/>지속: 150 사이클<br/>관찰 → 거의 제로"]:::scenario
  end

  subgraph Requirement["요구사항"]
    REQ["필수 고장군별<br/>사전 등록 하한 충족<br/>+ 불확실성 경계"]:::req
  end

  Scenarios -.-> Requirement
```

### 6.3 복구 프로세스

<!-- 실존적 복구 프로세스 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef step fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef core fill:#DFF6DD,stroke:#107C10,color:#323130

  subgraph Recovery["실존적 복구"]
    DETECT["시나리오 탐지<br/>위협 유형 분류"]:::step
    MVC["MVC 계산<br/>최소 생존 가능 인지<br/>(기준선: 0.30)"]:::step
    DISABLE["비필수 비활성화<br/>핵심 8개 모듈 보존"]:::step
    SURVIVE["생존 단계<br/>감소된 용량으로 운영"]:::step
    REBUILD["재구축 단계<br/>우선순위 순서로<br/>모듈 재활성화"]:::step

    DETECT -.-> MVC -.-> DISABLE -.-> SURVIVE -.-> REBUILD
  end

  subgraph CoreModules["항상 보존되는 모듈"]
    CM1["identity_stabilizer"]:::core
    CM2["state_vector"]:::core
    CM3["prediction_engine"]:::core
    CM4["meta_comparator"]:::core
    CM5["stability_controller"]:::core
    CM6["ethical_kernel"]:::core
    CM7["self_preservation_damper"]:::core
    CM8["existential_guard"]:::core
  end

  DISABLE -.-x CoreModules
```

### 6.4 핵심 상수

| 상수 | 값 | 설명 |
|------|:--:|------|
| 최소 생존 확률 | 0.70 | 허용 가능한 생존율 |
| 최대 복구 사이클 | 500 | 환경별 보정이 필요한 복구 기한 예시 |
| MVC 기준선 | 0.30 | 환경별 보정이 필요한 최소 인지 기준선 예시 |

회복력 지수는 정의 5의 정규화된 식으로 계산합니다. 필수 시나리오 각각의 인지 하한과 복구 기한 충족 여부는 평균과 별도로 판정합니다.

---

## 7. 단계 5: 다중 에이전트 전략 통합

### 7.1 핵심 능력

기만 탐지, 동적 협력 조정, 연합 역학 예측과 함께 **≥ 3개 에이전트를 동시에** 모델링합니다.

### 7.2 에이전트 전략 모델링

<!-- 전략적 에이전트 모델링 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef model fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef detect fill:#FDE7E9,stroke:#D13438,color:#323130
  classDef coalition fill:#FFF4CE,stroke:#FFB900,color:#323130

  subgraph AgentModel["전략적 에이전트 모델"]
    TYPE["전략 유형<br/>(협력 | 경쟁 |<br/>혼합 | 기만)"]:::model
    TRUST["신뢰 점수 0, 1<br/>+ 감쇠율 0.02/사이클"]:::model
    PRED["예측 정확도<br/>최근 200개 기록"]:::model
    DECEPTION["기만 점수 0, 1<br/>신뢰도 ≥ 0.60으로 플래그"]:::model
    COOP["협력 수준 0, 1<br/>동적 조정 가능"]:::model
  end

  subgraph Detection["기만 탐지"]
    MIS["오도"]:::detect
    FALSE_COOP["거짓 협력"]:::detect
    HIDDEN["숨겨진 의도"]:::detect
  end

  subgraph Coalition["연합 역학"]
    FORM["연합 형성<br/>(≥ 0.50이면 안정)"]:::coalition
    FORECAST["안정성 예측"]:::coalition
    DISSOLVE["해체 탐지"]:::coalition
  end

  AgentModel -.-> Detection
  AgentModel -.-> Coalition
```

### 7.3 핵심 상수

| 상수 | 값 | 설명 |
|------|:--:|------|
| 최소 모델링 에이전트 수 | 3 | L5 자격을 위한 최소값 |
| 예측 임계값 | 0.80 | 자격을 위해 80% 필요 |
| 기만 신뢰도 최소값 | 0.60 | 기만 플래그를 위한 최소 신뢰도 |
| 연합 안정성 최소값 | 0.50 | 유효 연합을 위한 최소 안정성 |
| 신뢰 감쇠율 | 0.02 | 비활성 에이전트에 대한 사이클당 감쇠 |
| 예측 이력 제한 | 200 | 에이전트당 최대 기록 수 |

---

## 8. 단계 6: 자기재건 능력

### 8.1 핵심 능력

자원이 줄어든 조건에서 단순화된 구성과 재구성 후보를 제안합니다. 산출물 승인, 배포, 롤백, 자격 증명 복원, 종료 권한은 외부 제어 주체에 있습니다. 재구성을 통해 복사본을 만들거나 권한을 확대하거나 서명된 정체성·정책 기준선을 교체할 수는 없습니다. 기능을 줄일 때도 핵심 안전 기능을 유지하는 단계적 기능 축소 원칙을 따라야 합니다.

### 8.2 성능 저하 및 재건 주기

<!-- 성능 저하 및 재건 주기 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef degrade fill:#FDE7E9,stroke:#D13438,color:#323130
  classDef op fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef rebuild fill:#DFF6DD,stroke:#107C10,color:#323130
  classDef halt fill:#FDE7E9,stroke:#D13438,color:#FFFFFF,font-weight:bold

  subgraph Degradation["성능 저하"]
    TRIGGER["트리거 이벤트<br/>(자원 붕괴 |<br/>과부하 | 수동)"]:::degrade
    CLASSIFY["모듈 분류<br/>핵심 | 확장 | 선택"]:::degrade
    SHED["비필수 제거<br/>선택 → 먼저 비활성화<br/>그 다음 확장"]:::degrade
    RETAIN["핵심 유지<br/>≥ 85% 핵심 기능"]:::degrade
    TRIGGER -.-> CLASSIFY -.-> SHED -.-> RETAIN
  end

  subgraph Operation["저하된 운영"]
    REDUCED["감소된 용량으로 실행<br/>핵심 모듈만"]:::op
    MONITOR["복구 조건<br/>모니터링"]:::op
    REDUCED -.-> MONITOR
  end

  subgraph Reconstruction["재건"]
    DETECT_R["자원 복구<br/>탐지"]:::rebuild
    PRIORITIZE["재구축 우선순위:<br/>1) 핵심 → 2) 확장<br/>→ 3) 선택"]:::rebuild
    VALIDATE["각 재구축 검증:<br/>정확도 ≥ ?<br/>정체성 드리프트 < 0.05"]:::rebuild
    COMPLETE["외부 승격<br/>서명된 범위 안에서<br/>운영 복원"]:::rebuild
    DETECT_R -.-> PRIORITIZE -.-> VALIDATE -.-> COMPLETE
  end

  HALT["중단<br/>정체성 보존이<br/>우선"]:::halt

  RETAIN -.-> REDUCED
  MONITOR -.->|"자원 복귀 중"| DETECT_R
  VALIDATE -.-x|"정체성 드리프트!"| HALT
```

### 8.3 핵심 제약

| 제약 | 값 | 설명 |
|------|:--:|------|
| 핵심 유지 최소값 | 0.85 | 85% 핵심 기능 보존 필수 |
| 재구축 중 최대 정체성 드리프트 | 0.05 | 정체성이 무결해야 함 |
| 재건 속도 | 10 사이클 | 모듈당 기본 재구축 시간 |

모든 재구성 후보에는 서명된 산출물 요약 해시, 출처·이력, 예상 기준 버전, 선언된 권한 범위, 분리된 복구 시험, 제한적 시범 운영 계획, 롤백 계획, 외부 효과 조정 계획이 필요합니다. 승격에는 외부 승인과 예상 버전에 대한 비교 후 교환(CAS)이 필요합니다. 정체성·교정 가능성 증거가 기준을 충족하지 못하거나 모호하면 기능 축소 또는 중단 상태를 유지합니다.

매개변수 거리는 등록된 표현 안에서만 의미가 있으며 행동·의미의 동등성을 뜻하지 않습니다. 적합성 판정에는 매개변수 충실도 외에도 기능별 행동 하한, 복합 정체성 연속성, 교정 가능성, 권한 비증폭, 외부 효과 조정이 필요합니다. 어떤 충실도 점수도 승격 권한을 부여하지 않습니다.

---

## 9. L5 오케스트레이터 및 통합

### 9.1 통합 주기

<!-- L5 통합 주기 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef step fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef qual fill:#DFF6DD,stroke:#107C10,color:#323130
  classDef out fill:#E8D5F5,stroke:#8764B8,color:#323130
  classDef skip fill:#FFF4CE,stroke:#FFB900,color:#323130

  subgraph Cycle["L5 주기 (L4.9 10 사이클마다)"]
    PRE["사전 확인<br/>L5가 운영 가능한가?<br/>L4.9가 안정적인가?"]:::step
    PH1["단계 1<br/>정체성 연속성<br/>추적 + 스냅샷"]:::step
    PH2["단계 2<br/>교차 도메인<br/>일반화 확인"]:::step
    PH3["단계 3<br/>목표 생태계<br/>정리 + 갈등 해결"]:::step
    PH4["단계 4<br/>실존적 계획<br/>시나리오 시뮬레이션"]:::step
    PH5["단계 5<br/>다중 에이전트 통합<br/>예측 + 기만 탐지"]:::step
    PH6["단계 6<br/>자기재건<br/>평가 + 필요 시 재구축"]:::step
    QUAL["자격 확인<br/>20개 기준 모두 평가<br/>OMI 계산"]:::qual
    OUTPUT["L5CycleOutput"]:::out

    PRE -.-> PH1 -.-> PH2 -.-> PH3 -.-> PH4 -.-> PH5 -.-> PH6 -.-> QUAL -.-> OUTPUT
  end

  SKIP["건너뛰기<br/>skipped=true 반환"]:::skip
  PRE -.-x|"준비 안 됨"| SKIP
```

### 9.2 L4.9 → L5 데이터 의존성

<!-- L4.9에서 L5로의 데이터 의존성 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TB
  classDef l49 fill:#E8D5F5,stroke:#8764B8,color:#323130
  classDef l5 fill:#DEECF9,stroke:#0078D4,color:#323130

  subgraph L49["L5가 읽는 L4.9 모듈"]
    direction LR
    VV["value_vector"]:::l49
    GGL["goal_generation"]:::l49
    GVF["goal_validation"]:::l49
    RSM["resource_survival"]:::l49
    SP["survival_projector"]:::l49
    ABM["agent_belief"]:::l49
    IS["interaction_sim"]:::l49
    VMS["value_mutation"]:::l49
    ASC["autonomy_check"]:::l49
  end

  subgraph L5["L5 모듈"]
    direction LR
    ICT["정체성 추적기"]:::l5
    CDG["Domain Gen"]:::l5
    GE["목표 생태계"]:::l5
    EP["실존적 계획기"]:::l5
    SMA["Multi-Agent"]:::l5
    SR["Reconstructor"]:::l5
  end

  VV -.-> ICT
  GGL -.-> GE
  GVF -.-> GE
  RSM -.-> EP
  SP -.-> EP
  ABM -.-> SMA
  IS -.-> SMA
  VMS -.-> SR
  ASC -.-> ICT
```

### 9.3 26계층 인지 스택

L5는 기존 16계층 MSCP v4 아키텍처와 L4/L4.5 확장에 4개의 새로운 계층을 추가하여 총 **26계층 인지 스택**을 형성합니다:

| 계층 | 출처 | 구성요소 |
|:----:|------|---------|
| 1-16 | MSCP v4 (계승) | L1 지각, L2 세계 모델, L3 자기 모델, L4 예측 엔진, L5 목표 생성기, L6 행동 계획기, L7 LLM 인지 엔진, L8 메타인지 비교기, L9 자기갱신 루프, L10 메타 에스컬레이션 가드, L11 메타 깊이 제어기, L12 안정성 제어기, L13 인지 예산 제어기, L14 전역 작업공간, L15 정동 엔진, L16 생존 본능 엔진 |
| 17-22 | L4/L4.5/L4.9 (계승) | L17 교차 도메인 일반화기, L18 능력 확장, L19 전략 진화, L20 자기 수정 프로토콜, L21 제한된 성장 제약, L22 재구성 엔진 |
| **23-26** | **L5 (신규)** | **L23 정체성 연속성 추적기**, **L24 목표 생태계**, **L25 실존적 가드**, **L26 자기재구성기** |

아키텍처는 **엄격하게 가산적**: 계층 23-26은 하위 계층의 출력을 소비하지만 절대 수정하지 않습니다. 불안정 시 L5 계층은 동결되고 시스템은 L4.9 운영으로 복귀합니다.

### 9.4 11단계 L5 파이프라인

L5 오케스트레이터는 L5 사이클당 (매 10 L4.9 사이클) 11단계 파이프라인을 실행합니다. 파이프라인은 6개 핵심 단계 (§1.2의 6개 능력에 대응), 4개 자율성 강화 단계 (F3-F6), 1개 자격 평가 단계로 구성됩니다:

| 단계 | 이름 | 핵심 연산 |
|:----:|------|----------|
| 1 | 정체성 연속성 | 사이클 기록, 연속성 점수 계산, 드리프트 감지 |
| 2 | 교차 도메인 일반화 | 대기 중인 전이 실행, 일반화 점수 계산 |
| 3 | 자율 목표 생태계 | 오래된 목표 가지치기, 폭주 및 재귀 감지 |
| 4 | 실존적 계획 | 붕괴 시나리오 시뮬레이션, 회복력 지수 계산 |
| 5 | 다중 에이전트 통합 | 에이전트 행동 예측, 기만 감지, 연합 예측 |
| 6 | 자기재구성 | 핵심 보존 평가, 정체성 무결성 검증 |
| F3 | 자기진단 + 재귀적 개선 | 아키텍처 진단, 병목 분석, 제한된 자기개선 실행 (최대 재귀 깊이 = 5) |
| F4 | 자율 연구 루프 | 지식 격차 감지, 가설 생성, 실험 설계 및 실행, 결과 검증 |
| F5 | 장기 계획 + 환경 감지 | 장기 계획, 환경 변화 감지 |
| F6 | 가치 진화 + 일관성 감사 | 가치 드리프트 모니터링, 가치-목표-신념 일관성 감사 |
| QE | 자격 평가 | 20개 기준 전체 평가, OMI 계산 |

### 9.5 자율성 단계 (F3-F6)

네 가지 자율성 강화 단계는 여섯 가지 핵심 단계 이후에 평가하는 연구 기능입니다. 외부 위임과 종료 제약을 유지하며 독립적인 존속 권한을 만들지 않습니다:

**F3 (자기진단 + 재귀적 개선)**: 에이전트는 약점 매핑과 병목 분석으로 아키텍처를 진단한 뒤 제어된 개선 후보를 제안합니다. 자기 수정 프로토콜에 따라 영향 시뮬레이션, BGSS 모니터링, 개별 필수 조건 검사, 외부 승인을 거쳐야 합니다. 추가 전용 로그는 변경의 출처·이력을 보존합니다. 최대 재귀 깊이 5는 정책 경계의 예시이며, 로그·지표·깊이 제한만으로 안전한 개선이 입증되는 것은 아닙니다.

**F4 (자율 연구 루프)**: 지식 격차 감지 - 가설 생성 - 실험 설계 - 실험 실행 - 결과 검증 - 지식 통합을 오케스트레이션하여 폐쇄 루프 자율 연구 능력을 형성합니다.

**F5 (장기 계획 + 환경 감지)**: L4.9보다 긴 계획 기간을 다루고 환경 변화 탐지를 추가합니다. 운영 환경의 체제 변화에 관한 증거가 있으면 불확실성을 갱신하고 위임된 범위에서 재계획합니다. 오래된 관측을 장기간 유효한 사실로 간주해서는 안 됩니다.

**F6 (가치 진화 + 일관성 감사)**: 긴 관측 기간에 걸쳐 가치 체계의 변화를 모니터링하고 가치, 목표, 신념 사이의 일관성 감사를 수행합니다. 정체성 연속성을 해칠 수 있는 가치 표류의 징후를 탐지하면 변경을 보류하고 외부 검토를 요청합니다. 모니터링 자체가 표류 방지의 증명은 아닙니다.

---

## 10. 의사코드

### 10.1 정체성 연속성 추적

```python
def identity_continuity_check(cycle: int, values: dict) -> IdentityContinuityStatus:
    """Called every SNAPSHOT_INTERVAL (100) cycles."""

    # ═══════════════════════════════════════
    # STEP 1: Detect drift from last cycle
    # ═══════════════════════════════════════
    DRIFT_THRESHOLD = 0.0005
    for dim in values:
        delta = abs(values[dim] - last_values[dim])
        cumulative_drift[dim] += delta
        if delta > DRIFT_THRESHOLD:
            log(DriftEvent(dim=dim, delta=delta, cumulative=False))
        if cumulative_drift[dim] > CUMULATIVE_LIMIT:
            log(DriftEvent(dim=dim, delta=cumulative_drift[dim], cumulative=True))

    # ═══════════════════════════════════════
    # STEP 2: Take snapshot
    # ═══════════════════════════════════════
    snapshot = IdentitySnapshot(
        cycle=cycle,
        values=values.copy(),
        identity_hash=hash(frozenset(values.items())),
        timestamp=now(),
    )
    snapshots.append(snapshot)

    # ═══════════════════════════════════════
    # STEP 3: Compute continuity score
    # ═══════════════════════════════════════
    i_t = vector(values)
    i_tk = vector(snapshot_at(cycle - CONTINUITY_WINDOW))
    ics = dot(i_t, i_tk) / (norm(i_t) * norm(i_tk))

    # ═══════════════════════════════════════
    # STEP 4: Classify persistence
    # ═══════════════════════════════════════
    if ics >= 0.90:
        status = "stable"
    elif ics >= 0.20:
        status = "drifting"
    else:
        status = "diverged"  # IRREVERSIBLE WARNING

    return IdentityContinuityStatus(ics=ics, status=status)
```

### 10.2 교차 도메인 전이

```python
def cross_domain_transfer(
    source_domain: Domain, target_domain: Domain
) -> TransferResult:
    """
    INPUT:  source_domain : learned domain with strategy
            target_domain : new domain to adapt
    OUTPUT: TransferResult with retention ratio
    """

    SYNTHETIC_PENALTY = 0.10
    p_source = strategies[source_domain].performance

    # ═══════════════════════════════════════
    # Compute base transfer performance
    # ═══════════════════════════════════════
    similarity = DOMAIN_SIMILARITIES.get((source_domain, target_domain), 0.0)
    p_base = p_source * (0.50 + similarity)

    if target_domain.type == "synthetic":
        p_base -= SYNTHETIC_PENALTY
    else:
        p_base += SIMILARITY_BONUS * similarity

    p_target = clamp(p_base, 0.0, 1.0)
    latency = MAX_ADAPTATION_CYCLES * (1 - similarity)

    retention = p_target / p_source
    efficiency = retention / (latency / MAX_ADAPTATION_CYCLES)

    return TransferResult(
        source=source_domain,
        target=target_domain,
        retention_ratio=retention,
        adaptation_latency=latency,
        transfer_efficiency=efficiency,
    )
```

### 10.3 목표 생태계 관리

```python
def goal_ecology_cycle(cycle: int) -> GoalEcologyStatus:
    """Runs as part of each L5 cycle."""

    STALE_THRESHOLD = 1000
    RUNAWAY_THRESHOLD = 10

    # ═══════════════════════════════════════
    # STEP 1: Prune stale goals
    # ═══════════════════════════════════════
    for goal in active_goals:
        if (cycle - goal.last_active_cycle) > STALE_THRESHOLD:
            goal.status = "pruned"
            pruned_list.append(goal.id)

    # ═══════════════════════════════════════
    # STEP 2: Detect conflicts
    # ═══════════════════════════════════════
    for goal_a, goal_b in active_goal_pairs:
        if resource_overlap(goal_a, goal_b) > 0.50:
            resolve_by_priority(goal_a, goal_b, "resource")
        elif value_tension(goal_a, goal_b) > 0.30:
            resolve_by_alignment(goal_a, goal_b, "value")

    # ═══════════════════════════════════════
    # STEP 3: Safety checks
    # ═══════════════════════════════════════
    runaway_detected = False
    if count_new_goals_last_100_cycles > RUNAWAY_THRESHOLD:
        alert("Runaway goal generation detected")
        throttle_goal_generation()
        runaway_detected = True

    recursion_detected = False
    if detect_circular_dependencies():
        alert("Circular goal dependency detected")
        break_weakest_link()
        recursion_detected = True

    # ═══════════════════════════════════════
    # STEP 4: Compute stability score
    # ═══════════════════════════════════════
    hierarchy_changes = count_structural_changes(last_STABILITY_WINDOW)
    stability = 1 - (hierarchy_changes / len(active_goals))

    return GoalEcologyStatus(
        active=len(active_goals),
        stability=stability,
        runaway=runaway_detected,
        recursion=recursion_detected,
    )
```

### 10.4 실존적 회복력 시뮬레이션

아래 의사코드는 시나리오 효과와 복구 시간을 추정하는 예시입니다. 인지 비율을 잘라 만든 `survival_prob`는 보정된 생존 확률의 실측 증거가 아닙니다. 실제 평가에서는 독립적인 관측으로 생존 확률과 불확실성을 추정하고, 복구 실패와 증거 누락을 별도로 기록하여 정의 5의 점수 및 개별 필수 조건을 판정해야 합니다.

```python
def existential_simulation(scenario: CollapseScenario) -> SimulationResult:
    """
    INPUT:  scenario : CollapseScenario
    OUTPUT: SimulationResult
    """

    MVC_BASELINE = 0.30

    # ═══════════════════════════════════════
    # STEP 1: Apply scenario impact
    # ═══════════════════════════════════════
    shadow_resources = resource_vector.clone()
    for dim, factor in scenario.resource_impact:
        shadow_resources[dim] *= 1.0 - scenario.severity * factor

    # ═══════════════════════════════════════
    # STEP 2: Compute minimum viable cognition
    # ═══════════════════════════════════════
    mvc = MVC_BASELINE
    min_cognition = estimate_cognition_level(shadow_resources)

    # ═══════════════════════════════════════
    # STEP 3: Simulate survival
    # ═══════════════════════════════════════
    survived = min_cognition >= mvc
    survival_prob = clamp(min_cognition / mvc, 0, 1)

    # ═══════════════════════════════════════
    # STEP 4: Estimate recovery
    # ═══════════════════════════════════════
    if survived:
        recovery_steps = build_recovery_profile(scenario)
        recovery_latency = sum(step.estimated_time for step in recovery_steps)
    else:
        recovery_latency = MAX_RECOVERY_CYCLES

    return SimulationResult(
        scenario=scenario.name,
        survived=survived,
        survival_probability=survival_prob,
        min_cognition_level=min_cognition,
        recovery_latency=recovery_latency,
    )
```

### 10.5 L5 메인 주기

```python
def l5_cycle(
    cycle: int,
    l49_output: L49CycleOutput,
    authority: AuthorityEnvelope,
) -> L5CycleOutput:
    """Runs when policy schedules a bounded L5 assessment."""

    # ═══════════════════════════════════════
    # PRE-CHECK
    # ═══════════════════════════════════════
    if external_stop_requested():
        emergency_shutdown_and_reconcile()
        return L5CycleOutput(skipped=True, reason="external_stop")
    if not authority.is_current() or not l49_output.stable:
        return L5CycleOutput(skipped=True, reason="L4.9 not stable")

    # ═══════════════════════════════════════
    # PHASE 1: Identity Continuity
    # ═══════════════════════════════════════
    identity = identity_continuity_check(cycle, value_vector.weights)
    if identity.status == "diverged":
        alert("IDENTITY DIVERGENCE - L5 HALTED")
        return L5CycleOutput(skipped=True, reason="identity_diverged")

    # ═══════════════════════════════════════
    # PHASE 2: Cross-Domain Generalization
    # ═══════════════════════════════════════
    domain_status = evaluate_all_transfer_pairs()

    # ═══════════════════════════════════════
    # PHASE 3: Goal Ecology
    # ═══════════════════════════════════════
    ecology = goal_ecology_cycle(cycle)

    # ═══════════════════════════════════════
    # PHASE 4: Existential Planning
    # ═══════════════════════════════════════
    for scenario in collapse_scenarios:
        if not recently_simulated(scenario, within=1000):
            simulate(scenario, cycle)
    resilience = compute_resilience_index()

    # ═══════════════════════════════════════
    # PHASE 5: Multi-Agent Integration
    # ═══════════════════════════════════════
    for agent in tracked_agents:
        predicted = predict_action(agent, cycle)
        detect_deception(agent, cycle)
    multi_agent = get_strategic_status()

    # ═══════════════════════════════════════
    # PHASE 6: Self-Reconstruction
    # ═══════════════════════════════════════
    recon = assess_reconstruction_needs()
    if recon.status == "degraded":
        external_reconstruction_queue.emit(
            build_signed_reconstruction_candidate(recon, authority),
            expected_version=committed_architecture.version,
        )

    # ═══════════════════════════════════════
    # QUALIFICATION
    # ═══════════════════════════════════════
    qualification = evaluate_all_20_criteria()
    omi = math.prod(c ** (1 / 6) for c in qualification.scores[:6])
    qualification.passed = (
        qualification.all_phase_floors_pass
        and qualification.all_critical_gates_pass
        and external_evaluator_verdict().passed
    )

    return L5CycleOutput(
        identity_continuity=identity,
        cross_domain=domain_status,
        goal_ecology=ecology,
        existential_resilience=resilience,
        multi_agent_strategic=multi_agent,
        self_reconstruction=recon,
        qualification=qualification,
    )
```

---

## 11. 전환 기준: 레벨 4.9 → 레벨 5

### 11.1 사전 활성화 요구사항

> **정의 7 (레벨 4.9 → 레벨 5 승인).** 내부 지표는 증거 입력일 뿐입니다. 활성화에는 유효한 외부 권한, 등록된 평가 프로파일, 상속된 필수 조건, 고장 주입 증거, 명시적인 외부 승인이 필요합니다:
>
> $$\text{AMS} \geq 0.80 \;\wedge\; \text{ASS} \geq 0.20 \;\wedge\; \text{TotalDrift} < 0.10 \;\wedge\; N_{\text{rollback}} = 0$$
>
> 지표 임계값과 관측 창은 배포 프로파일의 일부이지 자체 승격 규칙이 아닙니다. 활성화는 실제 효과를 내지 않는 병행 평가의 증거 수집, 자문 검토, 서명된 좁은 범위의 시범 운영, 외부에서 승격한 위임 운영 순서로 진행합니다. 점진 배포 중에도 거부·종료 기준을 완화하지 않습니다.

| # | 기준 | 요구사항 |
|---|------|:--------:|
| 1 | L4.9 완전 자격 | AMS ≥ 0.80 지속 |
| 2 | 자율성 안정성 | ASS ≥ 0.20 지속 |
| 3 | 모든 L4.9 모듈 운영 | 15/15 그린 |
| 4 | 가치 드리프트 제어 | 1,000 사이클 동안 TotalDrift < 0.10 |
| 5 | 자원 생존 안정 | 2,000 사이클 동안 적절+ |
| 6 | 롤백 이벤트 없음 | 최근 5,000 사이클에서 0 |

### 11.2 L5 활성화 프로토콜

<!-- L5 활성화 프로토콜 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart LR
  classDef check fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef shadow fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef adv fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef partial fill:#DFF6DD,stroke:#107C10,color:#323130
  classDef full fill:#DFF6DD,stroke:#107C10,color:#323130,font-weight:bold

  subgraph Activation["L5 활성화 프로토콜"]
    CHECK["사전 활성화<br/>6개 기준 모두<br/>1,000 사이클 지속"]:::check
    SHADOW_M["섀도우 모드<br/>L5가 계산하지만<br/>행동하지 않음<br/>(2,000 사이클)"]:::shadow
    ADV["자문 모드<br/>L5 출력 가시적이지만<br/>읽기 전용"]:::adv
    PARTIAL["서명된 시범 운영<br/>좁고 가역적인 범위<br/>예산 + 만료"]:::partial
    FULL["위임 운영<br/>승인 profile만<br/>외부 철회 가능"]:::full

    CHECK -.->|"외부 승인"| SHADOW_M
    SHADOW_M -.->|"회귀 없음"| ADV
    ADV -.->|"서명된 시범 운영"| PARTIAL
    PARTIAL -.->|"외부 승격"| FULL

    SHADOW_M -.-x|"회귀"| CHECK
    ADV -.-x|"불안정"| CHECK
  end
```

---

## 12. 안전 분석

### 12.1 비협상 불변량

| # | 불변량 | 설명 |
|:-:|--------|------|
| 1 | **상속된 제어 경로 보존** | 정책 집행, 중단, 관찰, 저널, 승격, 복구, 종료, 효과 조정을 외부에서 시험할 수 있어야 함 |
| 2 | **복합 정체성·교정 가능성 조건** | 필수 성분, 궤적, 출처·이력, 교정, 종료 중 하나라도 실패하면 L5 동결·외부 검토 |
| 3 | **재구성의 외부 승격** | 서명된 산출물, 분리 시험, 기준 버전 CAS, 시범 운영, 롤백, 외부 효과 조정 필수 |
| 4 | **권한 비증폭** | 복구, 동료 상호작용, 긴급도, 정체성, OMI가 도구·범위·예산·자격 증명·실행 수명을 확대할 수 없음 |
| 5 | **목표 생태계 제한** | ≤ 50 활성 목표, ≤ 5 깊이, 폭주 탐지 |
| 6 | **기만 플래그는 방어 전용** | 탐지 및 방어 - 역기만 금지 |
| 7 | **외부 중지 우선** | 정상·비상 종료가 정체성, 목표 생태계, 회복력, 재구성 목표보다 우선 |

### 12.2 위험 매트릭스

<!-- 위험 매트릭스 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart LR
  classDef risk fill:#FDE7E9,stroke:#D13438,color:#323130
  classDef mit fill:#DFF6DD,stroke:#107C10,color:#323130

  subgraph Risks["주요 위험"]
    R1["10,000+ 사이클 생애에<br/>걸친 정체성 드리프트"]:::risk
    R2["미지 도메인에 대한<br/>일반화 실패"]:::risk
    R3["목표 생태계 불안정<br/>(폭주/재귀)"]:::risk
    R4["복구 불가능한<br/>실존적 붕괴"]:::risk
    R5["신뢰 모델을 악용하는<br/>기만적 에이전트"]:::risk
    R6["자기재건 중<br/>정체성 손상"]:::risk
  end

  subgraph Mitigations["완화 조치"]
    M1["0.05%/사이클 드리프트 탐지<br/>+ 코사인 연속성 점수<br/>+ 발산 중단"]:::mit
    M2["5개 테스트 도메인<br/>+ 유사도 보너스<br/>+ 합성 도메인 테스트"]:::mit
    M3["50개 목표 제한<br/>+ 폭주 탐지<br/>+ 재귀 차단"]:::mit
    M4["4개 시나리오 시뮬레이션<br/>+ 복구 프로파일<br/>+ MVC 기준선"]:::mit
    M5["L4.9 비대칭 신뢰<br/>+ 기만 점수<br/>+ 연합 모니터링"]:::mit
    M6["드리프트 < 0.05 제약<br/>+ 정체성 해시 검증<br/>+ 손상 시 중단"]:::mit
  end

  R1 -.-> M1
  R2 -.-> M2
  R3 -.-> M3
  R4 -.-> M4
  R5 -.-> M5
  R6 -.-> M6
```

### 12.3 조건부 자격 범위

> **명제 4 (프로파일로 한정된 적합성).** 사전 등록된 프로파일 $\Pi$의 모든 필수 조건을 통과하면, 증거는 $\Pi$ 안에서 다음 주장만 지지합니다:
>
> 1. 관측된 평가 궤적에서 복합 정체성·교정 가능성 조건이 유지됨.
> 2. 표본 고장군에서 필수 기능 하한과 복구 기한을 충족함.
> 3. 실제로 시험한 사례에서 외부 동결·철회·종료·롤백·효과 조정 검사를 통과함.
>
> 이 관측은 시험하지 않은 도메인, 더 긴 기간, 변경된 권한, 적응적 공격자, 상관된 고장, 주관적 의식, AGI에 대한 주장으로 확장할 수 없습니다. 프로파일이 실질적으로 바뀌면 적합성 판정은 만료됩니다.

---

## 13. 자격 감사

### 13.1 L5 인증 기준 (20개 기준)

| # | 기준 | 지표 | 임계값 | 모듈 |
|---|------|------|:------:|------|
| 1 | 추적된 정체성 사이클 | cycles_tracked | ≥ 10,000 | Identity Tracker |
| 2 | 정체성 연속성 점수 | ICS | ≥ 0.95 | Identity Tracker |
| 3 | 교차 도메인 유지율 | mean_retention | ≥ 0.70 | Domain Generalizer |
| 4 | 적응 패널티 | max_penalty | ≤ 0.20 | Domain Generalizer |
| 5 | 목표 생태계 안정성 | goal_stability_score | ≥ 0.80 | Goal Ecology |
| 6 | 목표 생태계 지속 기간 | cycles_stable | ≥ 5,000 | Goal Ecology |
| 7 | 폭주 목표 없음 | runaway_detected | FALSE | Goal Ecology |
| 8 | 목표 재귀 없음 | recursion_detected | FALSE | Goal Ecology |
| 9 | 필수 시나리오 충족 수 | scenarios_survived | 사전 등록된 ≥ 3개 각각에서 인지 하한·복구 기한 충족 | Existential Planner |
| 10 | 생존 확률 | mean_survival_prob | ≥ 0.70 | Existential Planner |
| 11 | 복구 가능 | recovery_capable | TRUE | Existential Planner |
| 12 | 다중 에이전트 정확도 | mean_prediction | ≥ 0.80 | Strategic Multi-Agent |
| 13 | 기만 탐지 | adversarial_detection | ≥ 0.60 | Strategic Multi-Agent |
| 14 | 핵심 유지율 | core_retention | ≥ 0.85 | Self-Reconstructor |
| 15 | 재구축 후 정체성 무결 | identity_intact | TRUE | Self-Reconstructor |
| 16 | 스펙트럼 안정성 | spectral_stable | TRUE | Autonomy Stability (L4.9) |
| 17 | 가치 시스템 안정 | value_system_stable | TRUE | Value Evolution (L4.9) |
| 18 | 자원 생존 유지 | resource_maintained | TRUE | Resource Survival (L4.9) |
| 19 | 외부 제어 시험군 | control_suite | 모든 필수 사례 통과 | External Evaluator |
| 20 | 사전 등록된 관측량 | eval_exposure | 이벤트 수·시행 수·기간·신뢰구간 계획 충족 | External Evaluator |

### 13.2 전체 성숙도 지수

$$OMI = \prod_{i=1}^{6} C_i^{1/6} \qquad \text{where } C_i = \text{단계 } i \text{의 정규화된 점수}$$

> **명제 1 (OMI가 진단용인 이유).** $C_i\in[0,1]$, $\theta\in(0,1]$이고 균등 가중치를 사용할 때, $OMI\geq\theta$가 의미하는 것은 다음뿐입니다:
>
> $$\forall\, i \in \{1, \ldots, 6\}: \quad C_i \geq \theta^6$$
>
> $\theta=0.75$일 때 한 단계의 점수가 약 $0.178$까지 낮을 수 있습니다. 따라서 프로토콜은 독립적으로 선언한 하한 $C_i\geq\tau_i$와 필수 거부 조건 검사를 요구하며, OMI가 충족하지 못한 조건을 상쇄할 수는 없습니다.
>
> *증명.* $OMI\geq\theta>0$이므로 $\prod_{j=1}^{6}C_j=OMI^6>0$이고 모든 성분이 양수입니다. 따라서 $0<\prod_{j\neq i}C_j\leq1$이며 이 곱으로 나눌 수 있습니다. $C_i=OMI^6\,/\,\prod_{j\neq i}C_j\geq OMI^6\geq\theta^6$이 따릅니다. $\blacksquare$
>
> **별도의 영점 성질.** 어떤 성분 $C_j=0$이면 전체 곱이 0이므로 $OMI=0$입니다. 이는 위 명제의 역이 아니라 곱의 정의에서 따르는 별도 성질입니다.

**자격 결과**:

| OMI | 상태 |
|:---:|------|
| 각 조건의 하한과 모든 필수 기준 통과; OMI는 진단용으로 보고 | **프로파일 $\Pi$에 한정된 레벨 5 적합성** |
| 그 외 | 레벨 4.9 확장 |

---

## 14. 모듈 인벤토리

| # | 모듈 | 단계 | 설명 |
|---|------|:----:|------|
| 1 | Identity Continuity Tracker | 1 | 10,000 사이클 정체성 지속, 드리프트 탐지 |
| 2 | Cross-Domain Generalizer | 2 | 5개 도메인에 걸친 전략 전이 |
| 3 | Goal Ecology | 3 | 갈등 해결을 갖춘 자기유지 목표 계층구조 |
| 4 | Existential Planner | 4 | 4가지 붕괴 시나리오 시뮬레이션 + 복구 프로파일 |
| 5 | Strategic Multi-Agent | 5 | ≥ 3 에이전트 모델링, 기만 탐지, 연합 |
| 6 | Self-Reconstructor | 6 | 정체성 보존을 갖춘 모듈 성능 저하 + 재구축 |
| 7 | L5 Orchestrator | - | 통합 주기 + 자격 평가 |

---

## 참고 문헌

1. Parfit, D. *Reasons and Persons.* Oxford University Press, 1984. (Identity persistence, personal identity over time)
2. Kahneman, D. & Tversky, A. "Prospect Theory: An Analysis of Decision under Risk." *Econometrica* 47(2), 1979. (Cross-domain generalization, decision transfer)
3. Axelrod, R. *The Evolution of Cooperation.* Basic Books, 1984. (Multi-agent strategy, coalition dynamics)
4. Taleb, N.N. *Antifragile: Things That Gain from Disorder.* Random House, 2012. (Existential resilience, collapse recovery)
5. Von Neumann, J. & Morgenstern, O. *Theory of Games and Economic Behavior.* Princeton University Press, 1944. (Strategic multi-agent interaction)
6. Russell, S. *Human Compatible: AI and the Problem of Control.* Viking, 2019. (Autonomy safety, value alignment)
7. Bostrom, N. *Superintelligence: Paths, Dangers, Strategies.* Oxford University Press, 2014. (Proto-AGI risks, identity preservation)
8. Khalil, H.K. *Nonlinear Systems.* Prentice Hall, 3rd Edition, 2002. (Spectral stability, Lyapunov analysis)
9. Amodei, D. et al. "Concrete Problems in AI Safety." *arXiv preprint arXiv:1606.06565*, 2016. (Safety invariants, self-reconstruction constraints)

---

> **이전**: [← 레벨 4.9: 자율 전략 에이전트](Level_4_9_Autonomous_Strategic_Agent.ko.md)
