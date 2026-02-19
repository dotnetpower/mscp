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

![Level 2 Five-Layer Architecture](../diagrams/level2-five-layer-architecture.svg)

### 2.2 Detailed Component Interaction

![Level 2 Component Interaction](../diagrams/level2-component-interaction.svg)

---

## 3. Data Flow

### 3.1 Full Processing Sequence

```mermaid
sequenceDiagram
    actor U as 👤 User
    participant IR as Intent Router v2
    participant ED as Emotion Detector
    participant SE as Sensor Encoder
    participant WM as World Model
    participant AG as Auto Goal Gen
    participant GP as Goal Prioritizer
    participant EP as Exec Planner
    participant TD as Tool Dispatcher
    participant RG as Response Gen

    U->>IR: "I'm worried about the partnership deadline"

    rect rgb(227, 242, 253)
        Note over IR,SE: Perception Phase
        IR->>IR: classify → EMOTIONAL + GOAL_QUERY
        ED->>ED: detect → {valence: -0.5, arousal: 0.6, label: anxiety}
        SE->>SE: encode → {time: "afternoon", session: 45min}
        IR->>IR: build Percept{intent, emotion, entities, complexity}
    end

    rect rgb(200, 230, 201)
        Note over WM: World Model Update
        WM->>WM: track_entity("partnership", type="topic", sentiment=-0.5)
        WM->>WM: track_entity("deadline", type="concept")
        WM->>WM: detect_patterns() → {repetition: 3x "partnership"}
    end

    rect rgb(255, 243, 224)
        Note over AG,GP: Goal Generation
        AG->>AG: pattern "repetition_partnership" detected
        AG->>AG: generate_clarification_goal(priority=0.7)
        AG->>AG: negative emotion → generate_support_goal(priority=0.8)
        GP->>GP: reprioritize_all(context, emotion)
        GP->>GP: top_goal = "User emotional support"
    end

    rect rgb(237, 231, 246)
        Note over EP,RG: Execution & Response
        EP->>TD: search("partnership deadline information")
        TD-->>EP: factual results
        EP->>RG: {goal: "emotional_support", facts: [...], emotion: "anxiety"}
        RG-->>U: "I notice you've asked about the partnership<br/>several times. The deadline is March 15.<br/>Would you like me to break down<br/>the remaining steps?"
    end
```

### 3.2 Autonomous Goal Generation Flow

![Level 2 Autonomous Goal Generation](../diagrams/level2-goal-generation.svg)

---

## 4. Key Components

### 4.1 Percept Structure

![Level 2 Percept Structure](../diagrams/level2-percept-structure.svg)

---

## 5. Pseudocode

### 5.1 Core Agent Loop

```python
def level2_agent_loop(user_input: str, session_context: dict) -> Level2Response:
    """
    Level 2 core agent loop with world model and autonomous goal generation.
    Input:  user_input — user request, session_context — session state
    Output: Level2Response with content, active_goal, context_summary, emotion
    """

    # ═══ LAYER 1: PERCEPTION ═══
    percept = IntentRouter.route(user_input, session_context)
    emotion = EmotionDetector.detect(user_input)
    sensors = SensorEncoder.encode()

    # ═══ LAYER 2: WORLD MODEL UPDATE ═══
    for entity_id in percept.entities:
        WorldModel.entity_tracker.track(entity_id, sentiment=emotion.valence)

    world_context = WorldModel.get_context()

    # ═══ LAYER 3: AUTONOMOUS GOAL GENERATION ═══
    patterns = WorldModel.detect_patterns()
    auto_goals = GoalGenerator.generate_from_patterns(patterns, world_context)

    # Emotion-driven goal generation
    if emotion.valence < -0.5 and emotion.arousal > 0.5:
        support_goal = GoalManager.create(
            description="Provide emotional support and clarification",
            type=GoalType.AUTO_GENERATED,
            priority=0.8,
        )
        auto_goals.append(support_goal)

    # Dynamic reprioritization
    GoalPrioritizer.reprioritize_all(world_context, emotion)

    # ═══ LAYER 4: GOAL-DIRECTED RESPONSE ═══
    active_goal = GoalManager.get_top_priority()

    response_content = ResponseGenerator.generate(
        user_input=user_input,
        world_context=world_context,
        active_goal=active_goal,
        emotion=emotion,
    )

    # ═══ BACKGROUND: PERSIST STATE ═══
    asyncio.create_task(WorldModel.sync_to_store())

    return Level2Response(
        content=response_content,
        active_goal=active_goal,
        context_summary=summarize(world_context),
        emotion=emotion,
    )
```

### 5.2 Entity State Tracker

```python
def track(self, entity_id: str, entity_type: str, sentiment: float) -> EntityState:
    """
    Track or update an entity's state.
    Input:  entity_id, entity_type, sentiment score
    Output: Updated EntityState
    """

    now = time.time()

    if entity_id in self.entities:
        entity = self.entities[entity_id]
        entity.mention_count += 1
        entity.last_mentioned = now
        # Exponential moving average for sentiment
        entity.sentiment_score = 0.7 * entity.sentiment_score + 0.3 * sentiment
    else:
        entity = EntityState(
            entity_id=entity_id,
            entity_type=entity_type,
            mention_count=1,
            first_mentioned=now,
            last_mentioned=now,
            sentiment_score=sentiment,
        )
        self.entities[entity_id] = entity

    self.mention_history.append((entity_id, now))
    return entity


def detect_repetition(self, entity_id: str, time_window: float) -> int:
    """
    Count mentions of entity_id within the last time_window seconds.
    """
    cutoff = time.time() - time_window
    count = sum(
        1 for eid, ts in self.mention_history
        if eid == entity_id and ts > cutoff
    )
    return count
```

### 5.3 Goal Prioritizer

```python
def compute_priority(self, goal: Goal, context: WorldContext, emotion: EmotionVector) -> float:
    """
    Dynamically recompute goal priority based on:
    - Time urgency (deadline proximity)
    - Emotional context (negative emotion boosts reactive goals)
    - Entity importance (frequently mentioned → higher priority)
    """

    base = goal.priority

    # Time urgency factor [0.0, 1.0]
    if goal.deadline is not None:
        remaining = goal.deadline - time.time()
        if remaining <= 0:
            time_mod = 1.0       # overdue
        elif remaining < 3600:   # < 1 hour
            time_mod = 0.9
        elif remaining < 86400:  # < 24 hours
            time_mod = 0.7
        else:
            time_mod = 0.5
    else:
        time_mod = 0.5

    # Emotion factor [0.0, 1.0]
    if goal.type == GoalType.REACTIVE and emotion.valence < 0:
        emotion_mod = 0.8
    else:
        emotion_mod = 0.5

    # Weighted combination
    final = 0.5 * base + 0.3 * time_mod + 0.2 * emotion_mod
    return max(0.0, min(1.0, final))
```

---

## 6. Level 1 vs Level 2: Behavioral Comparison

### 6.1 Same Scenario — Different Behavior

![Level 2 Behavioral Comparison](../diagrams/level2-behavioral-comparison.svg)

---

## 7. Structural Limitations of Level 2

What Level 2 still **cannot** do (motivating Level 3):

![Level 2 Structural Limitations](../diagrams/level2-limitations.svg)

---

## 8. Transition to Level 3

### 8.1 Architecture Delta

![Level 2 to Level 3 Transition](../diagrams/level2-transition-to-l3.svg)

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
