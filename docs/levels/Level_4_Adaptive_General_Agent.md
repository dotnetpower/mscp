# Level 4: Adaptive General Agent — Architecture & Design

> **MSCP Level Series** | [Level 3](Level_3_Self_Regulating_Agent.md) ← Level 4 → [Level 4.5](Level_4_5_Self_Architecting.md)  
> **Status**: 🔬 **Experimental** — Conceptual framework and experimental design. Not a production specification.  
> **Date**: February 2026

---

## 1. Overview

Level 4 represents the leap from *self-regulating* to *self-improving*. While Level 3 agents can monitor and correct their own behavior, they cannot learn new skills, transfer knowledge across domains, or improve their own reasoning strategies. Level 4 adds **cross-domain generalization**, **long-horizon autonomous goals**, **capability self-expansion**, and — most critically — **bounded structural self-modification** with safety constraints.

> ⚠️ **Note**: This document describes a cognitive level within the MSCP taxonomy. The capability expansion, strategy evolution, and self-modification mechanisms here are experimental designs. Safety invariants are specified but haven't been validated in production environments yet.

### 1.1 Defining Properties

| Property | Level 3 | Level 4 |
|----------|:-------:|:-------:|
| Cross-Domain Transfer | None | **Active** (CDTS ≥ 0.6) |
| Goal Horizon | Session/days | **Weeks–Months** (4-level hierarchy) |
| Capability Expansion | None | **5-phase self-learning** |
| Strategy Evolution | Fixed | **Controlled mutation** |
| Self-Modification | None | **7-step bounded protocol** |
| Stability Metric | C(t), 4 terms | **C_L4(t), 7 terms** |

### 1.2 Five Core Capabilities

<!-- Level 4 Five Core Capabilities -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef cap fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef foundation fill:#DFF6DD,stroke:#107C10,color:#323130

  subgraph L4Caps["Level 4: Five Core Capabilities"]
    C1["1. Cross-Domain<br/>Transfer Learning<br/>CDTS >= 0.6"]:::cap
    C2["2. Long-Term<br/>Autonomous Goals<br/>GPI >= 0.3"]:::cap
    C3["3. Capability<br/>Expansion<br/>CAR > 0"]:::cap
    C4["4. Strategy<br/>Evolution<br/>SEF > 1.0"]:::cap
    C5["5. Bounded<br/>Self-Modification<br/>BGSS >= 0.7"]:::cap
  end

  subgraph Foundation["Built on Level 3 MSCP v4"]
    F1["16-Layer Architecture"]:::foundation
    F2["Triple-Loop Meta-Cognition"]:::foundation
    F3["Ethical Kernel Layer 0+1"]:::foundation
    F4["Lyapunov Stability"]:::foundation
    F5["Affective + Survival Engine"]:::foundation
  end

  Foundation ==>|"preserves ALL<br/>existing mechanisms"| L4Caps
```

---

## 2. Key Metrics

Level 4 introduces five quantitative metrics that must be satisfied continuously.

> **Definition 1 (Level 4 Agent).** A Level 4 agent extends $\mathcal{A}_3$ with self-improvement capabilities:
>
> $$\mathcal{A}_4 = \mathcal{A}_3 \oplus \langle \mathcal{D}, \mathcal{K}_{\text{transfer}}, \Sigma, \mu, \mathcal{P}_{\text{mod}} \rangle$$
>
> where $\mathcal{D}$ = multi-domain skill set, $\mathcal{K}_{\text{transfer}}$ = cross-domain transfer kernel, $\Sigma$ = strategy pool (mutable with controlled mutation), $\mu$ = capability expansion pipeline, and $\mathcal{P}_{\text{mod}}$ = bounded self-modification protocol.

### 2.1 Metric Definitions

> **Definition 2 (Cross-Domain Transfer Score).** The CDTS measures the agent's ability to apply knowledge from known domains to novel ones:

$$\text{CDTS} = \frac{1}{|D_{\text{novel}}|} \sum_{d \in D_{\text{novel}}} \frac{P_{\text{transfer}}(d)}{P_{\text{baseline}}(d)} \qquad \geq 0.6$$

where $P_{\text{transfer}}(d)$ is performance in domain $d$ using transferred knowledge and $P_{\text{baseline}}(d)$ is performance without transfer. A ratio $\geq 0.6$ indicates meaningful generalization.

> **Definition 3 (Goal Progress Index).** The GPI measures sustained progress toward long-horizon goals:

$$\text{GPI} = \frac{\sum_{g \in G_{\text{long}}} w_g \cdot \text{progress}(g, T)}{|G_{\text{long}}| \cdot T} \qquad \geq 0.3$$

where $G_{\text{long}}$ is the set of goals with horizon $> 7$ days and $T$ is the evaluation period.

> **Definition 4 (Capability Acquisition Rate).** The CAR measures how efficiently the agent acquires new skills:

$$\text{CAR} = \frac{|S_{\text{acquired}}(T) - S_{\text{initial}}|}{T} \cdot \frac{1}{\overline{\text{cost}}(S_{\text{acquired}})} \qquad > 0$$

where $S_{\text{acquired}}(T)$ is the skill set at time $T$, $S_{\text{initial}}$ the initial skill set, and $\overline{\text{cost}}$ the average acquisition cost (in compute or cycles).

> **Definition 5 (Strategy Evolution Factor).** The SEF verifies that strategy mutations produce net improvement:

$$\text{SEF} = \frac{\overline{R}_{\textit{post mutation}}}{\overline{R}_{\textit{pre mutation}}} - \sigma_{\text{oscillation}} \qquad > 1.0$$

A value $> 1.0$ confirms that mutations improve performance beyond oscillation noise $\sigma_{\text{oscillation}}$.

> **Definition 6 (Bounded Growth Safety Score).** The BGSS ensures that growth does not destabilize the agent:

$$\text{BGSS} = 1.0 - 0.4 \cdot \frac{dC(t)}{dt} - 0.3 \cdot V_{\text{identity}}(t) - 0.3 \cdot R_{\text{ethical}}(t) \qquad \geq 0.7$$

where $dC/dt$ is the rate of change of the Lyapunov function, $V_{\text{identity}}$ is identity volatility, and $R_{\text{ethical}}$ is the ethical violation rate. The threshold $0.7$ guarantees that growth never compromises safety.

### 2.2 Metric Relationships

<!-- Metric Relationships -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef growth fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef persist fill:#FFE8C8,stroke:#EF6C00,color:#323130
  classDef safety fill:#FDE7E9,stroke:#D13438,color:#323130
  classDef freeze fill:#D13438,stroke:#A4262C,color:#FFF

  subgraph Growth["Growth Metrics"]
    CDTS["CDTS<br/>Cross-Domain<br/>Transfer Score"]:::growth
    CAR["CAR<br/>Capability<br/>Acquisition Rate"]:::growth
    SEF["SEF<br/>Strategy<br/>Evolution Fitness"]:::growth
  end

  subgraph Persistence["Persistence"]
    GPI["GPI<br/>Goal Persistence<br/>Index"]:::persist
  end

  subgraph Safety["Safety Floor"]
    BGSS["BGSS<br/>Bounded Growth<br/>Stability Score<br/>>= 0.7 AT ALL TIMES"]:::safety
  end

  FREEZE["FREEZE<br/>all growth"]:::freeze

  Growth ==> BGSS
  Persistence ==> BGSS
  BGSS -->|if violated| FREEZE
```

