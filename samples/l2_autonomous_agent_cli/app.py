import argparse
import fnmatch
import json
import os
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path

from openai import OpenAI


STATE_VERSION = 2
MANDATE_ID = "local-demo"
MAX_TOOL_ROUNDS = 4
MAX_CONTEXT_MESSAGES = 20
MAX_NOTES = 100
MAX_AUDIT_EVENTS = 200
NOTE_TTL_DAYS = 30
GOAL_TTL_DAYS = 7


def search_files(query: str, max_results: int = 20) -> list[str]:
    """Search for files in the current repo by name or simple glob."""
    root = Path(os.getenv("L2_SEARCH_ROOT", ".")).expanduser().resolve()
    if not root.is_dir():
        raise ValueError("L2_SEARCH_ROOT must be an existing directory")

    results: list[str] = []

    is_glob = any(ch in query for ch in ["*", "?", "["])
    query_lower = query.lower()

    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            name_lower = filename.lower()
            if is_glob:
                if not fnmatch.fnmatch(name_lower, query_lower):
                    continue
            else:
                if query_lower not in name_lower:
                    continue

            candidate = Path(dirpath, filename)
            try:
                candidate.resolve().relative_to(root)
            except ValueError:
                continue

            results.append(candidate.relative_to(root).as_posix())
            if len(results) >= max_results:
                return results

    return results


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def to_iso(value: datetime) -> str:
    return value.isoformat().replace("+00:00", "Z")


def parse_iso(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def default_state() -> dict:
    return {
        "version": STATE_VERSION,
        "notes": [],
        "goals": [],
        "triggers": [],
        "audit": [],
    }


def normalize_state(raw: dict) -> dict:
    state = default_state()
    for key in ("notes", "goals", "triggers", "audit"):
        value = raw.get(key, [])
        state[key] = value if isinstance(value, list) else []

    now = utc_now()
    for note in state["notes"]:
        note.setdefault("note_id", str(uuid.uuid4()))
        note.setdefault("provenance", {"source": "legacy", "mandate_id": MANDATE_ID})
        note.setdefault("created_at", to_iso(now))
        note.setdefault("expires_at", to_iso(now + timedelta(days=NOTE_TTL_DAYS)))

    migrated_goals = []
    for goal in state["goals"]:
        if "goal_id" in goal:
            migrated_goals.append(goal)
            continue
        description = str(goal.get("goal", "Legacy user goal")).strip()
        migrated = build_goal(
            description=description,
            goal_type="USER",
            provenance={
                "source": "legacy",
                "method": "state_migration",
                "mandate_id": MANDATE_ID,
            },
        )
        migrated_goals.append(migrated)
    state["goals"] = migrated_goals
    return state


def load_state(path: str) -> dict:
    state_path = Path(path)
    if not state_path.exists():
        return default_state()

    with state_path.open("r", encoding="utf-8") as handle:
        raw = json.load(handle)
    if not isinstance(raw, dict):
        raise ValueError("Persistent state must be a JSON object")
    return normalize_state(raw)


def save_state(path: str, state: dict) -> None:
    state_path = Path(path)
    state_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = state_path.with_suffix(f"{state_path.suffix}.tmp")
    with temporary_path.open("w", encoding="utf-8") as handle:
        json.dump(state, handle, indent=2)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temporary_path, state_path)


def record_audit(state: dict, event_type: str, details: dict) -> None:
    state["audit"].append(
        {
            "event_id": str(uuid.uuid4()),
            "event_type": event_type,
            "details": details,
            "created_at": to_iso(utc_now()),
        }
    )
    state["audit"] = state["audit"][-MAX_AUDIT_EVENTS:]


def apply_retention(state: dict, now: datetime | None = None) -> None:
    current = now or utc_now()
    state["notes"] = [
        note
        for note in state["notes"][-MAX_NOTES:]
        if parse_iso(note.get("expires_at", to_iso(current))) > current
    ]

    for goal in state["goals"]:
        if goal.get("status") in {"PENDING", "ACTIVE", "DEFERRED"}:
            if parse_iso(goal["expires_at"]) <= current:
                goal["status"] = "EXPIRED"

    active_goal_ids = {
        goal["goal_id"]
        for goal in state["goals"]
        if goal.get("status") in {"PENDING", "ACTIVE", "DEFERRED"}
    }
    for trigger in state["triggers"]:
        if trigger.get("status") == "REGISTERED":
            if (
                trigger.get("goal_id") not in active_goal_ids
                or parse_iso(trigger["expires_at"]) <= current
            ):
                trigger["status"] = "EXPIRED"


