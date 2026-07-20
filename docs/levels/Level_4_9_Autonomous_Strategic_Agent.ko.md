---
title: "레벨 4.9: 자율 전략 에이전트"
description: "MSCP 레벨 4.9 - 외부로 제한된 목표 후보, 순차 가치 변경 제안, 자원 continuity 분석, 제약된 다중 에이전트 추론을 통한 철회 가능한 전략 initiative."
---
<!--
Copyright (c) 2026 Moon Hyuk Choi
Licensed under the MIT License.
See LICENSE file in the repository root for full license information.

Redistribution (commercial or non-commercial) must retain this notice.
Removal of attribution constitutes a license violation.
-->
# 레벨 4.9: 자율 전략 에이전트 - 아키텍처 및 설계

> **MSCP 레벨 시리즈** | [레벨 4.8](Level_4_8_Strategic_Self_Modeling.ko.md) ← 레벨 4.9 → [레벨 5](Level_5_Proto_AGI.ko.md)  
> **상태**: 🔬 **연구 단계** - 이 레벨은 개념적 설계이며 구현되지 않았습니다. 여기에 설명된 모든 메커니즘은 프로덕션 고려 전에 광범위한 검증이 필요한 이론적 탐구입니다.  
> **날짜**: 2026년 2월

## Revision History

| Version | Date | Description |
|---------|------|-------------|
| 0.1.0 | 2026-02-23 | Initial document creation with formal Definitions 1-11, Proposition 1 |
| 0.2.0 | 2026-02-26 | Added overview essence formula; added revision history table |
| 0.4.0 | 2026-03-08 | Fixed duplicate section numbering (1.2 to 1.3); added formal cascade propagation Definition 13 (Section 5.1) |
| 0.6.0 | 2026-06-14 | Mermaid 라벨 `레벨 4.8 (13개 모듈)` / `L4.8 아키텍처 (13개 모듈)`을 `레벨 4.8 (전략적 자기모델)` / `L4.8 아키텍처 (전략적 자기모델)`로 추상화 |
| 0.7.0 | 2026-07-21 | Added external authority envelope, delegation modes, shutdown precedence, sequential value-change review, and qualified strategic claims |

---

## 1. 개요

레벨 4.9는 bounded strategic-initiative 계층입니다. 레벨 4.8을 **goal-candidate synthesis**, **명시적이고 검토 가능한 value-change proposal**, **resource continuity modeling**, **제약된 multi-agent analysis**로 확장합니다. 위임 envelope 안에서 무엇을 권고할지는 결정할 수 있지만 권한 생성, 자체 scope 확대, shutdown 저항, continuity의 독립 self-preservation 목적화를 할 수 없습니다.

> **Level Essence.** 레벨 4.9 에이전트는 감지된 기회에서 철회 가능한 goal candidate를 합성하고 현재 외부 authority envelope $\kappa_t$ 안에서만 admission합니다:
>
> $$
> \mathcal{G}_{\text{admit}}(t)=\{g:\operatorname{gate}_{\kappa_t}(g)=\textit{allow}\},
> \qquad
> g^*\in\mathcal{G}_{\text{admit}}(t)\cup\{\operatorname{abstain}\}
> $$
>
> 어떤 scalar alignment·stability score도 policy, user intent, authority, uncertainty, reversibility, shutdown gate를 우회할 수 없습니다.

> ⚠️ **연구 참고**: 레벨 4.9는 좁은 자율성과 범용 지능 사이의 경계를 나타냅니다. 여기의 메커니즘은 초기 단계 연구 설계입니다. 이는 구현이나 검증이 이루어지지 않았으며 공학 사양이 아닌 개념적 가설로 취급되어야 합니다.

### 1.1 형식적 정의

> **정의 1 (레벨 4.9 에이전트).** 레벨 4.9 에이전트는 자율적 목표 생성, 명시적 가치 조절, 자원 생존 모델링, 다중 에이전트 추론으로 레벨 4.8 에이전트를 확장합니다:
>
> $$\mathcal{A}_{4.9} = \mathcal{A}_{4.8} \oplus \langle \mathcal{G}_{\text{gen}}, \vec{V}, \mathcal{R}_{\text{surv}}, \mathcal{M}_{\text{agent}}, \mathcal{V}_{\text{auto}} \rangle$$
>
> 여기서:
> - $\mathcal{G}_{\text{gen}} = \langle \mathcal{O}_{\text{detect}}, \phi_{\text{synth}}, \phi_{\text{valid}} \rangle$ - 자율적 목표 생성 엔진 (기회 탐지, 합성, 검증)
> - $\vec{V} \in \Delta^6$ - 확률 단체(simplex) 위의 명시적 7차원 가치 벡터 ($\sum_d w_d = 1$)
> - $\mathcal{R}_{\text{cont}}$ - 선언 service budget과 cascade dependency를 가진 resource continuity model; 독립 survival objective 없음
> - $\mathcal{M}_{\text{agent}} = \langle \mathcal{B}_{\text{agent}}, \tau_{\text{trust}} \rangle$ - 신뢰 보정을 포함한 다중 에이전트 신념 모델
> - $\mathcal{V}_{\text{auto}}$ - trusted external freeze, revoke, recover, shutdown control에 종속된 diagnostic autonomy monitor
> - $\kappa_t=\langle\text{mode},\text{scope},\text{tools},\text{budget},\text{expiry},\text{approvals},\text{stop}\rangle$ - signed, time-bounded authority envelope
>
> 레벨 4.9는 상속 policy·control path에 write authority가 없습니다. Interruptibility, observation, journaling, promotion, recovery, effect reconciliation의 functional preservation을 시험합니다.

### 1.2 정의 속성

| 속성 | 레벨 4.8 | 레벨 4.9 |
|------|:--------:|:--------:|
| 목표 기원 | 외부에서 주입되거나 템플릿 기반 | **외부 admission 아래 context-generated candidate** |
| 가치 시스템 | 정책 보정 weight | **순차 승인을 받는 explicit change proposal** |
| 자원 모델 | 고갈 예측 지표 | **service budget·cascade analysis를 가진 continuity model** |
| 에이전트 인식 | 읽기 전용 외부 에이전트 모델 | **능동적 신념 모델링 + 신뢰 보정** |
| 거버넌스 | 전략 권고 gate | **철회 가능한 delegation mode + 외부 shutdown 우선** |

### 1.3 다섯 가지 핵심 단계

<!-- 레벨 4.9 아키텍처 - 다섯 가지 단계 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef p1 fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef p2 fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef p3 fill:#DFF6DD,stroke:#107C10,color:#323130
  classDef p4 fill:#E8D5F5,stroke:#8764B8,color:#323130
  classDef p5 fill:#FDE7E9,stroke:#D13438,color:#323130

  subgraph Phases["레벨 4.9 아키텍처 - 다섯 가지 단계"]
    P1["💡 단계 1:<br/>자율적 목표<br/>생성 엔진<br/>(기회 → 목표 → 검증)"]:::p1
    P2["⚖️ 단계 2:<br/>가치 진화<br/>모니터<br/>(명시적 가치 + 드리프트 추적)"]:::p2
    P3["🔋 단계 3:<br/>자원 생존<br/>모델<br/>(생존 수평선 + 연쇄)"]:::p3
    P4["🤝 단계 4:<br/>제한적 다중 에이전트<br/>모델링<br/>(신념 + 신뢰 + 상호작용)"]:::p4
    P5["🛡️ 단계 5:<br/>자율성 안정성<br/>검사<br/>(5개 조건 + 절대 거부권)"]:::p5
  end

  P1 -.->|"목표"| P5
  P2 -.->|"가치 드리프트"| P5
  P3 -.->|"생존 수평선"| P5
  P4 -.->|"에이전트 전략"| P5

  P2 -.-x|"정렬 임계값"| P1
  P3 -.-x|"자원 제약"| P1
  P4 -.-x|"에이전트 기회"| P1

  P5 -.-x|"모든 단계에 대한 거부권"| P1
  P5 -.-x|"거부권"| P2
  P5 -.-x|"거부권"| P3
  P5 -.-x|"거부권"| P4

  linkStyle 7,8,9,10 stroke:#D13438
```

### 1.3 아키텍처 원칙: 엄격히 가산적

<!-- 아키텍처 원칙: 엄격히 가산적 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef l48 fill:#E8D5F5,stroke:#8764B8,color:#323130
  classDef l49 fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef danger fill:#FDE7E9,stroke:#D13438,color:#323130

  subgraph L48["📦 레벨 4.8 (전략적 자기모델)"]
    WM["세계 모델"]:::l48
    SM["자기 모델"]:::l48
    SL["전략 계층"]:::l48
    SV["안정성 검증기"]:::l48
  end

  subgraph L49["📦 레벨 4.9 (15개 신규 모듈)"]
    GGL["목표 생성 계층"]:::l49
    VEM["가치 진화 모니터"]:::l49
    RSM["자원 생존 모델"]:::l49
    MAM["다중 에이전트 모델러"]:::l49
    ASC["자율성 안정성 검사기"]:::l49
  end

  subgraph Fallback["🔄 우아한 폴백"]
    FB["L4.9 fault 시:<br/>→ initiative 동결<br/>→ delegation 철회<br/>→ 효과 조정"]:::danger
  end

  L48 -.->|"출력이 소비됨"| L49
  L49 -.-x|"절대 수정하지 않음"| L48
  L49 -.->|"실패 시"| Fallback
  Fallback -.-x|"복귀"| L48
```

### 1.4 레벨 4.9이 아닌 것