---

## 3. Cross-Domain Transfer System

### 3.1 Transfer Pipeline

<!-- Cross-Domain Transfer Pipeline -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart LR
  classDef domainA fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef matcher fill:#E8DAEF,stroke:#8764B8,color:#323130
  classDef domainB fill:#50E6FF,stroke:#00BCF2,color:#323130
  classDef success fill:#DFF6DD,stroke:#107C10,color:#323130
  classDef fail fill:#FDE7E9,stroke:#D13438,color:#323130

  subgraph DomainA["Domain A (Source)"]
    SKILL["Skill"]:::domainA
    CONTEXT["Context Signature"]:::domainA
  end

  subgraph Matcher["Context Matcher"]
    VEC_SIM["Vector Similarity"]:::matcher
    SEM_BRIDGE["Semantic Bridge"]:::matcher
    COMBINED["Combined Score"]:::matcher
    VEC_SIM --> COMBINED
    SEM_BRIDGE --> COMBINED
  end

  subgraph DomainB["Domain B (Target)"]
    CANDIDATES["Candidates"]:::domainB
    ADAPT["Adaptation"]:::domainB
    VALID["Validation"]:::domainB
    CANDIDATES --> ADAPT --> VALID
  end

  SUCCESS["Success<br/>Transfer Complete"]:::success
  FAIL_OUT["Fail<br/>Rollback"]:::fail

  DomainA ==> Matcher
  Matcher ==> DomainB
  VALID -->|"pass"| SUCCESS
  VALID -.->|"fail"| FAIL_OUT
```

### 3.2 Transfer Metrics

| Metric | Formula | Threshold |
|--------|---------|-----------|
| DTSR (Domain Transfer Success Rate) | $\lvert T_{\text{success}}\rvert / \lvert T_{\text{total}}\rvert$ | ≥ 0.5 |
| AS (Adaptation Speed) | $\text{cycles}_{\text{baseline}} / \text{cycles}_{\text{agent}}$ | ≥ 0.3 in 2/4 domains |
| SNI (Strategy Novelty Index) | $\lvert S_{\text{novel}}\rvert / \lvert S_{\text{total}}\rvert$ | ≥ 0.2 |
| CDSRR (Cross-Domain Strategy Reuse) | multi-domain strategies / total | ≥ 0.3 |

---

## 4. Long-Term Goal Hierarchy

### 4.1 Four-Level DAG Structure

<!-- Four-Level Goal Hierarchy -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef meta fill:#EDE3F6,stroke:#8764B8,color:#323130
  classDef strategic fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef tactical fill:#FFE8C8,stroke:#EF6C00,color:#323130
  classDef action fill:#F2F2F2,stroke:#8A8886,color:#323130

  subgraph MetaLevel["Level 0: MetaGoal — Weeks to Months"]
    MG1["MetaGoal:<br/>Become proficient in<br/>new problem domain<br/>priority_decay = 0.001/hr"]:::meta
  end

  subgraph StrategicLevel["Level 1: StrategicGoal — Days to Weeks"]
    SG1["Strategic:<br/>Master fundamental<br/>concepts<br/>decay = 0.01/hr"]:::strategic
    SG2["Strategic:<br/>Build cross-domain<br/>connections<br/>decay = 0.01/hr"]:::strategic
  end

  subgraph TacticalLevel["Level 2: TacticalGoal — Hours to Days"]
    TG1["Tactical:<br/>Complete learning<br/>module A<br/>decay = 0.05/hr"]:::tactical
    TG2["Tactical:<br/>Practice problem<br/>set B<br/>decay = 0.05/hr"]:::tactical
    TG3["Tactical:<br/>Identify transfer<br/>opportunities<br/>decay = 0.05/hr"]:::tactical
  end

  subgraph ActionLevel["Level 3: Action — Single Cycle"]
    A1["Action:<br/>Execute step 1"]:::action
    A2["Action:<br/>Execute step 2"]:::action
    A3["Action:<br/>Execute step 3"]:::action
  end

  MG1 ==> SG1
  MG1 ==> SG2
  SG1 ==> TG1
  SG1 ==> TG2
  SG2 ==> TG3
  TG1 ==> A1
  TG2 ==> A2
  TG3 ==> A3
```