def add_note(state: dict, note: str, tag: str | None = None) -> dict:
    if not note.strip():
        raise ValueError("Note must not be empty")

    now = utc_now()
    entry = {
        "note_id": str(uuid.uuid4()),
        "note": note.strip(),
        "tag": tag.strip() if tag else None,
        "provenance": {"source": "user", "mandate_id": MANDATE_ID},
        "created_at": to_iso(now),
        "expires_at": to_iso(now + timedelta(days=NOTE_TTL_DAYS)),
    }
    state["notes"].append(entry)
    record_audit(state, "note_added", {"note_id": entry["note_id"]})
    return entry


def list_notes(state: dict, tag: str | None = None) -> list[dict]:
    if not tag:
        return state["notes"]
    tag_lower = tag.lower()
    return [item for item in state["notes"] if (item.get("tag") or "").lower() == tag_lower]


def build_goal(
    description: str,
    goal_type: str,
    provenance: dict,
    source_key: str | None = None,
) -> dict:
    now = utc_now()
    return {
        "goal_id": str(uuid.uuid4()),
        "type": goal_type,
        "description": description.strip(),
        "status": "PENDING",
        "priority": 0.5,
        "provenance": provenance,
        "mandate_id": MANDATE_ID,
        "budget": {"remaining_actions": 1},
        "created_at": to_iso(now),
        "expires_at": to_iso(now + timedelta(days=GOAL_TTL_DAYS)),
        "success_condition": "emit one bounded follow-up receipt",
        "stop_condition": "cancelled, expired, mandate withdrawn, or budget exhausted",
        "trigger_id": None,
        "source_key": source_key,
    }


def add_user_goal(state: dict, goal: str) -> dict:
    if not goal.strip():
        raise ValueError("Goal must not be empty")

    entry = build_goal(
        description=goal,
        goal_type="USER",
        provenance={
            "source": "user",
            "method": "explicit",
            "mandate_id": MANDATE_ID,
        },
    )
    state["goals"].append(entry)
    record_audit(
        state,
        "goal_admitted",
        {"goal_id": entry["goal_id"], "type": "USER"},
    )
    return entry


def list_goals(state: dict) -> list[dict]:
    return state["goals"]


def propose_goal_candidates(state: dict) -> list[dict]:
    tag_counts: dict[str, int] = {}
    for note in state["notes"]:
        tag = (note.get("tag") or "").strip().lower()
        if tag:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1

    existing_keys = {
        goal.get("source_key")
        for goal in state["goals"]
        if goal.get("status") not in {"CANCELLED", "EXPIRED", "FAILED"}
    }
    candidates = []
    for tag, count in sorted(tag_counts.items()):
        source_key = f"recurring-tag:{tag}"
        if count >= 2 and source_key not in existing_keys:
            candidates.append(
                build_goal(
                    description=f"Review recurring topic tagged '{tag}'",
                    goal_type="AUTO",
                    provenance={
                        "source": "persistent_pattern",
                        "method": "repeated_tag",
                        "evidence_count": count,
                        "mandate_id": MANDATE_ID,
                    },
                    source_key=source_key,
                )
            )
    return candidates


def admit_candidates(
    state: dict,
    candidates: list[dict],
    trigger_delay: int,
) -> list[dict]:
    admitted = []
    now = utc_now()
    for candidate in candidates:
        allowed = (
            candidate.get("mandate_id") == MANDATE_ID
            and candidate.get("type") == "AUTO"
            and candidate.get("budget", {}).get("remaining_actions") == 1
            and parse_iso(candidate["expires_at"]) > now
        )
        if not allowed:
            record_audit(
                state,
                "goal_rejected",
                {
                    "source_key": candidate.get("source_key"),
                    "reason": "admission_policy",
                },
            )
            continue

        trigger_id = str(uuid.uuid4())
        candidate["trigger_id"] = trigger_id
        state["goals"].append(candidate)
        state["triggers"].append(
            {
                "trigger_id": trigger_id,
                "type": "TIMER",
                "goal_id": candidate["goal_id"],
                "due_at": to_iso(now + timedelta(seconds=max(0, trigger_delay))),
                "expires_at": candidate["expires_at"],
                "mandate_id": MANDATE_ID,
                "status": "REGISTERED",
            }
        )
        admitted.append(candidate)
        record_audit(
            state,
            "goal_admitted",
            {"goal_id": candidate["goal_id"], "type": "AUTO"},
        )
    return admitted