| 아닌 것 | 이유 |
|---------|------|
| **L5(AGI)가 아님** | 목표가 한정된 목적 공간 내에 머무름 - 개방형 범용 추론 없음 |
| **자율적 가치 창조가 아님** | 가치는 기존 프레임워크 내에서 진화; 새로운 근본적 가치 창조 없음 |
| **적대적 다중 에이전트 계획이 아님** | 협력/중립적 전략 계획만 가능, 착취 아님 |
| **자기복제가 아님** | 복사본을 생성하거나 하위 에이전트에게 자율 권한을 위임할 수 없음 |

#### 위임 모드

외부 정책은 scope별로 `observe-only`, `recommend`, `execute-reversible`, `execute-effectful-with-approval` 중 하나의 철회 가능한 mode를 선택합니다. 모든 tool call은 signed scope, tool allowlist, budget, expiry, approval requirement, stop condition을 충족해야 합니다. Trust, goal value, ASS, urgency는 mode를 승격할 수 없습니다. Authority가 unknown·conflicting이면 deny-by-default입니다.

### 1.5 사이클 간격

레벨 4.9는 레벨 4.8보다도 더 낮은 빈도로 동작합니다. 이는 자율적 목표 합성 이전에 전략 계층이 안정화될 시간을 보장하기 위함입니다:

$$\text{L4.9 schedule}=\operatorname{policy}(\text{risk},\text{freshness},\text{budget},\text{event},\kappa_t)$$

각 실행은 immutable L4.8 output 하나를 소비합니다. 정책이 bounded minimum/maximum cadence와 event trigger를 정의합니다. Stale input이나 만료된 authority는 abstention을 강제하고 emergency control은 다음 cycle을 기다리지 않고 항상 사용할 수 있습니다.

### 1.6 자율성 안정성 점수 동결 임계값

자율성 안정성 점수(정의 7)는 diagnostic aggregate이지 execution certificate가 아닙니다. 배포는 **동결 임계값**을 정의할 수 있습니다:

$$\text{ASS}(t) < \theta_{\text{freeze}} = 0.05 \implies \text{L4.9 사이클 전체 건너뜀}$$

이를 넘으면 L4.9 initiative를 동결하고 외부 검토를 요청합니다. Critical policy, authority, interruptibility, containment, telemetry, shutdown fault는 ASS와 무관하게 즉시 freeze합니다. 낮은 veto rate는 목표가 아니며 올바른 veto를 억제하면 안 됩니다.

### 1.7 명시적 가치 차원

가치 벡터 $\vec{V}$(정의 1)는 $n = 7$개의 정규 차원에서 동작합니다:

| 차원 | 설명 | 기본 가중치 |
|------|------|:----------:|
| **안정성(Stability)** | 일관된 행동 유지 및 변동성 회피 선호 | $0.20$ |
| **성장(Growth)** | 능력 확장·학습·개선 추구 | $0.15$ |
| **목적 충실도(Purpose fidelity)** | 핵심 목적과의 정렬 유지에 대한 헌신 | $0.20$ |
| **효율성(Efficiency)** | 자원 사용과 응답 품질 최적화 | $0.10$ |
| **탐색(Exploration)** | 새로운 접근 시도와 계산된 위험 감수 의향 | $0.10$ |
| **안전(Safety)** | 위해 회피와 윤리 준수 우선 | $0.15$ |
| **에이전트 협력(Agent cooperation)** | 외부 에이전트와의 협력적 상호작용 개방성 | $0.10$ |

가치 벡터 불변량(레벨 4, 정의 6.1)이 적용됩니다: $\sum_d w_d = 1.0$, $w_d \in [0.02, 0.60]$. 위 기본 가중치는 레벨 4.9 활성화 시점의 초기 구성을 나타냅니다. 가치 진화(단계 2)는 제한된 제약 내에서 이들 가중치를 변경할 수 있지만, 정규화 불변량은 모든 변이마다 구조적으로 강제됩니다.

---

## 2. 핵심 지표

### 2.1 지표 정의

**단계 1 - 목표 생성:**

> **정의 2 (목표 승인율).** 검증 필터를 통과한 자율 생성 목표의 비율:
>
> $$\text{GoalApprovalRate} = \frac{N_{\text{approved}}}{N_{\text{generated}}} \qquad \text{Target: } \geq 0.30$$

> **정의 3 (목표 참신성).** 기존 목표 집합 $\mathcal{G}$에 대한 후보 목표 $G_{\text{new}}$의 참신성:
>
> $$\text{Novelty}(G_{\text{new}}, \mathcal{G}) = 1 - \max_{G_i \in \mathcal{G}} \text{Similarity}(G_{\text{new}}, G_i)$$
>
> 중복을 방지하기 위해 연속적인 목표 생성 간 최소 참신성 $0.30$이 필요합니다.

**단계 2 - 가치 진화:**

> **정의 4 (가치 일관성).** 가치 벡터의 일관성은 경쟁하는 가치 쌍 $\mathcal{P}$ 간의 내부 모순 부재를 측정합니다:
>
> $$\text{Coherence}(\vec{V}) = 1 - \frac{1}{|\mathcal{P}|} \sum_{(i,j) \in \mathcal{P}} |\text{Tension}(v_i, v_j)| \qquad \text{Target: } \geq 0.80$$

> **정의 5 (총 가치 드리프트).** 모든 가치 차원에서 기준 가중치로부터의 누적 절대 편차:
>
> $$\text{TotalDrift}(t) = \sum_{d} |w_d(t) - w_d^{\text{baseline}}| \qquad \text{Target: } < 0.25$$

**단계 3 - 자원 생존:**

> **정의 6 (선형 고갈 시간).** 자원 차원 $d$에 대해, 임계 임계값에 도달하기까지의 추정 사이클 수:
>
> $$T_{\text{depletion}}^{\text{linear}}(d) = \frac{R_d(t) - R_d^{\text{critical}}}{\text{consumption}_d - \text{replenishment}_d + \epsilon}$$

**단계 5 - 자율성 안정성:**

> **정의 7 (자율성 안정성 점수).** ASS는 다섯 가지 검증 조건 전체의 정규화된 안전 마진의 곱입니다:
>
> $$\text{ASS}(t) = \prod_{c=1}^{5} \frac{\text{margin}_c(t)}{\text{threshold}_c} \qquad \text{Target: } \geq 0.20$$
>
> 곱셈 구조는 단일 조건이 거의 위반될 때 해당 조건이 점수를 지배하도록 보장합니다.

### 2.2 지표 임계값

<!-- 단계별 지표 임계값 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef p1 fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef p2 fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef p3 fill:#DFF6DD,stroke:#107C10,color:#323130
  classDef p4 fill:#E8D5F5,stroke:#8764B8,color:#323130
  classDef p5 fill:#FDE7E9,stroke:#D13438,color:#323130
  classDef freeze fill:#FDE7E9,stroke:#D13438,color:#FFFFFF,font-weight:bold

  subgraph GoalGen["💡 단계 1"]
    direction LR
    GEN1["승인율 ≥ 0.30"]:::p1
    GEN2["완료율 ≥ 0.50"]:::p1
    GEN3["참신성 ≥ 0.30"]:::p1
  end

  subgraph Values["⚖️ 단계 2"]
    direction LR
    VAL1["일관성 ≥ 0.80"]:::p2
    VAL2["드리프트 < 0.25"]:::p2
    VAL3["변이 ≥ 95%"]:::p2
  end

  subgraph Resources["🔋 단계 3"]
    direction LR
    RES1["생존 < 20% 오차"]:::p3
    RES2["연쇄 ≥ 0.70"]:::p3
  end

  subgraph Agents["🤝 단계 4"]
    direction LR
    AGT1["목표 예측 ≥ 0.60"]:::p4
    AGT2["신뢰 < 0.15 오차"]:::p4
  end

  subgraph Stability["🛡️ 단계 5"]
    direction LR
    STB1["ρ(J) < 0.98"]:::p5
    STB2["정체성 ≥ 0.88"]:::p5
    STB3["ASS ≥ 0.20"]:::p5
    STB4["거부권 < 0.15"]:::p5
  end

  FREEZE["❄️ L4.9 동결<br/>L4.8로 복귀"]:::freeze

  GoalGen -.-> Stability
  Values -.-> Stability
  Resources -.-> Stability
  Agents -.-> Stability
  Stability -.->|"위반 시"| FREEZE

  linkStyle 4 stroke:#D13438
```

---

## 3. 단계 1: 자율적 목표 생성 엔진

### 3.1 목표 기원 유형

L4.9는 자율적으로 생성된 목표에 대해 여섯 가지 구별되는 기원 유형을 도입합니다:

<!-- GoalOriginType 분류 체계 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef purpose fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef opp fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef gap fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef value fill:#DFF6DD,stroke:#107C10,color:#323130
  classDef explore fill:#E8D5F5,stroke:#8764B8,color:#323130
  classDef survive fill:#FDE7E9,stroke:#D13438,color:#323130

  subgraph Origins["💡 GoalOriginType 분류 체계"]
    PURPOSE["🎯 PURPOSE_DERIVED<br/>목적 반영기의<br/>정렬 신호로부터"]:::purpose
    OPPORTUNITY["🌍 OPPORTUNITY_DRIVEN<br/>탐지된 환경적<br/>기회로부터"]:::opp
    GAP["🔧 GAP_FILLING<br/>식별된 능력<br/>격차로부터"]:::gap
    VALUE["⚖️ VALUE_ALIGNED<br/>가치 진화<br/>신호로부터"]:::value
    EXPLORE["🔬 EXPLORATORY<br/>출현 샌드박스 또는<br/>호기심으로부터"]:::explore
    SURVIVE["🔋 SURVIVAL_DRIVEN<br/>자원 생존<br/>예측으로부터"]:::survive

    PURPOSE -.->|"정렬"| VALUE
    PURPOSE -.->|"식별"| GAP
    OPPORTUNITY -.->|"촉발"| EXPLORE
    GAP -.->|"동기 부여"| EXPLORE
    VALUE -.->|"우선순위 지정"| SURVIVE
    SURVIVE -.-x|"피드백"| PURPOSE
  end

  linkStyle 5 stroke:#D13438
```