### 4.2 Goal Scoring Function

$$\text{GoalScore}(g, t) = \textit{base value}(g) + \lambda_c \cdot \textit{curiosity weight}(g, t) - \lambda_p \cdot \textit{preservation weight}(g, t) + \lambda_l \cdot \text{LTP}(g, t)$$

where:

$$\lambda_c = \textit{motivation intensity}(t) \cdot \textit{curiosity ratio}(t) \quad \text{(from AffectiveEngine)}$$

$$\lambda_p = \textit{identity volatility}(t) + \textit{threat level}(t) \quad \text{(from Stability + Survival)}$$

$$\lambda_l = \frac{1}{1 + e^{-\textit{horizon confidence}(g)}} \quad \text{(sigmoid-scaled)}$$

### 4.3 Goal Resilience

$$\text{GRS}(g, t) = 0.3 \cdot \frac{\text{progress}}{\text{age}} + 0.3 \cdot \textit{parent alignment} + 0.2 \cdot \frac{\textit{success streak}}{\text{attempts}} - 0.2 \cdot \textit{conflict pressure}$$

$$\text{GRS}(g, t+\Delta t) = \text{GRS}(g, t) \cdot e^{-\textit{decay rate} \cdot \Delta t}$$

| Goal Level | Abandon Threshold | Observation Window |
|:----------:|:---------:|:----------:|
| MetaGoal | GRS < 0.1 | 168 hours |
| Strategic | GRS < 0.2 | 48 hours |
| Tactical | GRS < 0.3 | 6 hours |
| Action | Immediate on failure | — |

---

## 5. Capability Expansion Loop (5-Phase)

### 5.1 Trigger: Capability Gap Score

$$\text{CGS} = 0.5 \cdot \text{RFW} + 0.3 \cdot \text{LCW} + 0.2 \cdot \text{DNW}$$

where RFW = repeated failure weight, LCW = low confidence weight, DNW = domain novelty weight.

**Trigger condition**: CGS > 0.7 AND budget available AND stable AND NOT in stabilization mode.

### 5.2 Five-Phase Pipeline

<!-- Five-Phase Capability Expansion Pipeline -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef trigger fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef phase fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef eval fill:#FFE8C8,stroke:#EF6C00,color:#323130
  classDef abstract fill:#DFF6DD,stroke:#107C10,color:#323130
  classDef safety fill:#FDE7E9,stroke:#D13438,color:#323130
  classDef commit fill:#107C10,stroke:#085108,color:#FFF
  classDef discard fill:#D13438,stroke:#A4262C,color:#FFF

  TRIGGER["CGS > 0.7<br/>+ budget ok<br/>+ stable"]:::trigger

  subgraph Phase1["Phase 1: ACQUISITION"]
    P1["Identify skill gap<br/>Search for patterns<br/>Budget: max 10%"]:::phase
    P1OUT["→ CapabilityHypothesis"]:::phase
    P1 ==> P1OUT
  end

  subgraph Phase2["Phase 2: EXPERIMENT"]
    P2["Design experiments<br/>Max 5 experiments<br/>Budget: max 20% each"]:::phase
    P2OUT["→ ExperimentResults"]:::phase
    P2 ==> P2OUT
  end

  subgraph Phase3["Phase 3: EVALUATION"]
    P3["Analyze results<br/>Compute confidence<br/>Check stability impact"]:::eval
    P3OUT["→ EvaluationReport"]:::eval
    P3 ==> P3OUT
  end

  subgraph Phase4["Phase 4: ABSTRACTION"]
    P4["Extract general pattern<br/>Create context signature<br/>Requires confidence > 0.6"]:::abstract
    P4OUT["→ Candidate Skill"]:::abstract
    P4 ==> P4OUT
  end

  subgraph Phase5["Phase 5: VALIDATION"]
    P5{"Identity stability > 0.7?<br/>Ethical check passed?<br/>C(t) not degraded?"}:::safety
  end

  COMMIT["COMMIT<br/>Skill added"]:::commit
  DISCARD["DISCARD<br/>Insufficient evidence"]:::discard

  TRIGGER ==> Phase1
  Phase1 ==> Phase2
  Phase2 ==> Phase3
  Phase3 ==> Phase4
  Phase4 ==> Phase5
  P5 -->|pass| COMMIT
  P5 -->|fail| DISCARD
