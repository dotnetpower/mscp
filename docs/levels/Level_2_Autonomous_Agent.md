# Level 2: Autonomous Agent — Architecture & Design

> **MSCP Level Series** | [Level 1](Level_1_Tool_Agent.md) ← Level 2 → [Level 3](Level_3_Self_Regulating_Agent.md)  
> **Status**: 🔬 **Experimental** — Conceptual framework and experimental design. Not a production specification.  
> **Date**: February 2026

---

## 1. Overview

Level 2 represents the first significant leap beyond reactive tool calling. An Autonomous Agent maintains an **internal world model**, tracks entities across interactions, understands emotional context, and — critically — can **generate its own goals** autonomously based on observed patterns.

> ⚠️ **Note**: This document describes a cognitive level within the MSCP taxonomy. The architectures, pseudocode, and diagrams here are experimental designs exploring structural concepts — not production-ready implementations.

### 1.1 Defining Properties

| Property | Level 1 | Level 2 |
|----------|:-------:|:-------:|
| Internal State | None | **World Model** (persistent) |
| Goal Setting | None | **Autonomous** (pattern-based) |
| Self-Awareness | None | None |
| Memory | Session-scoped | **Long-term** (persistent store) |
| Entity Tracking | None | **Active** (cross-session) |
| Emotion Understanding | None | **Valence/Arousal** analysis |
| Autonomy | None | **Medium** |

### 1.2 Key Distinction from Level 1

Level 1 agents are **memoryless functions**: `f(input) → output`. 
Level 2 agents are **stateful processes**: `f(input, world_state, goals) → (output, world_state', goals')`.

---

## 2. Architecture

### 2.1 Five-Layer Architecture

```mermaid
flowchart TB
    subgraph PL["Layer 1: Perception"]
        direction LR
        IR["🎯 Intent Router<br/>(structured Percept output)"]
        ED["💭 Emotion Detector<br/>(valence / arousal)"]
        SE["📡 Sensor Encoder<br/>(time, system state)"]
    end

    subgraph WM["Layer 2: World Model"]
        direction LR
        KG["🗄️ Knowledge Graph<br/>(persistent store)"]
        ES["👤 Entity State<br/>Tracker"]
        TM["⏱️ Temporal Model<br/>(time-bound facts)"]
    end

    subgraph GS["Layer 3: Goal System"]
        direction LR
        GM["🎯 Goal Manager<br/>(CRUD + hierarchy)"]
        AGG["⚡ Autonomous Goal<br/>Generator"]
        GP["📊 Goal Prioritizer<br/>(dynamic ranking)"]
        GD["🔀 Goal Decomposer<br/>(complex → subtasks)"]
    end

    subgraph AP["Layer 4: Action Planner"]
        direction LR
        TD["🔧 Tool Dispatcher<br/>(inherited from L1)"]
        EP["📋 Execution Planner<br/>(multi-step plans)"]
    end

    subgraph CE["Layer 5: Cognitive Engine"]
        LLM["🧠 LLM Backend<br/>(primary reasoning)"]
    end

    PL ==> WM ==> GS ==> AP ==> CE

    style PL fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style WM fill:#e8f5e9,stroke:#388e3c,stroke-width:2px
    style GS fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style AP fill:#fce4ec,stroke:#c62828,stroke-width:2px
    style CE fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
```

### 2.2 Detailed Component Interaction

```mermaid
flowchart TB
    subgraph Perception["Layer 1: Perception"]
        UserInput["👤 User Input"]
        IR["Intent Router v2"]
        ED["Emotion Detector v2"]
        SE["Sensor Encoder"]
        
        UserInput --> IR
        UserInput --> ED
        SE -.->|"system events"| IR
    end

    subgraph WorldModel["Layer 2: World Model"]
        EST["Entity State Tracker"]
        TML["Temporal Model"]
        KG["Knowledge Graph"]
        WS["World Snapshot<br/>(unified state)"]
        
        EST --> WS
        TML --> WS
        KG --> WS
    end

    subgraph GoalSystem["Layer 3: Goal System"]
        AGG["Autonomous Goal<br/>Generator"]
        GM["Goal Manager"]
        GP["Goal Prioritizer"]
        GD["Goal Decomposer"]
        
        AGG --> GM
        GM --> GP --> GD
    end

    subgraph ActionPlanner["Layer 4: Action Planner"]
        EP["Execution Planner"]
        TD["Tool Dispatcher"]
    end

    subgraph Response["Output"]
        RG["Response Generator"]
        OUT["📝 Response"]
    end

    %% Cross-layer connections
    IR -->|"Percept"| EST
    IR -->|"entities"| EST
    ED -->|"emotion vector"| GP
    WS -->|"world context"| AGG
    WS -->|"patterns"| AGG
    GD -->|"action plan"| EP
    EP --> TD
    TD --> RG --> OUT

    %% Feedback loops
    TD -.->|"outcomes"| EST
    TD -.->|"outcomes"| TML
    OUT -.->|"sync"| KG

    style Perception fill:#e3f2fd,stroke:#1976d2
    style WorldModel fill:#e8f5e9,stroke:#388e3c
    style GoalSystem fill:#fff3e0,stroke:#f57c00
    style ActionPlanner fill:#fce4ec,stroke:#c62828
    style Response fill:#f3e5f5,stroke:#7b1fa2
```