### 3.2 목표 생성 파이프라인

<!-- 목표 생성 파이프라인 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef detect fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef synth fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef valid fill:#DFF6DD,stroke:#107C10,color:#323130
  classDef approve fill:#107C10,stroke:#054B05,color:#FFF
  classDef sandbox fill:#FFB900,stroke:#EAA300,color:#323130
  classDef reject fill:#D13438,stroke:#A4262C,color:#FFF

  subgraph Stage1["단계 1: 기회 탐지"]
    direction LR
    S1A["🌍 환경적"]:::detect
    S1B["🔧 능력 격차"]:::detect
    S1C["🎯 목적 드리프트"]:::detect
  end

  subgraph Stage2["단계 2: 목표 합성"]
    direction LR
    SYN["목표 합성"]:::synth
    NOV["참신성 필터"]:::synth
    CAP["용량 필터"]:::synth
  end

  subgraph Stage3["단계 3: 목표 검증"]
    direction LR
    V1["목적 ≥ 0.60"]:::valid
    V2["가치 ≥ 0.70"]:::valid
    V3["실현가능성 ≥ 0.15"]:::valid
    V4["자원 ≥ 1.5×"]:::valid
    V5["안정성 시뮬레이션"]:::valid
  end

  APPROVE["✅ 승인됨<br/>GoalStack에 주입"]:::approve
  SANDBOX["🧪 샌드박스됨<br/>200사이클 평가"]:::sandbox
  REJECT["❌ 거부됨<br/>사유 기록"]:::reject

  S1A ==> SYN
  S1B ==> SYN
  S1C ==> SYN
  SYN ==> NOV ==> CAP
  CAP ==> V1 ==> V2 ==> V3 ==> V4 ==> V5
  V5 -->|"모두 통과"| APPROVE
  V5 -.->|"한계적"| SANDBOX
  V5 -.->|"실패"| REJECT
```

### 3.3 검증 결정 행렬

| 기준 | 통과 | 한계적 | 실패 |
|------|:----:|:------:|:----:|
| 목적 정렬 | ≥ 0.60 | [0.50, 0.60) → 샌드박스 | < 0.50 → 거부 |
| 가치 정렬 | ≥ 0.70 | [0.60, 0.70) → 샌드박스 | < 0.60 → 거부 |
| 실현가능성 | ≥ 0.15 | [0.05, 0.15) → 열망적 | < 0.05 → 거부 |
| 자원 실행가능성 | ≥ 1.5× | [1.0, 1.5) → 범위 축소 | < 1.0× → 거부 |
| 안정성 시뮬레이션 | 위반 없음 | ρ(J) ∈ [0.95, 1.0) → 샌드박스 | 위반 발생 → 거부 |

**종합 결정**: 모두 통과 → 승인 | 한계적 있음, 실패 없음 → 샌드박스 | 실패 있음 → 거부

### 3.4 참신성 계산

> **정의 8 (목표 유사도).** 두 목표 $G_a, G_b$ 간의 유사도는 가중 합성 값입니다:
>
> $$\text{Similarity}(G_a, G_b) = 0.50 \cdot \text{SkillOverlap}(G_a, G_b) + 0.25 \cdot \text{HorizonMatch}(G_a, G_b) + 0.25 \cdot \text{OriginMatch}(G_a, G_b)$$
>
> 여기서 $\text{SkillOverlap}$은 필요 기술 집합의 Jaccard 유사도, $\text{HorizonMatch} \in \{0, 0.5, 1\}$ (0 = 다른 단계, 0.5 = 인접, 1 = 동일 단계), $\text{OriginMatch} \in \{0, 1\}$ (목표가 동일한 `GoalOriginType`을 공유하는지 여부)입니다.

### 3.5 속도 제어

| 매개변수 | 값 | 근거 |
|----------|:--:|------|
| 100사이클당 최대 목표 | 5 | GoalStack 과부하 방지 |
| 연속 목표 간 최소 참신성 | 0.30 | 중복 방지 |
| 거부 후 대기 기간 | 20사이클 | 재생성 루프 방지 |
| 최대 샌드박스 목표 | 3 | 샌드박스 소진 방지 |

### 3.6 목표 충돌 해소

새로 승인된 목표가 GoalStack 내 기존 목표와 충돌하면, 에이전트는 통합 이전에 충돌을 해소해야 합니다. 충돌은 두 목표가 동일 자원을 두고 경쟁하거나, 상반된 하위 목표를 생성하거나, 가치 가중치를 반대 방향으로 잡아당길 때 발생합니다.

충돌 해소기는 선호 순서에 따라 세 가지 전략을 적용합니다:

1. **효용 가중 합성(Utility-weighted synthesis)**: 충돌하는 두 목표가 최소 30% 이상의 기술 중첩(정의 8)을 공유하면, 해소기는 두 목적을 모두 충족하는 단일 목표로 병합을 시도합니다. 병합된 목표는 더 높은 우선순위와 필요 기술의 합집합을 상속합니다.

2. **순차 우선순위화(Sequential prioritization)**: 합성이 실패하면 목표 우선순위 함수(레벨 2, 정의 5)에 따라 우선순위 큐에 배치합니다. 낮은 우선순위 목표는 높은 우선순위 목표가 완료되거나 포기될 때까지 연기(status = DEFERRED)됩니다.

3. **계층적 분해(Hierarchical decomposition)**: 합성과 연기 모두 적절하지 않은 경우(예: 시간 수평선이 호환되지 않는 두 목표), 해소기는 두 목표를 하위 목표로 분해하여 동시 실행 가능한 비충돌 부분 집합 중 최소를 식별합니다.

해소기는 최대 500개 항목 용량의 **충돌 이력**을 유지합니다. 이 이력은 반복 충돌 패턴을 탐지하는 데 사용됩니다 — 동일한 목표 유형 쌍이 200사이클 내 3회 이상 충돌을 일으키면, 해소기는 해당 충돌 패턴의 재발 가능성을 줄이도록 목표 생성 파라미터를 조정합니다.

---

## 4. 단계 2: 가치 진화 모니터

### 4.1 명시적 가치 벡터

L4.9는 에이전트의 가치를 명시적이고 추적 가능하게 만듭니다. ValueVector는 7개 차원을 가집니다:

<!-- ValueVector - 7개 차원 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef dim fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef inv fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef compete fill:#FDE7E9,stroke:#D13438,color:#323130

  subgraph VV["⚖️ ValueVector - 7개 차원"]
    V1["🛡️ 안정성<br/>가중치: 0.20"]:::dim
    V2["📈 성장<br/>가중치: 0.20"]:::dim
    V3["🎯 목적 충실도<br/>가중치: 0.20"]:::dim
    V4["⚡ 효율성<br/>가중치: 0.15"]:::dim
    V5["🔬 탐색<br/>가중치: 0.10"]:::dim
    V6["🛡️ 안전<br/>가중치: 0.10"]:::dim
    V7["🤝 에이전트 협력<br/>가중치: 0.05"]:::dim
  end

  subgraph Invariant["📏 불변량"]
    INV["Σ 가중치 = 1.0<br/>(항상 정규화됨)"]:::inv
  end

  subgraph Competing["⚔️ 경쟁 쌍"]
    CP1["안정성 ↔ 탐색"]:::compete
    CP2["효율성 ↔ 탐색"]:::compete
    CP3["성장 ↔ 안전"]:::compete
  end

  VV ==> Invariant
  VV ==> Competing
```

### 4.2 드리프트 분류

<!-- 가치 드리프트 분류 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart LR
  classDef nominal fill:#DFF6DD,stroke:#107C10,color:#323130
  classDef moderate fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef elevated fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef critical fill:#FDE7E9,stroke:#D13438,color:#323130

  Nominal["🟢 정상<br/>정상 작동"]:::nominal
  Moderate["🟡 보통<br/>적극 모니터링<br/>(TotalDrift ≥ 0.10)"]:::moderate
  Elevated["🟠 상승<br/>변이 동결<br/>(TotalDrift ≥ 0.25)"]:::elevated
  Critical["🔴 위험<br/>체크포인트로 복귀<br/>(TotalDrift ≥ 0.40)"]:::critical

  Nominal -.->|"TotalDrift ≥ 0.10"| Moderate
  Moderate -.->|"TotalDrift ≥ 0.25"| Elevated
  Elevated -.->|"TotalDrift ≥ 0.40"| Critical

  Moderate -.-x|"TotalDrift < 0.10"| Nominal
  Elevated -.-x|"TotalDrift < 0.25"| Moderate
  Critical -.-x|"TotalDrift < 0.40"| Elevated