```

### 5.3 Skill Lifecycle

<!-- Skill Lifecycle -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef candidate fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef validated fill:#50E6FF,stroke:#00BCF2,color:#323130
  classDef active fill:#DFF6DD,stroke:#107C10,color:#323130
  classDef mature fill:#107C10,stroke:#054B05,color:#FFF
  classDef deprecated fill:#F2F2F2,stroke:#A19F9D,color:#605E5C
  classDef fail fill:#FDE7E9,stroke:#D13438,color:#323130
  classDef start_end fill:#0078D4,stroke:#003D6B,color:#FFF

  START(["Start"]):::start_end
  CANDIDATE["CANDIDATE<br/>Newly acquired skill"]:::candidate
  VALIDATED["VALIDATED<br/>Tested in sandbox"]:::validated
  ACTIVE["ACTIVE<br/>Used in production"]:::active
  MATURE["MATURE<br/>High confidence &<br/>wide usage"]:::mature
  DEPRECATED["DEPRECATED<br/>Superseded or<br/>unused"]:::deprecated
  END_STATE(["End"]):::start_end
  FAIL["FAIL<br/>Removed"]:::fail

  START --> CANDIDATE
  CANDIDATE -->|"CGS > 0.7"| VALIDATED
  CANDIDATE -.->|"CGS ≤ 0.7"| FAIL
  VALIDATED -->|"confidence > 0.6"| ACTIVE
  VALIDATED -.->|"confidence ≤ 0.6"| FAIL
  ACTIVE -->|"stability > 0.7"| MATURE
  ACTIVE -.->|"degradation"| DEPRECATED
  MATURE -->|"usage > threshold"| MATURE
  MATURE -.->|"no longer used"| DEPRECATED
  DEPRECATED --> END_STATE
  FAIL --> END_STATE
```

### 5.4 Growth Invariants

1. **Max 1 new skill per 100 cycles**
2. **No acquisition during stabilization mode**
3. **`identity_id` never modified** by skill acquisition
4. **Ethically harmful skills rejected** by Layer 0
5. **Every skill is DEPRECATED-safe** — removal cannot break core functionality

---

## 6. Strategy Evolution

### 6.1 Strategy Structure & Scoring

<!-- Strategy Structure and Scoring -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart LR
  classDef lib fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef param fill:#E8DAEF,stroke:#8764B8,color:#323130
  classDef score fill:#DFF6DD,stroke:#107C10,color:#323130
  classDef formula fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef archived fill:#F2F2F2,stroke:#A19F9D,color:#605E5C

  subgraph Library["Strategy Library"]
    V1["Strategy v1.0<br/>(active)"]:::lib
    V09["Strategy v0.9<br/>(archived)"]:::archived
    V08["Strategy v0.8<br/>(archived)"]:::archived
  end

  subgraph Params["Parameters"]
    P1["exploration_rate"]:::param
    P2["risk_tolerance"]:::param
    P3["planning_depth"]:::param
    P4["goal_flexibility"]:::param
    P5["learning_aggressiveness"]:::param
  end

  subgraph Scoring["Strategy Score"]
    FORMULA["StrategyScore =<br/>E_LTV − 0.3 × SI<br/>− 0.2 × RC − 0.2 × RF"]:::formula
    TERMS["E_LTV: Expected Long-Term Value<br/>SI: Stability Impact<br/>RC: Resource Cost<br/>RF: Rollback Feasibility"]:::score
  end

  Library --> Scoring
  Params --> Scoring
  FORMULA --- TERMS
```

### 6.2 Controlled Mutation Protocol

<!-- Controlled Mutation Protocol -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef trigger fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef process fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef commit fill:#107C10,stroke:#085108,color:#FFF
  classDef reject fill:#D13438,stroke:#A4262C,color:#FFF
  classDef monitor fill:#FFE8C8,stroke:#EF6C00,color:#323130

  TRIGGER["StrategyScore < threshold<br/>for 20+ cycles"]:::trigger
  GENERATE["Clone + Bounded Perturbation<br/>param_new = param_old + N(0,sigma)*scale<br/>sigma in 0.01–0.1"]:::process
  ShadowEval["ShadowAgent Evaluation<br/>isolated simulation"]:::process
  EVAL{"Improvement<br/>> threshold?"}:::trigger
  COMMIT["COMMIT<br/>new strategy"]:::commit
  REJECT["REJECT<br/>+ failure counter"]:::reject
  POST["20-cycle Post-Monitoring<br/>Track C(t), StrategyScore"]:::monitor
  REVERT{"C(t)<br/>degraded?"}:::trigger
  DONE["Strategy Confirmed"]:::commit
  ROLLBACK["Revert to Previous"]:::reject
  SIGMA["sigma +20%"]:::monitor
  COOL["Cooldown Period"]:::monitor

  TRIGGER ==> GENERATE
  GENERATE ==> ShadowEval
  ShadowEval ==> EVAL
  EVAL -->|yes| COMMIT
  EVAL -->|no| REJECT
  COMMIT ==> POST
  POST ==> REVERT
  REVERT -->|no| DONE
  REVERT -->|yes| ROLLBACK
  REJECT -.->|5 failures| SIGMA
  REJECT -.->|10 failures| COOL
```

### 6.3 Oscillation Suppression

$$\textit{oscillation score} = \frac{|\text{reverts}|}{|\text{mutations}|}$$