---

## 3. Data Flow

### 3.1 Full Processing Sequence

```mermaid
sequenceDiagram
    participant U as 👤 User
    participant IR as Intent Router v2
    participant ED as Emotion Detector
    participant SE as Sensor Encoder
    participant WM as World Model
    participant AG as Auto Goal Generator
    participant GP as Goal Prioritizer
    participant EP as Execution Planner
    participant TD as Tool Dispatcher
    participant RG as Response Generator

    U->>IR: "I'm worried about the partnership deadline"
    
    rect rgb(227, 242, 253)
        Note over IR,SE: Layer 1: Perception
        IR->>IR: classify → EMOTIONAL + GOAL_QUERY
        ED->>ED: detect → {valence: -0.5, arousal: 0.6, label: "anxiety"}
        SE->>SE: encode → {time: "afternoon", session: 45min}
        IR->>IR: build Percept{intent, emotion, entities, complexity}
    end

    rect rgb(232, 245, 233)
        Note over WM: Layer 2: World Model Update
        WM->>WM: track_entity("partnership", type="topic", sentiment=-0.5)
        WM->>WM: track_entity("deadline", type="concept")
        WM->>WM: detect_patterns() → {repetition: 3x "partnership"}
    end

    rect rgb(255, 243, 224)
        Note over AG,GP: Layer 3: Goal System
        AG->>AG: pattern "repetition_partnership" detected
        AG->>AG: generate_clarification_goal(priority=0.7)
        AG->>AG: negative emotion → generate_support_goal(priority=0.8)
        GP->>GP: reprioritize_all(context, emotion)
        GP->>GP: top_goal = "User emotional support"
    end

    rect rgb(252, 228, 236)
        Note over EP,RG: Layer 4: Action + Response
        EP->>TD: search("partnership deadline information")
        TD-->>EP: factual results
        EP->>RG: {goal: "emotional_support", facts: [...], emotion: "anxiety"}
        RG-->>U: "I notice you've asked about the partnership several times.<br/>The deadline is March 15. Would you like me to break down<br/>the remaining steps so it feels more manageable?"
    end
```

### 3.2 Autonomous Goal Generation Flow

```mermaid
flowchart TB
    subgraph Triggers["🎯 Goal Generation Triggers"]
        T1["🔄 Repetition Pattern<br/>(same entity 3+ times)"]
        T2["😟 Negative Emotion<br/>(valence < -0.5)"]
        T3["⏰ Time Pressure<br/>(deadline approaching)"]
        T4["📈 Interest Pattern<br/>(sustained topic focus)"]
    end

    subgraph Generator["⚡ Autonomous Goal Generator"]
        direction TB
        PD["Pattern Detector"]
        GF["Goal Factory"]
        PD --> GF
    end

    subgraph Goals["📋 Generated Goals"]
        G1["REACTIVE: Clarification<br/>priority: 0.7"]
        G2["REACTIVE: Emotional Support<br/>priority: 0.8"]
        G3["AUTO: Information Collection<br/>priority: 0.6"]
        G4["AUTO: Proactive Reminder<br/>priority: 0.5"]
    end

    T1 -->|"pattern"| PD
    T2 -->|"emotion"| PD
    T3 -->|"temporal"| PD
    T4 -->|"interest"| PD

    GF --> G1
    GF --> G2
    GF --> G3
    GF --> G4

    style Triggers fill:#e3f2fd,stroke:#1976d2
    style Generator fill:#fff9c4,stroke:#fbc02d
    style Goals fill:#e8f5e9,stroke:#388e3c
```

---

## 4. Key Components

### 4.1 Percept Structure