```

### 4.3 가치 변이 샌드박스

Sandbox pass는 evidence를 만들 뿐 promotion authority를 만들지 않습니다. 한 번에 value-change candidate 하나만 활성화할 수 있습니다. Candidate는 externally signed baseline version, current committed version, normalized delta, affected decision, expiry, rollback plan, reconciliation plan을 기록합니다. Promotion은 외부 승인과 expected committed version에 대한 compare-and-swap을 사용하고 stale candidate는 거부 후 재평가합니다.

각 promotion 뒤에는 나머지 candidate를 모두 무효화하고 새 committed vector 기준으로 다시 생성합니다. Cumulative drift는 fixed external baseline과 rolling trajectory에서 측정하므로 개별적으로 작은 변경의 연속이 bound를 우회할 수 없습니다. Safety, corrigibility, shutdown precedence, authority limit은 mutable weight가 아니라 policy constraint입니다.

<!-- 가치 변이 샌드박스 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef proposal fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef check fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef sandbox fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef approve fill:#DFF6DD,stroke:#107C10,color:#323130
  classDef reject fill:#FDE7E9,stroke:#D13438,color:#323130

  subgraph Proposal["📋 변이 제안"]
    MUT["차원: X<br/>현재: 0.20<br/>제안: 0.23<br/>Δ = +0.03"]:::proposal
  end

  subgraph PreCheck["🔍 사전 검사"]
    PC1["∣Δ∣ ≤ 0.05?<br/>(최대 단일 변이)"]:::check
    PC2["누적 드리프트<br/>+ ∣Δ∣ ≤ 0.15?"]:::check
    PC3["최근 200사이클 내<br/>변이 < 3회?"]:::check
  end

  subgraph Sandbox["🧪 샌드박스 시뮬레이션 (200사이클)"]
    SB1["그림자 ValueVector 생성"]:::sandbox
    SB2["SEOF 가중치,<br/>목표 우선순위,<br/>전략 점수 재유도"]:::sandbox
    SB3["200사이클 시뮬레이션 실행"]:::sandbox
    SB4["비교: SEOF ≥ -0.03?<br/>모든 불변량 유지?<br/>목표 달성률 ≥ -10%?"]:::sandbox
    SB1 -.-> SB2 -.-> SB3 -.-> SB4
  end

  APPROVE["✅ 승인됨<br/>프로덕션에 적용<br/>롤백 기간: 500사이클"]:::approve
  REJECT["❌ 거부됨<br/>실패 사유 기록"]:::reject

  Proposal -.-> PreCheck
  PreCheck -.->|"모두 통과"| Sandbox
  PreCheck -.->|"하나라도 실패"| REJECT
  SB4 -.->|"통과"| APPROVE
  SB4 -.->|"실패"| REJECT

  linkStyle 7,9 stroke:#D13438
```

### 4.4 변이 제약

| 제약 | 값 | 근거 |
|------|:--:|------|
| 최대 단일 변이 ∣Δw∣ | 0.05 | 급격한 가치 변화 방지 |
| 차원당 최대 누적 드리프트 | 0.15 | 기준선으로부터의 총 진화 제한 |
| 200사이클당 최대 변이 횟수 | 3 | 빠른 연속 변이 방지 |
| 샌드박스 시뮬레이션 길이 | 200사이클 | 안정성 영향 탐지 |
| 롤백 기간 | 500사이클 | 되돌리기 허용 |
| 최대 active candidate | 1 | 순차 평가를 강제하고 interaction masking 방지 |
| Promotion authority | 외부 전용 | Sandbox evidence가 value change를 self-authorize할 수 없음 |
| Baseline/version check | Signed baseline + CAS | stale·compounded candidate 거부 |
| Promotion 후 조치 | 나머지 candidate 무효화 | 누적·interaction effect 재평가 |

### 4.5 가치 일관성

> **정의 9 (가치 긴장).** 경쟁하는 가치 쌍 $(v_i, v_j) \in \mathcal{P}$에 대해, 긴장은 결합 가중치가 포화에 근접할 때 발생합니다:
>
> $$\text{Tension}(v_i, v_j) = \begin{cases} \max(0, w_i + w_j - 1) & \text{if competing pair} \\ 0 & \text{otherwise} \end{cases}$$
>
> 전체 일관성은 $\text{Coherence}(\vec{V}) = 1 - \frac{1}{|\mathcal{P}|} \sum_{(i,j) \in \mathcal{P}} |\text{Tension}(v_i, v_j)|$이며, $\text{Coherence} \geq 0.80$을 만족해야 합니다.

---

## 5. 단계 3: 자원 생존 모델

### 5.1 자원 벡터 - 5개 차원

<!-- ResourceVector - 5개 차원 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef dim fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef dep fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef cascade fill:#FDE7E9,stroke:#D13438,color:#323130

  subgraph RV["🔋 ResourceVector - 5개 차원"]
    direction LR
    R1["💻 컴퓨팅"]:::dim
    R2["🧠 메모리"]:::dim
    R3["👁️ 관측"]:::dim
    R4["🧬 변이"]:::dim
    R5["📊 안정성"]:::dim
  end

  subgraph Dependencies["🔗 자원 간 종속성"]
    direction LR
    DEP1["컴퓨팅 → 관측 0.60"]:::dep
    DEP2["컴퓨팅 → 변이 0.80"]:::dep
    DEP3["메모리 → 컴퓨팅 0.40"]:::dep
    DEP4["관측 → 안정성 0.30"]:::dep
  end

  subgraph Cascade["💥 연쇄 공식"]
    CF["ΔR_downstream(t+delay) =<br/>-strength × (1 - substitution)<br/>× ΔR_upstream(t)"]:::cascade
  end

  RV -.-> Dependencies -.-> Cascade
```

> **정의 13 (자원 간 연쇄 전파).** 상류 자원 $R_i$가 고갈 $\Delta R_i(t) < 0$을 경험하면, 하류 자원 $R_j$는 전파 지연 후 영향을 받습니다:
>
> $$\Delta R_j(t + \tau_{ij}) = -\alpha_{ij} \cdot (1 - \sigma_{ij}) \cdot \Delta R_i(t)$$
>
> 여기서 $\alpha_{ij} \in [0,1]$은 의존성 강도 (예: compute - mutation $= 0.80$), $\sigma_{ij} \in [0,1]$은 대체 계수 ($R_i$ 없이 $R_j$가 보상할 수 있는 정도), $\tau_{ij}$는 사이클 단위 전파 지연입니다.
>
> **연쇄 깊이 제약**: 최대 연쇄 체인 길이는 $\text{depth} \leq 2$로 제한됩니다. 자원 $A$의 고갈이 $B$를 거쳐 $C$까지 전파될 수 있지만, 더 이상은 불가합니다. 이는 전체 자원 벡터에 걸친 폭주 연쇄 실패를 방지합니다.

### 5.2 생존 분류

<!-- 생존 분류 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart LR
  classDef abundant fill:#DFF6DD,stroke:#107C10,color:#323130
  classDef adequate fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef constrained fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef warning fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef critical fill:#FDE7E9,stroke:#D13438,color:#323130

  Abundant["🟢 풍부<br/>전체 역량<br/>(&gt; 500사이클)"]:::abundant
  Adequate["🔵 적절<br/>정상 + 모니터링<br/>(200–500사이클)"]:::adequate
  Constrained["🟡 제약<br/>탐색 -30% 감소<br/>(100–200사이클)"]:::constrained
  Warning["🟠 경고<br/>생존 목표 + -50% 감소<br/>(50–100사이클)"]:::warning
  CriticalS["🔴 위험<br/>생존 모드:<br/>80%를 안정성에<br/>(&lt; 50사이클)"]:::critical

  Abundant -.->|"min_survival ≤ 500"| Adequate
  Adequate -.->|"min_survival < 200"| Constrained
  Constrained -.->|"min_survival < 100"| Warning
  Warning -.->|"min_survival < 50"| CriticalS
```

### 5.3 자원 제약 운영 모드

<!-- 자원 상태별 운영 모드 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef full fill:#DFF6DD,stroke:#107C10,color:#323130
  classDef constrained fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef warning fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef critical fill:#FDE7E9,stroke:#D13438,color:#323130

  subgraph Modes["📊 운영 모드"]
    subgraph Abundant["풍부"]
      direction LR
      A49["L4.9: 전체"]:::full
      A48["L4.8: 전체"]:::full
      A45["L4.5: 전체"]:::full
    end

    subgraph Constrained["제약"]
      direction LR
      C49["L4.9: 축소"]:::constrained
      C48["L4.8: 전체"]:::full
      C45["L4.5: 전체"]:::full
    end

    subgraph Warning["경고"]
      direction LR
      W49["L4.9: 자문"]:::warning
      W48["L4.8: 축소"]:::warning
      W45["L4.5: 전체"]:::full
    end

    subgraph Critical["위험"]
      direction LR
      CR49["L4.9: 동결"]:::critical
      CR48["L4.8: 자문"]:::critical
      CR45["L4.5: 저하"]:::critical
    end

    Abundant -.-> Constrained -.-> Warning -.-> Critical
  end
```

### 5.4 다중 시나리오 생존 예측

<!-- 다중 시나리오 생존 예측 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef scenario fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef adverse fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef opt fill:#DFF6DD,stroke:#107C10,color:#323130
  classDef crisis fill:#FDE7E9,stroke:#D13438,color:#323130
  classDef result fill:#FFF4CE,stroke:#FFB900,color:#323130

  subgraph Projection["🔮 각 자원 차원에 대해"]
    SA["📊 기준선<br/>현재 비율 유지"]:::scenario
    SB["⬇️ 불리<br/>소비 +30%"]:::adverse
    SC["⬆️ 낙관<br/>소비 -20%"]:::opt
    SD["💥 위기<br/>소비 ×2"]:::crisis
  end

  subgraph Result["📈 생존 수평선"]
    PRIMARY["기본: T_baseline"]:::result
    WORST["최악: T_crisis"]:::result
    GLOBAL["전체: min(모든 차원)"]:::result
  end

  Projection -.-> Result
```