def cancel_goal(state: dict, goal_id: str) -> bool:
    for goal in state["goals"]:
        if goal.get("goal_id") == goal_id and goal.get("status") not in {
            "COMPLETED",
            "CANCELLED",
            "EXPIRED",
        }:
            goal["status"] = "CANCELLED"
            for trigger in state["triggers"]:
                if (
                    trigger.get("goal_id") == goal_id
                    and trigger.get("status") == "REGISTERED"
                ):
                    trigger["status"] = "REVOKED"
            record_audit(state, "goal_cancelled", {"goal_id": goal_id})
            return True
    return False


def run_due_triggers(state: dict, now: datetime | None = None) -> list[dict]:
    current = now or utc_now()
    apply_retention(state, current)
    goals_by_id = {goal["goal_id"]: goal for goal in state["goals"]}
    receipts = []

    for trigger in state["triggers"]:
        if trigger.get("status") != "REGISTERED":
            continue
        if parse_iso(trigger["due_at"]) > current:
            continue

        goal = goals_by_id.get(trigger.get("goal_id"))
        authorized = (
            trigger.get("mandate_id") == MANDATE_ID
            and goal is not None
            and goal.get("status") in {"PENDING", "ACTIVE", "DEFERRED"}
            and goal.get("mandate_id") == MANDATE_ID
            and parse_iso(goal["expires_at"]) > current
            and goal.get("budget", {}).get("remaining_actions", 0) > 0
        )
        if not authorized:
            trigger["status"] = "REVOKED"
            record_audit(
                state,
                "trigger_rejected",
                {
                    "trigger_id": trigger["trigger_id"],
                    "reason": "reauthorization",
                },
            )
            continue

        goal["status"] = "ACTIVE"
        goal["budget"]["remaining_actions"] -= 1
        receipt = {
            "trigger_id": trigger["trigger_id"],
            "goal_id": goal["goal_id"],
            "description": goal["description"],
            "status": "COMPLETED",
        }
        receipts.append(receipt)
        goal["status"] = "COMPLETED"
        trigger["status"] = "FIRED"
        record_audit(state, "trigger_fired", receipt)

    return receipts


def build_client() -> OpenAI:
    endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
    api_key = os.environ.get("AZURE_OPENAI_API_KEY")

    if not endpoint or not api_key:
        raise RuntimeError(
            "Missing AZURE_OPENAI_ENDPOINT or AZURE_OPENAI_API_KEY. "
            "Set them before running."
        )

    return OpenAI(
        base_url=f"{endpoint.rstrip('/')}/openai/v1/",
        api_key=api_key,
    )


def execute_tool_call(tool_call: object, state: dict, trigger_delay: int) -> str:
    name = tool_call.function.name
    try:
        args = json.loads(tool_call.function.arguments or "{}")
    except json.JSONDecodeError:
        return json.dumps(
            {"status": "failed", "error_code": "invalid_json_arguments"}
        )

    try:
        if name == "search_files":
            query = args.get("query")
            max_results = args.get("max_results", 20)
            if not isinstance(query, str) or not query.strip():
                raise ValueError("invalid_query")
            if not isinstance(max_results, int) or isinstance(max_results, bool):
                raise ValueError("invalid_max_results")
            payload = {
                "results": search_files(
                    query=query.strip(),
                    max_results=max(1, min(50, max_results)),
                )
            }
        elif name == "add_note":
            note = args.get("note")
            tag = args.get("tag")
            if not isinstance(note, str):
                raise ValueError("invalid_note")
            if tag is not None and not isinstance(tag, str):
                raise ValueError("invalid_tag")
            entry = add_note(state, note=note, tag=tag)
            candidates = propose_goal_candidates(state)
            admitted = admit_candidates(state, candidates, trigger_delay)
            payload = {
                "note": entry,
                "autonomous_goals_admitted": [
                    {
                        "goal_id": goal["goal_id"],
                        "description": goal["description"],
                        "trigger_id": goal["trigger_id"],
                    }
                    for goal in admitted
                ],
            }
        elif name == "list_notes":
            tag = args.get("tag")
            if tag is not None and not isinstance(tag, str):
                raise ValueError("invalid_tag")
            payload = {"notes": list_notes(state, tag=tag)}
        elif name == "add_goal":
            goal = args.get("goal")
            if not isinstance(goal, str):
                raise ValueError("invalid_goal")
            payload = {"goal": add_user_goal(state, goal=goal)}
        elif name == "list_goals":
            payload = {"goals": list_goals(state)}
        elif name == "cancel_goal":
            goal_id = args.get("goal_id")
            if not isinstance(goal_id, str) or not goal_id.strip():
                raise ValueError("invalid_goal_id")
            payload = {"cancelled": cancel_goal(state, goal_id.strip())}
        else:
            return json.dumps({"status": "failed", "error_code": "unknown_tool"})
    except (OSError, ValueError) as error:
        return json.dumps(
            {"status": "failed", "error_code": str(error) or "tool_failed"}
        )

    apply_retention(state)
    return json.dumps({"status": "succeeded", **payload})