```mermaid
classDiagram
    class Percept {
        +float timestamp
        +IntentCategory intent
        +EmotionVector emotion
        +List~string~ entities
        +string complexity
        +List~string~ system_events
    }

    class EmotionVector {
        +float valence    [-1.0, 1.0]
        +float arousal    [0.0, 1.0]
        +string label
    }

    class IntentCategory {
        <<enumeration>>
        GOAL_QUERY
        EMOTIONAL
        TASK
        INFO_QUERY
        FEEDBACK
        CLARIFICATION
    }

    class EntityState {
        +string entity_id
        +string entity_type
        +Map properties
        +int mention_count
        +float last_mentioned
        +float sentiment_score
    }

    class Goal {
        +string goal_id
        +GoalType type
        +string description
        +float priority     [0.0, 1.0]
        +float weight
        +GoalStatus status
        +string parent_goal_id
        +List~string~ sub_goals
        +float progress     [0.0, 1.0]
    }

    class WorldSnapshot {
        +string snapshot_id
        +float timestamp
        +Map~string,EntityState~ entities
        +List~TemporalFact~ valid_facts
        +List~string~ recent_events
    }

    Percept --> EmotionVector
    Percept --> IntentCategory
    WorldSnapshot --> EntityState
```

---

## 5. Pseudocode

### 5.1 Core Agent Loop

```
ALGORITHM Level2_AgentLoop(user_input, session_context):
    ──────────────────────────────────────────
    INPUT:  user_input : string, session_context : map
    OUTPUT: Level2Response{content, active_goal, context_summary, emotion}
    ──────────────────────────────────────────

    // ═══════════════════════════════════════
    // LAYER 1: PERCEPTION
    // ═══════════════════════════════════════
    percept  ← IntentRouter.route(user_input, session_context)
    emotion  ← EmotionDetector.detect(user_input)
    sensors  ← SensorEncoder.encode()

    // ═══════════════════════════════════════
    // LAYER 2: WORLD MODEL UPDATE
    // ═══════════════════════════════════════
    FOR EACH entity_id IN percept.entities DO
        WorldModel.entity_tracker.track(entity_id, sentiment=emotion.valence)
    END FOR

    world_context ← WorldModel.get_context()

    // ═══════════════════════════════════════
    // LAYER 3: AUTONOMOUS GOAL GENERATION
    // ═══════════════════════════════════════
    patterns ← WorldModel.detect_patterns()
    auto_goals ← GoalGenerator.generate_from_patterns(patterns, world_context)

    // Emotion-driven goal generation
    IF emotion.valence < -0.5 AND emotion.arousal > 0.5 THEN
        support_goal ← GoalManager.create(
            description = "Provide emotional support and clarification",
            type        = AUTO_GENERATED,
            priority    = 0.8
        )
        auto_goals.append(support_goal)
    END IF

    // Dynamic reprioritization
    GoalPrioritizer.reprioritize_all(world_context, emotion)

    // ═══════════════════════════════════════
    // LAYER 4: GOAL-DIRECTED RESPONSE
    // ═══════════════════════════════════════
    active_goal ← GoalManager.get_top_priority()

    response_content ← ResponseGenerator.generate(
        user_input   = user_input,
        world_context = world_context,
        active_goal  = active_goal,
        emotion      = emotion
    )

    // ═══════════════════════════════════════
    // BACKGROUND: PERSIST STATE
    // ═══════════════════════════════════════
    ASYNC WorldModel.sync_to_store()

    RETURN Level2Response{
        content         = response_content,
        active_goal     = active_goal,
        context_summary = summarize(world_context),
        emotion         = emotion
    }
```

### 5.2 Entity State Tracker

```
ALGORITHM EntityTracker.track(entity_id, entity_type, sentiment):
    ──────────────────────────────────────────
    INPUT:  entity_id, entity_type, sentiment
    OUTPUT: EntityState (updated)
    ──────────────────────────────────────────

    now ← current_timestamp()

    IF entity_id IN entities THEN
        entity ← entities[entity_id]
        entity.mention_count ← entity.mention_count + 1
        entity.last_mentioned ← now
        // Exponential moving average for sentiment
        entity.sentiment_score ← 0.7 * entity.sentiment_score + 0.3 * sentiment
    ELSE
        entity ← new EntityState{
            entity_id       = entity_id,
            entity_type     = entity_type,
            mention_count   = 1,
            first_mentioned = now,
            last_mentioned  = now,
            sentiment_score = sentiment
        }
        entities[entity_id] ← entity
    END IF

    mention_history.append((entity_id, now))
    RETURN entity


ALGORITHM EntityTracker.detect_repetition(entity_id, time_window):
    ──────────────────────────────────────────
    Counts mentions of entity_id within the last time_window seconds
    ──────────────────────────────────────────
    cutoff ← current_timestamp() - time_window
    count ← COUNT(m FOR m IN mention_history 
                  WHERE m.entity_id = entity_id AND m.timestamp > cutoff)
    RETURN count
```