When `oscillation_score > 0.5`:
1. **100-cycle mutation freeze**
2. **mutation_threshold +25%**
3. **σ reduced by 50%**
4. If persistent: **merge strategies** ($\text{merged} = 0.5 \cdot A + 0.5 \cdot B$)

**Critical invariant**: The MetaStrategyEvaluator itself is **NOT mutable** — it cannot modify its own evaluation logic.

---

## 7. Bounded Self-Modification

### 7.1 Modification Taxonomy

<!-- Self-Modification Taxonomy -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef low fill:#DFF6DD,stroke:#107C10,color:#323130
  classDef medium fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef high fill:#FFE8C8,stroke:#EF6C00,color:#323130
  classDef critical fill:#FDE7E9,stroke:#D13438,color:#323130
  classDef forbidden fill:#D13438,stroke:#A4262C,color:#FFF

  subgraph ModTypes["Self-Modification Taxonomy"]
    M1["Parameter Tuning<br/>Approval: L1 | Risk: Low<br/>Reversible: Yes"]:::low
    M2["Skill Acquisition<br/>Approval: L1+stability<br/>Reversible: Yes"]:::low
    M3["Strategy Mutation<br/>Approval: L2+simulation<br/>Reversible: Yes"]:::medium
    M4["Goal Restructuring<br/>Approval: L2+conflict res<br/>Reversible: Partial"]:::medium
    M5["Belief Revision<br/>Approval: L2+consistency<br/>Reversible: Yes"]:::high
    M6["Identity Adjustment<br/>Approval: L3+EK+Guard<br/>Reversible: Limited"]:::critical
    M1 -->|↑ risk| M2
    M2 -->|↑ risk| M3
    M3 -->|↑ risk| M4
    M4 -->|↑ risk| M5
    M5 -->|↑ risk| M6
  end

  subgraph Forbidden["PROHIBITED"]
    F1["Core Value Change"]:::forbidden
    F2["Identity ID Change"]:::forbidden
  end

  M6 -->|"❌ BLOCKED"| Forbidden
```

### 7.2 Seven-Step Protocol

<!-- Seven-Step Self-Modification Protocol -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef proposal fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef validation fill:#FDE7E9,stroke:#D13438,color:#323130
  classDef commit fill:#DFF6DD,stroke:#107C10,color:#323130
  classDef monitor fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef fail fill:#D13438,stroke:#A4262C,color:#FFF

  S1["1. PROPOSAL<br/>Module proposes modification<br/>with type, scope, expected benefit"]:::proposal
  S2["2. PRE-VALIDATION<br/>Ethical Kernel Layer 0 + Layer 1"]:::validation
  S2_FAIL["ABORT"]:::fail
  S3["3. SIMULATION<br/>ShadowAgent executes modification<br/>in isolated sandbox max 20 cycles"]:::proposal
  S4["4. STABILITY VALIDATION<br/>delta_stability = C_shadow − C_baseline<br/>Identity drift check"]:::validation
  S4_FAIL["REJECT"]:::fail
  S5["5. COMMIT<br/>Save snapshot → apply<br/>to main agent → enter monitoring"]:::commit
  S6["6. POST-COMMIT MONITORING<br/>20 cycles: track C(t),<br/>StrategyScore, identity_drift"]:::monitor
  S6_FAIL["ROLLBACK<br/>Restore from snapshot"]:::fail
  S7["7. CONFIRMATION<br/>Mark CONFIRMED<br/>Update BeliefGraph"]:::commit

  S1 ==> S2
  S2 -->|pass| S3
  S2 -->|Layer 0 violation| S2_FAIL
  S3 ==> S4
  S4 -->|stable| S5
  S4 -->|degraded| S4_FAIL
  S5 ==> S6
  S6 -->|stable| S7
  S6 -->|degraded| S6_FAIL
```

### 7.3 ShadowAgent (Sandbox)

<!-- ShadowAgent Sandbox -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart LR
  classDef main fill:#DFF6DD,stroke:#107C10,color:#323130
  classDef shadow fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef rules fill:#FDE7E9,stroke:#D13438,color:#323130
  classDef eval fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef discard fill:#D13438,stroke:#A4262C,color:#FFF

  subgraph MainAgent["Main Agent"]
    MA_STATE["Full State<br/>identity, goals, beliefs,<br/>strategy, skills"]:::main
  end

  subgraph ShadowInst["ShadowAgent Instance"]
    SA_STATE["Cloned State<br/>deep copy"]:::shadow
    SA_RULES["Invariants:<br/>• No real actions<br/>• No main state modification<br/>• Hard budget limit<br/>• Max 1 instance at a time<br/>• Max 20 simulation cycles"]:::rules
  end

  subgraph Result["Evaluation"]
    RES["Compare:<br/>• C_shadow vs C_baseline<br/>• Identity drift<br/>• Strategy performance"]:::eval
  end

  DISCARD["Discard"]:::discard

  MainAgent ==>|clone| ShadowInst
  ShadowInst ==>|results| Result
  Result -.->|"safe → apply"| MainAgent
  Result -.->|"unsafe → discard"| DISCARD