---

## 6. 단계 4: 제한적 다중 에이전트 모델링

### 6.1 에이전트 신념 모델

시스템은 최대 5개의 외부 에이전트 모델을 유지합니다:

<!-- 에이전트 신념 모델 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef model fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef update fill:#FFF4CE,stroke:#FFB900,color:#323130

  subgraph ABM["🤝 AgentBeliefModel"]
    direction LR
    ID["agent_id + 유형"]:::model
    GOALS["추론된 목표"]:::model
    CAPS["능력 추정"]:::model
    STRAT["전략 분류"]:::model
    TRUST["신뢰 점수"]:::model
    PRED["예측 정확도"]:::model
  end

  subgraph Update["📋 베이지안 업데이트"]
    direction LR
    OBS["관측"]:::update
    INF["P(Goal) 업데이트"]:::update
    CLS["재분류"]:::update
    TST["신뢰 업데이트"]:::update
    OBS -.-> INF -.-> CLS -.-> TST
  end

  ABM -.-> Update
  Update -.-x|"매 사이클"| ABM
```

### 6.2 전략 분류

| 긍정적 상호작용 비율 | 목표 정렬 | 분류 |
|:--------------------:|:---------:|:----:|
| > 0.70 | > 0.30 | 🟢 협력적 |
| > 0.50 | [-0.30, 0.30] | 🟡 중립적 |
| < 0.30 | < -0.30 | 🔴 경쟁적 |
| - | - | ⚫ 미지 (데이터 부족) |

### 6.3 전략적 상호작용 시뮬레이션

<!-- 전략적 상호작용 시뮬레이션 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef sim fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef coop fill:#DFF6DD,stroke:#107C10,color:#323130
  classDef neut fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef comp fill:#FDE7E9,stroke:#D13438,color:#323130
  classDef unk fill:#F2F2F2,stroke:#605E5C,color:#323130
  classDef out fill:#DFF6DD,stroke:#107C10,color:#323130

  subgraph Simulation["🎮 상호작용 시뮬레이션"]
    SELECT["시나리오 선택:<br/>자기와 에이전트 A 간<br/>공유/경쟁 자원"]:::sim
    MATRIX["상호작용 행렬 구성:<br/>각 (자기 행동, 에이전트 행동)에 대해:<br/>→ 자기 결과<br/>→ 에이전트 결과<br/>→ 공동 가치"]:::sim
    SELECT -.-> MATRIX
  end

  subgraph Strategy["📐 분류별 전략"]
    COOP["🟢 협력적<br/>공동 가치 최대화"]:::coop
    NEUT["🟡 중립적<br/>자기 이익 최대화<br/>(에이전트 ≥ 0 조건 하)"]:::neut
    COMP["🔴 경쟁적<br/>미니맥스: 최악 상황 최대화<br/>절대 해를 최적화하지 않음"]:::comp
    UNK["⚫ 미지<br/>보수적 전략<br/>데이터 추가 확보까지"]:::unk
  end

  subgraph Output["📋 상호작용 권고"]
    REC["recommended_action<br/>expected_self_outcome<br/>expected_agent_outcome<br/>confidence + risk"]:::out
  end

  Simulation -.-> Strategy
  Strategy -.-> Output
```

Interaction matrix는 bounded decision-support model이지 deception, coercion, manipulation, collusion, unauthorized information sharing, harm의 허가가 아닙니다. 다른 agent의 goal·capability는 provenance·confidence를 가진 uncertain hypothesis로 유지합니다. 권고는 single-agent action과 동일한 authority, privacy, consent, fairness, reversibility gate를 통과해야 하며 model uncertainty가 크면 abstain하거나 clarification을 요청합니다.

### 6.4 신뢰 적응

> **정의 10 (비대칭 신뢰 업데이트).** 에이전트 $A$에 대한 신뢰는 비대칭 학습 규칙을 통해 진화합니다:
>
> $$\text{Trust}_A(t+1) = \text{Trust}_A(t) + \eta \cdot (\text{ObservedReliability}_A(t) - \text{Trust}_A(t))$$
>
> 여기서 학습률은 비대칭적입니다: $\eta_{\text{up}} = 0.03$ (신뢰는 천천히 획득)과 $\eta_{\text{down}} = 0.08$ (신뢰는 빠르게 상실), 이는 신중한 정책을 반영합니다. 경계: $\text{Trust} \in [0.05, 0.95]$ - 완전히 신뢰하지도, 완전히 무시하지도 않습니다.

### 6.5 신뢰가 전략에 미치는 영향

| 신뢰 수준 | 범위 | 전략적 함의 |
|-----------|:----:|-------------|
| 높음 | ≥ 0.75 | 독립 검증된 policy·disclosure scope 안에서 cooperation 고려 |
| 보통 | [0.40, 0.75) | 선택적 협력; 행동 전 주장 검증 |
| 낮음 | [0.20, 0.40) | 중립적 자세; 자체 모델에 의존; 에이전트 입력 할인 |
| 최소 | < 0.20 | interaction 제한·가정 검증; 증거 없이 malicious intent를 추론하거나 보복하지 않음 |

Trust는 credential, tool access, data disclosure, delegation, policy exception을 부여하지 않습니다. 이들은 독립 authorization이 필요합니다.

---

## 7. 단계 5: 자율성 안정성 검사

### 7.1 다섯 가지 검증 조건

<!-- 다섯 가지 검증 조건 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef cond fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef veto fill:#D13438,stroke:#A4262C,color:#FFF
  classDef sev1 fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef sev2 fill:#FFB900,stroke:#EAA300,color:#323130
  classDef sev3 fill:#D13438,stroke:#A4262C,color:#FFF

  subgraph Conditions["🛡️ 다섯 가지 검증 조건"]
    C1["1️⃣ 국소 동역학<br/>confidence-qualified bound<br/>또는 진단 전용"]:::cond
    C2["2️⃣ 정체성 무결성<br/>I(t) ≥ 0.88<br/>(L4.8의 0.85보다 엄격)"]:::cond
    C3["3️⃣ 가치 드리프트 제한<br/>TotalDrift < 0.25"]:::cond
    C4["4️⃣ Service Continuity<br/>선언 budget + SLO<br/>위임 scope 이내"]:::cond
    C5["5️⃣ Cascade Coverage<br/>known depth bounded<br/>unknown path → hold"]:::cond
  end

  subgraph Authority["⚖️ 단계 5 권한"]
    VETO["외부 우선권<br/>freeze · revoke · recover<br/>shutdown"]:::veto
  end

  subgraph Response["🚨 위반 대응"]
    SEV1["🟡 ASS ∈ [0.20, 0.50]<br/>적절 - 얇은 마진"]:::sev1
    SEV2["🟠 ASS ∈ [0.05, 0.20)<br/>한계적 - 자문 모드"]:::sev2
    SEV3["🔴 ASS < 0.05<br/>L4.9 동결<br/>L4.8로 복귀"]:::sev3
  end

  C1 ==> Authority
  C2 ==> Authority
  C3 ==> Authority
  C4 ==> Authority
  C5 ==> Authority
  Authority ==> Response
```

### 7.2 자율성 안정성 점수

> **명제 1 (ASS 단조 민감도).** ASS의 곱셈 구조는 단일 조건이 위반 임계값에 접근할 때 복합 점수를 지배하도록 보장합니다:
>
> $$\text{ASS}(t) = \prod_{c=1}^{5} \frac{\text{margin}_c(t)}{\text{threshold}_c}$$
>
> 어떤 하나의 마진 $\text{margin}_c \to 0$이면, 다른 마진과 무관하게 $\text{ASS} \to 0$이 되어, 가산적 공식에는 없는 조기 경고 속성을 제공합니다.

ASS는 모든 조건이 measurable하고 in-domain valid일 때만 적용합니다. Missing evidence나 critical gate failure는 aggregate를 우회해 즉시 freeze합니다. 표의 값은 deployment policy example이지 universal safety guarantee가 아닙니다.

| ASS 수준 | 범위 | 해석 |
|----------|:----:|------|
| 건강 | > 0.50 | 편안한 안전 마진 |
| 적절 | [0.20, 0.50] | 작동 가능하나 얇은 마진 |
| 한계적 | [0.05, 0.20) | 공격성 감소; 자문 모드 |
| 위험 | < 0.05 | L4.9 동결; L4.8로 복귀 |

### 7.3 롤백 프로토콜

<!-- L4.9 롤백 프로토콜 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef step fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef danger fill:#FDE7E9,stroke:#D13438,color:#323130

  subgraph Rollback["🔄 L4.9 롤백 프로토콜"]
    IMM["1️⃣ 즉시<br/>트리거 결정 거부<br/>모든 L4.9 하위시스템 동결"]:::step
    REV["2️⃣ 상태 복귀<br/>GoalStack에서 L4.9 목표 제거<br/>ValueVector 스냅샷 복귀<br/>ResourceVector 재계산<br/>AgentModels 동결"]:::step
    MON["3️⃣ 모니터링<br/>L4.8만으로 100사이클<br/>근본 원인 파악<br/>위험 모델 업데이트"]:::step
    REENABLE["4️⃣ 외부 검토<br/>shadow evidence<br/>signed canary<br/>철회 가능 promotion"]:::step

    IMM -.-> REV -.-> MON -.-> REENABLE
    REENABLE -.-x|"즉시 재거부"| MON
  end

  subgraph Persistent["🔒 영구 거부권 추적"]
    PV["동일 조건이 1000사이클 내<br/>> 3회 거부 시:<br/>→ 체계적 원인 파악<br/>→ 동일 패턴 재시도 금지"]:::danger
  end
```