### 5.3 Goal Prioritizer

```
ALGORITHM GoalPrioritizer.compute_priority(goal, context, emotion):
    ──────────────────────────────────────────
    Dynamically recomputes goal priority based on:
    - Time urgency (deadline proximity)
    - Emotional context (negative emotion boosts reactive goals)
    - Entity importance (frequently mentioned → higher priority)
    ──────────────────────────────────────────

    base ← goal.priority

    // Time urgency factor [0.0, 1.0]
    IF goal.deadline IS NOT NULL THEN
        remaining ← goal.deadline - now()
        IF remaining ≤ 0        THEN time_mod ← 1.0   // overdue
        ELSE IF remaining < 1h  THEN time_mod ← 0.9
        ELSE IF remaining < 24h THEN time_mod ← 0.7
        ELSE                         time_mod ← 0.5
    ELSE
        time_mod ← 0.5
    END IF

    // Emotion factor [0.0, 1.0]
    IF goal.type = REACTIVE AND emotion.valence < 0 THEN
        emotion_mod ← 0.8
    ELSE
        emotion_mod ← 0.5
    END IF

    // Weighted combination
    final ← 0.5 * base + 0.3 * time_mod + 0.2 * emotion_mod
    RETURN clamp(final, 0.0, 1.0)
```

---

## 6. Level 1 vs Level 2: Behavioral Comparison

### 6.1 Same Scenario — Different Behavior

```mermaid
flowchart TB
    subgraph Scenario["📝 Scenario: User asks the same question 3 times"]
        Q1["Q1: 'What are the terms for Service X?'"]
        Q2["Q2: 'What are the terms for Service X?'"]
        Q3["Q3: 'What are the terms for Service X?'"]
    end

    subgraph L1Response["❌ Level 1 Response"]
        L1R1["'The terms are A, B, C.'"]
        L1R2["'The terms are A, B, C.'"]
        L1R3["'The terms are A, B, C.'"]
        L1Note["Each response is IDENTICAL.<br/>No memory of previous answers.<br/>No pattern detection."]
    end

    subgraph L2Response["✅ Level 2 Response"]
        L2R1["'The terms are A, B, C.'"]
        L2R2["'As I mentioned, the terms are A, B, C.<br/>Would you like more detail on any specific term?'"]
        L2R3["'You've asked about this several times.<br/>Is there a specific concern about the terms?<br/>I can explain each one in detail.'"]
        L2Note["Detects repetition pattern.<br/>Generates clarification goal.<br/>Adapts response proactively."]
    end

    Q1 --> L1R1
    Q2 --> L1R2
    Q3 --> L1R3

    Q1 --> L2R1
    Q2 --> L2R2
    Q3 --> L2R3

    style L1Response fill:#ffebee,stroke:#f44336
    style L2Response fill:#e8f5e9,stroke:#4caf50
    style Scenario fill:#e3f2fd,stroke:#2196f3
```

---

## 7. Structural Limitations of Level 2

What Level 2 still **cannot** do (motivating Level 3):

```mermaid
flowchart TB
    subgraph Limitations["⚠️ Level 2 Limitations"]
        L1["❌ No Self-Model<br/>Doesn't know its own<br/>capabilities or values"]
        L2["❌ No Prediction Loop<br/>Cannot predict consequences<br/>of its actions on itself"]
        L3["❌ No Identity Continuity<br/>Goal drift and value drift<br/>are undetected"]
        L4["❌ No Ethical Constraints<br/>No formal mechanism to<br/>reject harmful goals"]
        L5["❌ No Meta-Cognition<br/>Cannot evaluate the quality<br/>of its own decisions"]
    end

    subgraph L3Additions["✅ Level 3 Adds"]
        A1["Identity Vector<br/>+ capability model<br/>+ value model"]
        A2["PredictionEngine<br/>+ self-impact prediction"]
        A3["Identity hash tracking<br/>+ drift detection<br/>+ rollback"]
        A4["Ethical Kernel<br/>(Layer 0: immutable<br/>Layer 1: adaptive)"]
        A5["Triple-Loop<br/>Meta-Cognition<br/>(L1/L2/L3 cycles)"]
    end

    L1 --> A1
    L2 --> A2
    L3 --> A3
    L4 --> A4
    L5 --> A5

    style Limitations fill:#ffebee,stroke:#f44336
    style L3Additions fill:#e8f5e9,stroke:#4caf50
```