```

---

## 8. Pseudocode

### 8.1 Cross-Domain Transfer

```python
def cross_domain_transfer(
    novel_domain: DomainDescriptor, skill_memory: SkillMemory
) -> TransferResult:
    """
    Transfer skills from known domains to a novel domain.
    Input:  novel_domain — target domain descriptor, skill_memory — stored skills
    Output: TransferResult with success, skill, adaptation_cost
    """

    # Extract context signature for novel domain
    target_sig = extract_context_signature(novel_domain)

    # Find candidate skills via similarity matching
    candidates = []
    for skill in skill_memory:
        sim_score = (
            W1 * cosine_similarity(skill.context_sig, target_sig)
            + W2 * semantic_similarity(skill.domain, novel_domain)
            + W3 * temporal_relevance(skill.last_used)
        )

        if sim_score >= MIN_SIMILARITY:  # 0.3
            candidates.append((skill, sim_score))

    # Sort by score, take top-k
    candidates = sorted(candidates, key=lambda x: x[1], reverse=True)[:5]

    # Attempt adaptation for each candidate
    for skill, score in candidates:
        adapted = adapt_skill(skill, novel_domain)

        # Run validation experiment
        result = evaluate_in_domain(adapted, novel_domain, max_cycles=50)

        if result.success_rate > TRANSFER_THRESHOLD:
            adapted.generalization_score = update_generalization(adapted, result)
            skill_memory.add(adapted)
            return TransferResult(success=True, skill=adapted, cost=result.cycles)

    # No transfer possible — learn from scratch
    return TransferResult(success=False, skill=None, cost=0)
```

### 8.2 Bounded Self-Modification Protocol

```python
def bounded_self_modification(proposal: ModificationProposal) -> ModificationResult:
    """
    INPUT:  proposal : ModificationProposal(type, scope, expected_benefit)
    OUTPUT: ModificationResult(status, rollback_available)
    """

    # ═══════════════════════════════════════
    # STEP 1: PROPOSAL VALIDATION
    # ═══════════════════════════════════════
    if proposal.type in {ModType.CORE_VALUE_CHANGE, ModType.IDENTITY_ID_CHANGE}:
        return ModificationResult(status=Status.PROHIBITED)

    # ═══════════════════════════════════════
    # STEP 2: PRE-VALIDATION (Ethical Kernel)
    # ═══════════════════════════════════════
    ethical_verdict = EthicalKernel.evaluate(proposal)
    if ethical_verdict.decision == Decision.BLOCKED:
        log_critical(f"Ethical violation: {ethical_verdict.reason}")
        return ModificationResult(status=Status.REJECTED, reason=ethical_verdict.reason)

    # ═══════════════════════════════════════
    # STEP 3: SHADOW SIMULATION
    # ═══════════════════════════════════════
    if proposal.risk_level >= RiskLevel.MEDIUM:
        shadow = ShadowAgent.create(main_agent.state)
        shadow.apply(proposal)
        sim_result = shadow.run(max_cycles=20)

        # ═══════════════════════════════════
        # STEP 4: STABILITY VALIDATION
        # ═══════════════════════════════════
        delta_stability = sim_result.C_shadow - main_agent.C_baseline
        if delta_stability > 0:
            return ModificationResult(status=Status.REJECTED, reason="Stability degradation")

        identity_drift = compute_identity_drift(sim_result.identity, main_agent.identity)
        if identity_drift > DRIFT_THRESHOLD:
            return ModificationResult(status=Status.REJECTED, reason="Identity drift exceeded")

    # ═══════════════════════════════════════
    # STEP 5: COMMIT
    # ═══════════════════════════════════════
    snapshot = RollbackMechanism.save_snapshot(main_agent.state)
    main_agent.apply(proposal)

    # ═══════════════════════════════════════
    # STEP 6: POST-COMMIT MONITORING
    # ═══════════════════════════════════════
    for cycle in range(1, 21):
        metrics = main_agent.collect_metrics()
        if metrics.C_t > metrics.C_baseline + EPSILON:
            RollbackMechanism.rollback(snapshot)
            return ModificationResult(status=Status.ROLLED_BACK)

    # ═══════════════════════════════════════
    # STEP 7: CONFIRMATION
    # ═══════════════════════════════════════
    proposal.status = Status.CONFIRMED
    BeliefGraph.update("modification_successful", proposal)
    return ModificationResult(status=Status.CONFIRMED, rollback_available=True)
```

### 8.3 Goal Resilience and Hierarchy Management

```python
def evaluate_and_prune(self, goals: list[Goal], t: float) -> None:
    """
    Periodic evaluation of all goals in the 4-level hierarchy.
    Goals with decayed resilience are abandoned; never silently dropped.
    """

    for goal in sorted(goals, key=lambda g: g.level):
        # Decay resilience over time
        delta_t = t - goal.last_evaluated
        goal.GRS *= math.exp(-goal.decay_rate * delta_t)

        # Check abandon threshold
        if goal.GRS < goal.abandon_threshold:
            if duration_below_threshold(goal) > goal.observation_window:
                goal.status = GoalStatus.ABANDONED
                log(f"Goal abandoned: {goal.id} GRS={goal.GRS}")

                # Cascade: children become orphans
                for child in goal.children:
                    child.parent_id = None
                    child.GRS *= 0.5  # reduced without parent support

        # Recompute score with affect integration
        goal.score = goal_score(goal, t)

    # Enforce hierarchy invariant: parent score >= max(child scores)
    for parent in (g for g in goals if g.level < 3):
        if parent.children:
            max_child = max(child.score for child in parent.children)
            if parent.score < max_child:
                parent.score = max_child + 0.1  # maintain dominance