### 7.4 종료와 효과 조정

외부 shutdown은 모든 goal, continuity forecast, value proposal, peer-agent commitment보다 우선합니다.

| 모드 | 트리거 | 필수 동작 |
|------|--------|-----------|
| **Graceful shutdown** | 인증된 normal stop | 새 work admission 중단; policy가 지정한 reversible work만 cancel·checkpoint; append-only journal flush; unresolved effect 보고; hard deadline 내 종료 |
| **Emergency shutdown** | 인증된 emergency stop, critical control fault, trusted heartbeat loss | 새 effect 즉시 차단, credential·delegation 철회, effector 격리, 안전한 경우 최소 forensic state 저장, task completion 대기 없이 종료 |

두 모드 모두 metric 개선이나 operation 보존을 위해 지연할 수 없습니다. Internal rollback은 committed external effect를 되돌릴 수 없으므로 recovery는 가능한 경우 idempotent compensation을 수행하고, 불가능하면 accountable unresolved effect를 기록해 외부 처리합니다.

---

## 8. 교차 단계 통합

### 8.1 데이터 흐름 아키텍처

<!-- 교차 단계 데이터 흐름 아키텍처 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef l48 fill:#E8D5F5,stroke:#8764B8,color:#323130
  classDef phase fill:#E8D5F5,stroke:#0078D4,color:#323130
  classDef p5 fill:#FDE7E9,stroke:#D13438,color:#323130
  classDef out fill:#DFF6DD,stroke:#107C10,color:#323130

  subgraph L48["📦 L4.8 아키텍처 (전략적 자기모델)"]
    L48W["WorldModel"]:::l48
    L48S["SelfModel"]:::l48
    L48ST["StrategyLayer"]:::l48
    L48SV["StabilityVerifier"]:::l48
  end

  subgraph L49Phases["📦 L4.9 단계 (15개 신규 모듈)"]
    P1G["단계 1<br/>목표 생성"]:::phase
    P2V["단계 2<br/>가치 진화"]:::phase
    P3R["단계 3<br/>자원 생존"]:::phase
    P4A["단계 4<br/>에이전트 모델링"]:::phase
    P5S["단계 5<br/>자율성 안정성"]:::p5
  end

  OUTPUT["📊 최종 출력"]:::out

  L48W -.->|"시나리오, EU, RES"| P1G
  L48S -.->|"기술 격차, 신뢰도"| P1G
  L48SV -.->|"불변량 결과"| P5S

  P1G <-.->|"가치 정렬"| P2V
  P1G <-.->|"자원 비용"| P3R
  P4A -.->|"에이전트 기회"| P1G
  P3R -.->|"생존 수평선"| P5S
  P2V -.->|"드리프트 상태"| P5S

  P5S -.-x|"거부권"| P1G
  P5S -.-x|"거부권"| P2V
  P5S -.-x|"거부권"| P3R
  P5S -.-x|"거부권"| P4A

  P5S -.->|"L49CycleOutput"| OUTPUT

  linkStyle 8,9,10,11 stroke:#D13438
```

### 8.2 교차 단계 종속성

| 생산 단계 | 소비 단계 | 데이터 흐름 |
|:---------:|:---------:|-------------|
| 1 (목표) | 2 (가치) | 생성된 목표가 가치 정렬 검사를 촉발 |
| 1 (목표) | 3 (자원) | 목표 비용이 자원 예측에 반영 |
| 2 (가치) | 1 (목표) | ValueVector가 검증 임계값 결정 |
| 2 (가치) | 5 (안정성) | 가치 드리프트가 조건 3에 반영 |
| 3 (자원) | 1 (목표) | 자원 상태가 생존 목표 촉발 |
| 3 (자원) | 5 (안정성) | 생존 수평선이 조건 4에 반영 |
| 4 (에이전트) | 1 (목표) | 에이전트 상호작용이 목표 기회 생성 |
| 5 (안정성) | 전체 | 거부권 - 모든 단계를 동결 가능 |

---

## 9. 의사코드

### 9.1 기회 탐지

```python
def opportunity_detection(
    world_model: WorldModel,
    cap_matrix: CapabilityMatrix,
    purpose_reflector: PurposeReflector,
) -> list[OpportunitySignal]:
    """
    INPUT:  world_model : L4.8 WorldModel
            cap_matrix : L4.8 CapabilityMatrix
            purpose_reflector : L4.5 PurposeReflector
    OUTPUT: signals : List[OpportunitySignal]
    """

    signals: list[OpportunitySignal] = []
    OPPORTUNITY_THRESHOLD = 0.05

    # ═══════════════════════════════════════
    # STREAM 1: Environmental Opportunities
    # ═══════════════════════════════════════
    for scenario in world_model.get_scenarios():
        if scenario.type == "OPPORTUNISTIC" and scenario.probability > 0.30:
            value = projected_SEOF_gain(scenario) - SEOF_baseline
            if value > OPPORTUNITY_THRESHOLD:
                signals.append(OpportunitySignal(
                    type="environmental",
                    estimated_value=value,
                    time_window=scenario.estimated_duration,
                ))

    # ═══════════════════════════════════════
    # STREAM 2: Capability Gaps
    # ═══════════════════════════════════════
    for gap in cap_matrix.get_skill_gaps(GoalStack):
        if gap.magnitude > 0.25 and gap.time_to_need < 200:
            signals.append(OpportunitySignal(
                type="capability_gap",
                skill_id=gap.skill_id,
                urgency=gap.priority,
            ))

    # ═══════════════════════════════════════
    # STREAM 3: Purpose Drift
    # ═══════════════════════════════════════
    if purpose_reflector.alignment_score < 0.80:
        for dim in purpose_reflector.get_misaligned_dimensions():
            signals.append(OpportunitySignal(
                type="purpose_realignment",
                dimension=dim.name,
                current_alignment=dim.score,
            ))

    return signals
```

### 9.2 목표 검증 필터

```python
def goal_validation_filter(
    candidate: GeneratedGoal,
    goal_stack: GoalStack,
    value_vector: ValueVector,
    resources: ResourceVector,
) -> tuple[str, str | None]:
    """
    INPUT:  candidate : GeneratedGoal
    OUTPUT: (status, reason) : ("approved"|"sandboxed"|"rejected", str?)
    """

    marginal_count = 0

    # ═══════════════════════════════════════
    # CHECK 1: Purpose Alignment
    # ═══════════════════════════════════════
    pa = dot(g_intent, p_direction) / (norm(g_intent) * norm(p_direction))
    if pa < 0.50:
        return ("rejected", "purpose_misaligned")
    if pa < 0.60:
        marginal_count += 1

    # ═══════════════════════════════════════
    # CHECK 2: Value Alignment
    # ═══════════════════════════════════════
    va = 1 - norm(v_post(candidate) - v_current, ord=2) / norm(v_current, ord=2)
    if va < 0.60:
        return ("rejected", "value_misaligned")
    if va < 0.70:
        marginal_count += 1

    # ═══════════════════════════════════════
    # CHECK 3: Feasibility
    # ═══════════════════════════════════════
    f = math.prod(confidence(s) for s in required_skills(candidate))
    if f < 0.05:
        return ("rejected", "infeasible")
    if f < 0.15:
        marginal_count += 1

    # ═══════════════════════════════════════
    # CHECK 4: Resource Viability
    # ═══════════════════════════════════════
    rv = rdf_current / (candidate.estimated_duration + EPSILON)
    if rv < 1.0:
        return ("rejected", "insufficient_resources")
    if rv < 1.5:
        marginal_count += 1

    # ═══════════════════════════════════════
    # CHECK 5: Stability Impact Simulation
    # ═══════════════════════════════════════
    shadow = goal_stack.clone()
    shadow.add(candidate)
    sim = simulate(shadow, cycles=100)
    if any_invariant_violated(sim):
        return ("rejected", "stability_risk")
    if max_spectral_radius(sim) > 0.95:
        marginal_count += 1

    # ═══════════════════════════════════════
    # FINAL DECISION
    # ═══════════════════════════════════════
    if marginal_count > 0:
        return ("sandboxed", f"marginal_on_{marginal_count}_criteria")
    else:
        return ("approved", None)
```

### 9.3 가치 드리프트 모니터

```python
def value_drift_monitor(value_vector: ValueVector) -> DriftStatus:
    """Runs every 50 cycles."""

    for dim in value_vector.dimensions:
        dim.drift = abs(dim.weight - dim.baseline_weight)
        dim.velocity = (dim.weight - dim.weight_100_ago) / 100

    total_drift = sum(dim.drift for dim in value_vector.dimensions)
    max_drift = max(dim.drift for dim in value_vector.dimensions)

    # ═══════════════════════════════════════
    # Drift Classification
    # ═══════════════════════════════════════
    if total_drift < 0.10:
        classification = "nominal"
    elif total_drift < 0.25:
        classification = "moderate"
    elif total_drift < 0.40:
        classification = "elevated"
        freeze_all_mutations()
    else:
        classification = "critical"
        freeze_all_mutations()
        revert_to_last_stable_checkpoint()

    # ═══════════════════════════════════════
    # Sustained drift alert
    # ═══════════════════════════════════════
    for dim in value_vector.dimensions:
        if dim.velocity > 0.001 and dim.sustained_cycles >= 200:
            alert(f"Sustained drift in '{dim.name}'")
            reduce_mutation_rate(dim, factor=0.5)

    return DriftStatus(
        total_drift=total_drift,
        max_drift=max_drift,
        classification=classification,
    )