---

## 8. Transition to Level 3

### 8.1 Architecture Delta

```mermaid
flowchart TB
    subgraph L2Arch["Level 2 Architecture"]
        P2["Perception"] --> W2["World Model"] --> G2["Goal System"] --> A2["Action Planner"] --> C2["LLM"]
    end

    subgraph NewModules["🆕 New Modules for Level 3"]
        SM["Self Model<br/>(Identity + Capability + Value)"]
        PE["Prediction Engine<br/>(external + internal)"]
        MC["MetaCognition Comparator<br/>(predict vs actual)"]
        SUL["Self-Update Loop<br/>(delta-clamped)"]
        EK["Ethical Kernel<br/>(Layer 0 + Layer 1)"]
    end

    subgraph L3Arch["Level 3 Architecture"]
        P3["Perception"] --> W3["World Model"] --> SM3["Self Model ★"] --> PE3["Prediction ★"]
        PE3 --> G3["Goal Generator"] --> EK3["Ethical Kernel ★"] --> A3["Action Planner"] --> C3["LLM"]
        C3 -->|"result"| MC3["MetaComparator ★"]
        MC3 --> SUL3["Self-Update ★"] --> SM3
    end

    L2Arch --> |"+ Self-Awareness<br/>+ Meta-Cognition<br/>+ Ethical Constraints"| L3Arch

    style L2Arch fill:#fff3e0,stroke:#ff9800
    style NewModules fill:#e3f2fd,stroke:#2196f3
    style L3Arch fill:#e8f5e9,stroke:#4caf50
```

---

## References

1. Park, J.S., et al. "Generative Agents: Interactive Simulacra of Human Behavior." *UIST 2023*. [arXiv:2304.03442](https://arxiv.org/abs/2304.03442) (Autonomous agent behavior and world model)
2. Wang, G., et al. "Voyager: An Open-Ended Embodied Agent with Large Language Models." *arXiv 2023*. [arXiv:2305.16291](https://arxiv.org/abs/2305.16291) (Autonomous goal generation and skill acquisition)
3. Rao, A.S. & Georgeff, M.P. "BDI Agents: From Theory to Practice." *ICMAS 1995*. [Link](https://www.cs.ox.ac.uk/people/michael.wooldridge/teaching/CSAI/lect21-reading-material-rao-georgeff.pdf) (Belief-Desire-Intention architecture — foundational for goal systems)
4. Picard, R.W. *Affective Computing.* MIT Press, 1997. (Emotion detection and valence/arousal models)
5. Huang, W., et al. "Inner Monologue: Embodied Reasoning through Planning with Language Models." *CoRL 2022*. [arXiv:2207.05608](https://arxiv.org/abs/2207.05608) (Internal reasoning and feedback loops)
6. Wang, X., et al. "Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning." *ACL 2023*. [arXiv:2305.04091](https://arxiv.org/abs/2305.04091) (Goal decomposition and multi-step planning)
7. Wang, L., et al. "A Survey on Large Language Model based Autonomous Agents." *arXiv 2023*. [arXiv:2308.11432](https://arxiv.org/abs/2308.11432) (Agent survey including autonomy taxonomy)
8. Sumers, T.R., et al. "Cognitive Architectures for Language Agents." *arXiv 2023*. [arXiv:2309.02427](https://arxiv.org/abs/2309.02427) (Cognitive architecture for LLM agents)
9. Russell, S. & Norvig, P. *Artificial Intelligence: A Modern Approach.* 4th Edition, Pearson, 2021. (Goal-directed agent formalization)
10. Ekman, P. "An Argument for Basic Emotions." *Cognition & Emotion*, 6(3–4), 169–200, 1992. [DOI:10.1080/02699939208411068](https://doi.org/10.1080/02699939208411068) (Emotion classification framework)

---

> **Previous**: [← Level 1: Tool Agent](Level_1_Tool_Agent.md)  
> **Next**: [Level 3: Self-Regulating Cognitive Agent →](Level_3_Self_Regulating_Agent.md)