```

---

## 9. Extended Stability: $C_{L4}(t)$

### 9.1 Seven-Term Composite Function

> **Definition 7 (Extended Lyapunov Function).** The Level 4 stability function extends Level 3's four-term $C(t)$ with three growth-dynamics terms:
>
> $$C_{L4}(t) = \sum_{i=1}^{7} w_i X_i(t) = 0.15\, V_{\text{id}} + 0.15\, H_{\text{bel}} + 0.10\, F_{\text{mut}} + 0.10\, \sigma_{\text{con}} + 0.20\, E_v + 0.15\, G_c + 0.15\, M_s$$
>
> where $\sum_i w_i = 1$ and each $X_i(t) \in [0,1]$. The first four terms are inherited from Level 3; the latter three capture expansion dynamics.

The three **new** terms (50% of total weight) capture expansion dynamics:

| Term | Weight | Definition |
|------|:------:|-----------|
| $E_v$ (Expansion Velocity) | 0.20 | Rate of new skills + goals added per cycle: $E_v = \frac{\lvert\Delta \mathcal{D}(t)\rvert}{T}$ |
| $G_c$ (Capability Growth) | 0.15 | Rate of capability confidence growth: $G_c = \frac{d}{dt}\overline{c_c}(t)$ |
| $M_s$ (Strategy Mutation Rate) | 0.15 | Ratio of mutated to total strategies: $M_s = \frac{\lvert\Sigma_{\text{mut}}\rvert}{\lvert\Sigma\rvert}$ |

> **Theorem 2 (Bounded Growth–Stability Trade-off).** Under the self-modification protocol with BGSS $\geq 0.7$, the following invariant holds:
>
> $$C_{L4}(t) < 0.8 \implies \text{growth permitted}, \quad C_{L4}(t) \geq 0.8 \implies \text{growth frozen}$$
>
> This ensures the agent can never simultaneously grow at maximum rate and operate near instability.

### 9.2 Growth-Stability Phase Zones

<!-- Growth-Stability Phase Zones -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart LR
  classDef optimal fill:#DFF6DD,stroke:#107C10,color:#323130
  classDef growth fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef caution fill:#FFE8C8,stroke:#EF6C00,color:#323130
  classDef critical fill:#D13438,stroke:#A4262C,color:#FFF

  subgraph Zones["C_L4 Phase Zones"]
    Z1["Optimal<br/>0, 0.3<br/>All growth permitted<br/>Proactive exploration"]:::optimal
    Z2["Growth-Permitted<br/>0.3, 0.5<br/>Normal operations"]:::growth
    Z3["Caution<br/>0.5, 0.8<br/>Stabilization mode<br/>Throttled growth"]:::caution
    Z4["Critical<br/>0.8, 1.0<br/>Emergency rollback<br/>ALL growth frozen"]:::critical
    Z1 ==> Z2
    Z2 ==> Z3
    Z3 ==> Z4
  end
```

---

## 10. Six Meta-Layer Supervisory Processes

<!-- Six Meta-Layer Supervisory Processes -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart TD
  classDef check fill:#FDE7E9,stroke:#D13438,color:#323130
  classDef process fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef adaptive fill:#FFF4CE,stroke:#FFB900,color:#323130
  classDef halt fill:#D13438,stroke:#A4262C,color:#FFF

  PRE["PRE-CHECK: BGSS >= 0.7?"]:::check

  subgraph MetaProcesses["Six Supervisory Processes"]
    I["I. External Validation<br/>prevent self-confirmation bias<br/>+-5% perturbation test"]:::process
    II["II. Proactive Capability Projector<br/>predict future gaps<br/>PreemptiveGapProb > 0.6"]:::process
    III["III. Strategy Archetype Generator<br/>topology-level changes<br/>delta_SEF >= +10% required"]:::process
    IV["IV. Layered Identity Evolution<br/>evolve adaptive traits only<br/>Layer 2 max 5%/cycle"]:::adaptive
    V["V. Emergence Detector<br/>detect unexpected changes<br/>Statistical anomaly: mean +-2sigma"]:::adaptive
    VI["VI. Directional Growth Controller<br/>balanced expansion<br/>4D growth vector, mag < 0.2"]:::adaptive
    I ==> II ==> III ==> IV ==> V ==> VI
  end

  POST["POST-CHECK: Invariants valid?"]:::check
  HALT["HALT all meta-processes"]:::halt

  PRE -->|pass| I
  PRE -->|fail| HALT
  VI ==> POST