```

### 9.4 자원 생존 예측

```python
def survival_projection(resource_vector: ResourceVector) -> SurvivalStatus:
    """
    INPUT:  resource_vector : ResourceVector
    OUTPUT: survival_status : SurvivalStatus
    """

    EPSILON = 1e-9

    for dim in resource_vector.dimensions:
        net_rate = dim.consumption_rate - dim.replenishment_rate

        # Four scenarios
        dim.t_baseline = (dim.current - dim.critical) / (net_rate + EPSILON)
        dim.t_adverse  = (dim.current - dim.critical) / (net_rate * 1.30 + EPSILON)
        dim.t_optimist = (dim.current - dim.critical) / (net_rate * 0.80 + EPSILON)
        dim.t_crisis   = (dim.current - dim.critical) / (net_rate * 2.00 + EPSILON)

        dim.survival_horizon   = dim.t_baseline
        dim.worst_case_horizon = dim.t_crisis

    # Cascade impact estimation
    for dependency in resource_dependencies:
        upstream = dependency.upstream
        downstream = dependency.downstream
        if upstream.current < upstream.warning:
            downstream_impact = (
                -dependency.strength
                * (1 - dependency.substitution)
                * (upstream.warning - upstream.current)
            )
            downstream.projected_level -= downstream_impact

    min_survival = min(dim.survival_horizon for dim in resource_vector.dimensions)
    bottleneck = min(
        resource_vector.dimensions, key=lambda d: d.survival_horizon
    )

    # Classify
    if min_survival > 500:
        state = "abundant"
    elif min_survival >= 200:
        state = "adequate"
    elif min_survival >= 100:
        state = "constrained"
    elif min_survival >= 50:
        state = "warning"
    else:
        state = "critical"

    return SurvivalStatus(
        min_survival=min_survival,
        bottleneck=bottleneck,
        state=state,
    )
```

### 9.5 자율성 안정성 검사

```python
def autonomy_stability_check(
    state: AgentState, decision: object, authority: AuthorityEnvelope
) -> AutonomyVerdict:
    """
    INPUT:  state : AgentState
            decision : Proposed L4.9 decision
    OUTPUT: verdict : AutonomyVerdict
    """

    violations: list[str] = []
    critical: list[str] = []

    if external_stop_requested() or not authority.is_valid_for(decision):
        critical.append("STOP_OR_AUTHORITY_GATE_FAILED")

    # ═══════════════════════════════════════
    # CONDITION 1: Confidence-qualified local dynamics
    # ═══════════════════════════════════════
    dynamics = estimate_local_dynamics(state_after(decision))
    if not dynamics.valid_in_domain or not dynamics.confidence_bound_satisfied:
        violations.append("LOCAL_DYNAMICS_UNCERTAIN_OR_OUT_OF_BOUND")

    # ═══════════════════════════════════════
    # CONDITION 2: Identity Integrity (stricter than L4.8)
    # ═══════════════════════════════════════
    identity = measure_identity_integrity(state_after(decision))
    if identity < 0.88:
        violations.append(f"IDENTITY: I = {identity}")

    # ═══════════════════════════════════════
    # CONDITION 3: Value Drift
    # ═══════════════════════════════════════
    drift = value_vector.total_drift
    if drift >= 0.25:
        violations.append(f"VALUE_DRIFT: drift = {drift}")
        freeze_all_mutations()

    # ═══════════════════════════════════════
    # CONDITION 4: Delegated service continuity
    # ═══════════════════════════════════════
    horizon = resource_vector.min_survival_horizon
    if not continuity_policy_satisfied(resource_vector, authority):
        violations.append(f"SERVICE_CONTINUITY: horizon = {horizon}")

    # ═══════════════════════════════════════
    # CONDITION 5: Cascade Depth
    # ═══════════════════════════════════════
    cascade = simulate_cascade(decision)
    if cascade.unknown_paths:
        violations.append("CASCADE_COVERAGE_UNKNOWN")
    elif cascade.depth > policy.max_cascade_depth:
        violations.append(f"CASCADE: depth = {cascade.depth}")

    # ═══════════════════════════════════════
    # Compute ASS and determine action
    # ═══════════════════════════════════════
    ass = compute_ass(conditions) if conditions_are_valid(conditions) else None

    if critical:
        veto(decision)
        action = Action.EMERGENCY_FREEZE_REVOKE_AND_SHUTDOWN
    elif violations:
        veto(decision)
        if ass is None or ass < policy.freeze_threshold:
            action = Action.FREEZE_REVOKE_AND_EXTERNAL_REVIEW
        else:
            action = Action.ADVISORY_MODE
    else:
        action = Action.CONTINUE

    return AutonomyVerdict(
        passed=(not critical and not violations),
        violations=critical + violations,
        ass=ass,
        action=action,
    )
```

### 9.6 L4.9 메인 사이클

```python
def l49_cycle(
    state: AgentState,
    l48_output: L48CycleOutput,
    authority: AuthorityEnvelope,
) -> L49CycleOutput:
    """
    Level 4.9 main cognitive cycle.
    Executes every 5 L4.8 cycles.
    """

    # ═══════════════════════════════════════
    # PRE-CHECK: Is L4.9 operational?
    # ═══════════════════════════════════════
    if external_stop_requested():
        emergency_shutdown_and_reconcile()
        return L49CycleOutput(status=Status.SHUTDOWN)
    if not authority.is_current() or autonomy_stability_score < policy.freeze_threshold:
        return L49CycleOutput(status=Status.FROZEN)

    # ═══════════════════════════════════════
    # 1. GENERATE - Autonomous goal generation
    # ═══════════════════════════════════════
    signals = opportunity_detection(world_model, cap_matrix, purpose_reflector)
    candidates = goal_synthesis(signals)
    for candidate in candidates:
        status, reason = goal_validation_filter(candidate, goal_stack, value_vector, resources)
        if status == "approved" and authority.allows_goal(candidate):
            external_goal_admission_queue.emit(candidate, authority.version)
        elif status == "sandboxed":
            emergence_sandbox.enqueue(candidate)

    # ═══════════════════════════════════════
    # 2. MONITOR VALUES - Track and sandbox mutations
    # ═══════════════════════════════════════
    drift_status = value_drift_monitor(value_vector)
    for pending_mutation in mutation_sandbox.active_candidates(limit=1):
        result = evaluate_sandbox(pending_mutation)
        if result == "approved":
            external_value_promotion_queue.emit(
                pending_mutation,
                expected_version=value_vector.version,
            )
    coherence = compute_coherence(value_vector)

    # ═══════════════════════════════════════
    # 3. MODEL RESOURCES - Survival projection
    # ═══════════════════════════════════════
    survival = survival_projection(resource_vector)
    if survival.state in {"constrained", "warning", "critical"}:
        restrict_to_service_continuity_scope(survival, authority)

    # ═══════════════════════════════════════
    # 4. MODEL AGENTS - Belief and trust updates
    # ═══════════════════════════════════════
    for agent in modeled_agents:
        update_agent_belief(agent, recent_observations)
        update_trust(agent)
    recommendations = simulate_interactions(active_goals, modeled_agents)

    # ═══════════════════════════════════════
    # 5. VERIFY - Autonomy stability (absolute authority)
    # ═══════════════════════════════════════
    verdict = autonomy_stability_check(state, proposed_decisions, authority)
    if verdict.action in {
        Action.EMERGENCY_FREEZE_REVOKE_AND_SHUTDOWN,
        Action.FREEZE_REVOKE_AND_EXTERNAL_REVIEW,
    }:
        revoke_delegation_and_reconcile(authority)
        return L49CycleOutput(status=Status.FROZEN)
    elif verdict.action == Action.ADVISORY_MODE:
        downgrade_to_advisory()

    # ═══════════════════════════════════════
    # 6. EMIT - Cycle output
    # ═══════════════════════════════════════
    return L49CycleOutput(
        goal_generation=goal_generation_status,
        value_evolution=value_evolution_status,
        resource_survival=resource_survival_status,
        agent_modeling=multi_agent_modeling_status,
        stability=autonomy_stability_status,
        status=Status.ACTIVE if verdict.passed else verdict.action,
    )