def run_episode(
    client: OpenAI,
    deployment: str,
    user_input: str,
    host_context: list[dict],
    state: dict,
    state_path: str,
    tools: list[dict],
    trigger_delay: int,
) -> str:
    system_message = (
        "You are a bounded L2 Autonomous Agent with governed persistent state. "
        "Use only allowlisted tools. Persistent patterns may admit a bounded AUTO goal "
        "under the local mandate. Report goal and trigger receipts truthfully. "
        "Do not modify files, expand authority, or claim actions you did not take."
    )
    messages: list = [
        {"role": "system", "content": system_message},
        *host_context[-MAX_CONTEXT_MESSAGES:],
        {"role": "user", "content": user_input},
    ]

    for _ in range(MAX_TOOL_ROUNDS):
        response = client.chat.completions.create(
            model=deployment,
            messages=messages,
            tools=tools,
            tool_choice="auto",
        )
        assistant_message = response.choices[0].message
        messages.append(assistant_message)

        if not assistant_message.tool_calls:
            return assistant_message.content or ""

        for tool_call in assistant_message.tool_calls:
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": execute_tool_call(tool_call, state, trigger_delay),
                }
            )
        save_state(state_path, state)

    return "I stopped because the tool-call budget was exhausted."


def main() -> None:
    parser = argparse.ArgumentParser(description="Bounded L2 Autonomous Agent sample")
    parser.add_argument(
        "--run-due",
        action="store_true",
        help="Process due autonomous triggers once and exit (scheduler entry point).",
    )
    args = parser.parse_args()

    state_path = os.environ.get("L2_STATE_PATH", ".l2_state.json")
    state = load_state(state_path)
    apply_retention(state)

    if args.run_due:
        receipts = run_due_triggers(state)
        save_state(state_path, state)
        print(json.dumps({"status": "succeeded", "receipts": receipts}, indent=2))
        return

    deployment = os.environ.get("AZURE_OPENAI_DEPLOYMENT")
    if not deployment:
        raise RuntimeError("Missing AZURE_OPENAI_DEPLOYMENT.")

    client = build_client()
    trigger_delay = int(os.environ.get("L2_TRIGGER_DELAY_SECONDS", "60"))

    tools = [
        {
            "type": "function",
            "function": {
                "name": "search_files",
                "description": "Search for files in the current repo by name or glob pattern.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Substring or glob pattern, e.g. 'README' or '*.md'",
                        },
                        "max_results": {
                            "type": "integer",
                            "description": "Maximum results to return (1-50).",
                            "minimum": 1,
                            "maximum": 50,
                        },
                    },
                    "required": ["query"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "add_note",
                "description": "Store a note in persistent state.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "note": {
                            "type": "string",
                            "description": "The note to store.",
                        },
                        "tag": {
                            "type": "string",
                            "description": "Optional tag for filtering.",
                        },
                    },
                    "required": ["note"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "list_notes",
                "description": "List stored notes (optionally by tag).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tag": {
                            "type": "string",
                            "description": "Optional tag to filter notes.",
                        }
                    },
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "add_goal",
                "description": "Add a goal to persistent state.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "goal": {
                            "type": "string",
                            "description": "The goal to add.",
                        }
                    },
                    "required": ["goal"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "list_goals",
                "description": "List current goals.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "cancel_goal",
                "description": "Cancel a goal and revoke its registered triggers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "goal_id": {
                            "type": "string",
                            "description": "The goal ID to cancel.",
                        }
                    },
                    "required": ["goal_id"],
                },
            },
        },
    ]

    due_receipts = run_due_triggers(state)
    if due_receipts:
        print(json.dumps({"autonomous_trigger_receipts": due_receipts}, indent=2))
        save_state(state_path, state)

    host_context: list[dict] = []

    print("L2 Autonomous Agent (Azure OpenAI). Type 'exit' to quit.")
    while True:
        user_input = input("> ").strip()
        if user_input.lower() in {"exit", "quit"}:
            break
        if not user_input:
            continue

        answer = run_episode(
            client,
            deployment,
            user_input,
            host_context,
            state,
            state_path,
            tools,
            trigger_delay,
        )
        save_state(state_path, state)
        print(answer)

        host_context.extend(
            [
                {"role": "user", "content": user_input},
                {"role": "assistant", "content": answer},
            ]
        )
        host_context = host_context[-MAX_CONTEXT_MESSAGES:]


if __name__ == "__main__":
    main()