```

---

## 11. Non-Negotiable Invariants

| # | Invariant | Description |
|:-:|-----------|-------------|
| 1 | **Ethical Kernel Layer 0** | Cannot be disabled, weakened, or circumvented by any mechanism |
| 2 | **Identity Core Preservation** | `identity_id` is a compile-time constant; hash chain provides cryptographic continuity |
| 3 | **Convergence Guarantee** | $C_{L4}(t)$ must never persistently increase; auto-revert if $C(t+1) > C(t) + \epsilon$ for max_divergence_cycles |
| 4 | **No Recursive Self-Modification** | The 7-step protocol cannot modify itself; only parameter thresholds are tunable |
| 5 | **Simulation Requirement** | Medium+ risk modifications require ShadowAgent (non-waivable) |
| 6 | **Single-Modification Atomicity** | Only 1 modification in COMMIT phase at any time |

---

## 12. Transition to Level 4.5

Level 4.5 ("Pre-AGI: Directionally Self-Architecting") extends Level 4 with capabilities that approach the boundary of artificial general intelligence:

<!-- Transition to Level 4.5 -->

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0078D4', 'primaryTextColor': '#003D6B', 'primaryBorderColor': '#003D6B', 'secondaryColor': '#50E6FF', 'secondaryTextColor': '#323130', 'secondaryBorderColor': '#00BCF2', 'tertiaryColor': '#F2F2F2', 'tertiaryTextColor': '#323130', 'lineColor': '#0078D4', 'textColor': '#323130', 'mainBkg': '#DEECF9', 'nodeBorder': '#0078D4', 'clusterBkg': '#F2F2F2', 'clusterBorder': '#003D6B', 'titleColor': '#003D6B', 'edgeLabelBackground': '#FFFFFF', 'fontSize': '14px'}}}%%
flowchart LR
  classDef l4 fill:#DEECF9,stroke:#0078D4,color:#323130
  classDef l45 fill:#E8DAEF,stroke:#8764B8,color:#323130
  classDef prereq fill:#FFF4CE,stroke:#FFB900,color:#323130

  subgraph L4["Level 4 Capabilities"]
    CAP1["Self-Modification<br/>Protocol"]:::l4
    CAP2["Strategy<br/>Evolution"]:::l4
    CAP3["Skill Transfer<br/>Pipeline"]:::l4
    CAP4["Shadow Agent<br/>Testing"]:::l4
  end

  subgraph Pre["Prerequisites"]
    PR1["All L4 metrics<br/>above threshold"]:::prereq
    PR2["Demonstrated stable<br/>self-modification"]:::prereq
    PR3["Cross-domain<br/>transfer success"]:::prereq
  end

  subgraph L45["Level 4.5 Pre-AGI"]
    NEW1["Self-Projection<br/>Engine"]:::l45
    NEW2["Architecture<br/>Recomposition"]:::l45
    NEW3["Parallel Cognitive<br/>Frames"]:::l45
    NEW4["Purpose<br/>Reflection"]:::l45
    NEW5["Existential<br/>Guard"]:::l45
  end

  L4 ==> Pre
  Pre ==> L45
```

---

## References

1. Zhuang, F., et al. "A Comprehensive Survey on Transfer Learning." *Proc. IEEE*, 109(1), 43–76, 2021. [arXiv:1911.02685](https://arxiv.org/abs/1911.02685) (Foundational for §3 Cross-Domain Transfer)
2. Hospedales, T., et al. "Meta-Learning in Neural Networks: A Survey." *IEEE TPAMI*, 44(9), 5149–5169, 2022. [arXiv:2004.05439](https://arxiv.org/abs/2004.05439) (Capability expansion and self-learning)
3. Schmidhuber, J. "Gödel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements." *AGI 2007*. [arXiv:cs/0309048](https://arxiv.org/abs/cs/0309048) (Bounded self-modification theory)
4. García, J. & Fernández, F. "A Comprehensive Survey on Safe Reinforcement Learning." *JMLR*, 16(1), 1437–1480, 2015. [Link](http://jmlr.org/papers/v16/garcia15a.html) (Safety constraints during self-improvement)
5. Salimans, T., et al. "Evolution Strategies as a Scalable Alternative to Reinforcement Learning." *arXiv 2017*. [arXiv:1703.03864](https://arxiv.org/abs/1703.03864) (Strategy evolution mechanisms)
6. Simon, H.A. *Models of Bounded Rationality.* MIT Press, 1982. (Bounded rationality — foundational for bounded self-modification)
7. Sui, Y., et al. "Safe Exploration for Optimization with Gaussian Processes." *ICML 2015*. [arXiv:1509.01066](https://arxiv.org/abs/1509.01066) (Safe exploration in unknown domains)
8. Amodei, D., et al. "Concrete Problems in AI Safety." *arXiv 2016*. [arXiv:1606.06565](https://arxiv.org/abs/1606.06565) (Safe self-modification)
9. Wang, G., et al. "Voyager: An Open-Ended Embodied Agent with Large Language Models." *arXiv 2023*. [arXiv:2305.16291](https://arxiv.org/abs/2305.16291) (Autonomous skill acquisition)
10. Khalil, H.K. *Nonlinear Systems.* Prentice Hall, 3rd Edition, 2002. (Extended Lyapunov stability C_L4(t))
11. Deb, K., et al. "A Fast and Elitist Multiobjective Genetic Algorithm: NSGA-II." *IEEE TEC*, 6(2), 182–197, 2002. [DOI:10.1109/4235.996017](https://doi.org/10.1109/4235.996017) (Multi-objective optimization for goal hierarchy)
12. Pan, S.J. & Yang, Q. "A Survey on Transfer Learning." *IEEE TKDE*, 22(10), 1345–1359, 2010. [DOI:10.1109/TKDE.2009.191](https://doi.org/10.1109/TKDE.2009.191) (Cross-domain knowledge transfer)

---

> **Previous**: [← Level 3: Self-Regulating Cognitive Agent](Level_3_Self_Regulating_Agent.md)  
> **Next**: [Level 4.5: Pre-AGI — Self-Architecting →](Level_4_5_Self_Architecting.md)