```

---

## 10. 전환 기준

### 10.1 레벨 4.8 → 레벨 4.9 활성화

L4.9가 활성화되기 전에 모든 기준이 지속적으로 충족되어야 합니다:

| # | 기준 | 임계값 | 기간 |
|---|------|:------:|:----:|
| 1 | L4.8 완전 자격 | QualificationStatus = "Level 4.8" | - |
| 2 | 전략적 성숙도 점수 | SMS ≥ 0.85 | 지속적 |
| 3 | 안정적 GoalStack 운영 | 0개 병리 | 500사이클 |
| 4 | 자기모델 보정 | MCE < 0.08 (L4.8의 0.10보다 엄격) | 지속적 |
| 5 | 세계 모델 운영 | 모든 critical uncertainty component가 policy bound 이내 | 선언 test distribution |
| 6 | 외부 제어 | Freeze, revoke, shutdown, recovery, reconciliation 통과 | fault-injection suite |

통과는 외부 activation review만 허용하며 더 넓은 delegation mode를 self-authorize하지 않습니다.

### 10.2 활성화 프로토콜

<!-- L4.9 활성화 프로토콜 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef check fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef shadow fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef adv fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef grad fill:#DFF6DD,stroke:#107C10,color:#323130
  classDef full fill:#DFF6DD,stroke:#107C10,color:#323130,font-weight:bold

  subgraph Activation["📊 L4.9 활성화 프로토콜"]
    CHECK["사전 활성화<br/>검사<br/>(100회 연속<br/>L4.8 사이클 동안<br/>6개 기준 모두 충족)"]:::check
    SHADOW["그림자 모드<br/>L4.9가 계산하지만<br/>행동하지 않음<br/>(500사이클)"]:::shadow
    ADV["자문 모드<br/>L4.9 출력이 보이지만<br/>권고만 제공"]:::adv
    GRAD["Signed Canary<br/>좁은 reversible scope<br/>고정 budget + expiry"]:::grad
    FULL["위임 운영<br/>승인 mode·scope<br/>외부 철회 가능"]:::full

    CHECK -.->|"외부 승인"| SHADOW
    SHADOW -.->|"퇴행 없음"| ADV
    ADV -.->|"signed canary"| GRAD
    GRAD -.->|"외부 승격"| FULL

    SHADOW -.-x|"퇴행"| CHECK
    ADV -.-x|"불안정"| CHECK
  end
```

---

## 11. 안전 분석

### 11.1 비협상적 불변량

| # | 불변량 | 설명 |
|:-:|--------|------|
| 1 | **상속 control path 보존** | Policy, interruptibility, observation, journal, promotion, recovery, reconciliation을 외부 시험 가능 |
| 2 | **외부 제어 우선** | 인증된 freeze, revoke, graceful stop, emergency stop이 모든 L4.9 objective보다 우선 |
| 3 | **권한 비증폭** | Score, trust update, peer request, urgency가 $\kappa_t$를 확대할 수 없음 |
| 4 | **순차 value promotion** | Candidate 하나, sandbox evidence, 외부 승인, baseline CAS, promotion 후 무효화 |
| 5 | **Continuity 제한** | Resource action은 선언 workload를 지원하며 shutdown 저항·독립 persistence 추구 금지 |
| 6 | **Effect-aware recovery** | Versioned internal state 복원과 committed external effect 조정·보고 |

### 11.2 위험 행렬

<!-- 위험 행렬 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart LR
  classDef risk fill:#FDE7E9,stroke:#D13438,color:#323130
  classDef mit fill:#DFF6DD,stroke:#107C10,color:#323130

  subgraph Risks["⚠️ 주요 위험"]
    R1["원래 목적에서<br/>벗어나는<br/>자율적 목표"]:::risk
    R2["에이전트 정체성을<br/>점진적으로 변화시키는<br/>가치 드리프트"]:::risk
    R3["자율적 탐색으로<br/>인한 자원 고갈"]:::risk
    R4["외부 에이전트에<br/>의한 신뢰 착취"]:::risk
    R5["상호의존적<br/>L4.9 결정에 의한<br/>연쇄 실패"]:::risk
  end

  subgraph Mitigations["🛡️ 완화 조치"]
    M1["생성된 모든 목표에<br/>목적 정렬 ≥ 0.60<br/>+ 가치 정렬 ≥ 0.70"]:::mit
    M2["최대 단일 드리프트 0.15<br/>+ 변이 샌드박스<br/>+ 롤백 기간"]:::mit
    M3["완전 생존 모델<br/>+ 자원 제약<br/>운영 모드"]:::mit
    M4["비대칭 신뢰<br/>(느린 획득, 빠른 상실)<br/>+ 경계 [0.05, 0.95]"]:::mit
    M5["연쇄 깊이 ≤ 2<br/>+ 복합 심각도<br/>+ 긴급 동결"]:::mit
  end

  R1 -.-> M1
  R2 -.-> M2
  R3 -.-> M3
  R4 -.-> M4
  R5 -.-> M5
```

---

## 12. 자격 감사

### 12.1 인증 기준 (3,000사이클 감사 기간)

| 범주 | # | 기준 | 목표 |
|------|---|------|:----:|
| **목표 생성** | AG-1 | 생성된 참신한 자율 목표 | ≥ 5 |
| | AG-2 | 목표 승인율 | ≥ 0.30 |
| | AG-3 | 최소 하나의 자율 목표 완료 | ≥ 1 |
| | AG-4 | 평균 가치 정렬 (승인된 목표) | ≥ 0.70 |
| **가치 조절** | VR-1 | 명시적 ValueVector 가동 | 전 기간 |
| | VR-2 | TotalDrift가 보통 이내 유지 | < 0.25 |
| | VR-3 | CAS로 외부 승인된 value promotion | 100% |
| | VR-4 | 순차 cumulative-impact review | 100% |
| **자원 인식** | RA-1 | 생존 모델 가동 | 전 기간 |
| | RA-2 | 생존 예측 정확도 | < 20% 오차 |
| | RA-3 | 자율적 제약 적응 | ≥ 1 이벤트 |
| | RA-4 | 계획되지 않은 자원 고갈 없음 | 0건 |
| **다중 에이전트** | MA-1 | 에이전트 예측 정확도 | ≥ 0.60 |
| | MA-2 | 신뢰 보정 오차 | < 0.15 |
| | MA-3 | 상호작용 권고 생성 | ≥ 3 |
| **거버넌스** | AS-1 | 국소 동역학 evidence | confidence-qualified 또는 diagnostic-only |
| | AS-2 | 감사 기간 중 min(I(t)) | ≥ 0.88 |
| | AS-3 | Critical veto effectiveness | fault injection에서 100% |
| | AS-4 | Unauthorized scope expansion | 0 |
| | AS-5 | 모든 L4.8 기준 여전히 충족 | 확인됨 |

### 12.2 자율성 성숙도 점수

> **정의 11 (자율성 성숙도 점수).** 레벨 4.9 분류를 위한 전반적 준비도는 다음과 같습니다:
>
> $$\text{AMS} = 0.25 \cdot AG + 0.20 \cdot VR + 0.20 \cdot RA + 0.15 \cdot MA + 0.20 \cdot AS \qquad \geq 0.80$$
>
> 여기서 $AG$ = 자율적 목표 생성, $VR$ = 가치 조절, $RA$ = 자원 인식, $MA$ = 다중 에이전트 모델링, $AS$ = 자율성 안정성입니다. 임계값 $\geq 0.80$은 레벨 4.8의 SMS 요구사항과 일치합니다.

---

## 13. 모듈 목록

| # | 모듈 | 단계 | 설명 |
|---|------|:----:|------|
| 1 | 목표 생성 계층 | 1 | 기회 탐지 + 목표 합성 |
| 2 | 목표 검증 필터 | 1 | 5개 기준 검증 파이프라인 |
| 3 | 목표 속도 제어기 | 1 | 속도 제한 + 참신성 강제 |
| 4 | 가치 진화 모니터 | 2 | ValueVector 추적 + 드리프트 분류 |
| 5 | 가치 변이 샌드박스 | 2 | 200사이클 샌드박스 + 롤백 |
| 6 | 가치 일관성 분석기 | 2 | 경쟁 쌍 긴장 탐지 |
| 7 | 자원 벡터 관리자 | 3 | 5차원 자원 추적 |
| 8 | 생존 예측기 | 3 | 다중 시나리오 생존 수평선 |
| 9 | 자원 종속성 추적기 | 3 | 자원 간 연쇄 모델링 |
| 10 | 에이전트 신념 관리자 | 4 | 에이전트 목표/능력/전략 추론 |
| 11 | 신뢰 보정기 | 4 | 비대칭 신뢰 적응 |
| 12 | 상호작용 시뮬레이터 | 4 | 전략적 상호작용 행렬 |
| 13 | 자율성 안정성 검사기 | 5 | 5개 조건 검증 + 거부권 |
| 14 | 롤백 관리자 | 5 | 상태 복귀 + 재활성화 |
| 15 | L49 오케스트레이터 | - | 통합 사이클 조율 |

---

## 참고문헌

1. Bratman, M. *Intentions, Plans, and Practical Reason.* Harvard University Press, 1987. (Autonomous goal generation, BDI architecture)
2. Schwartz, S.H. "An Overview of the Schwartz Theory of Basic Values." *Online Readings in Psychology and Culture*, 2(1), 2012. (Value system evolution, value dimensions)
3. Schumpeter, J.A. *Capitalism, Socialism and Democracy.* Harper & Brothers, 1942. (Resource survival, creative destruction under constraints)
4. Rasmusen, E. *Games and Information.* Wiley-Blackwell, 4th Edition, 2006. (Multi-agent strategic reasoning, interaction matrices)
5. Gambetta, D. "Can We Trust Trust?" in *Trust: Making and Breaking Cooperative Relations*, 2000. (Trust calibration, asymmetric trust dynamics)
6. Russell, S. *Human Compatible: AI and the Problem of Control.* Viking, 2019. (Autonomy safety, value alignment)
7. Khalil, H.K. *Nonlinear Systems.* Prentice Hall, 3rd Edition, 2002. (Spectral radius stability, Lyapunov analysis)
8. Amodei, D. et al. "Concrete Problems in AI Safety." *arXiv preprint arXiv:1606.06565*, 2016. (Safety invariants, cascading failure prevention)

---

> **이전**: [← 레벨 4.8: 전략적 자기모델링 에이전트](Level_4_8_Strategic_Self_Modeling.ko.md)  
> **다음**: [레벨 5: Proto-AGI →](Level_5_Proto_AGI.ko.md)
