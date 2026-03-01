import fnmatch
import json
import os
from datetime import datetime

from openai import AzureOpenAI


def search_files(query: str, max_results: int = 20) -> list[str]:
    """Search for files in the current repo by name or simple glob."""
    root = os.path.abspath(os.getenv("L2_SEARCH_ROOT", "."))
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

            results.append(os.path.join(dirpath, filename))
            if len(results) >= max_results:
                return results

    return results


def load_state(path: str) -> dict:
    if not os.path.exists(path):
        return {"notes": [], "goals": []}

    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def save_state(path: str, state: dict) -> None:
    with open(path, "w", encoding="utf-8") as handle:
        json.dump(state, handle, indent=2)


def add_note(state: dict, note: str, tag: str | None = None) -> dict:
    entry = {
        "note": note.strip(),
        "tag": tag.strip() if tag else None,
        "created_at": datetime.utcnow().isoformat() + "Z",
    }
    state["notes"].append(entry)
    return entry


def list_notes(state: dict, tag: str | None = None) -> list[dict]:
    if not tag:
        return state["notes"]
    tag_lower = tag.lower()
    return [item for item in state["notes"] if (item.get("tag") or "").lower() == tag_lower]


def add_goal(state: dict, goal: str) -> dict:
    entry = {
        "goal": goal.strip(),
        "created_at": datetime.utcnow().isoformat() + "Z",
    }
    state["goals"].append(entry)
    return entry


def list_goals(state: dict) -> list[dict]:
    return state["goals"]


def build_client() -> AzureOpenAI:
    endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
    api_key = os.environ.get("AZURE_OPENAI_API_KEY")
    api_version = os.environ.get("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")

    if not endpoint or not api_key:
        raise RuntimeError(
            "Missing AZURE_OPENAI_ENDPOINT or AZURE_OPENAI_API_KEY. "
            "Set them before running."
        )

    return AzureOpenAI(
        azure_endpoint=endpoint,
        api_key=api_key,
        api_version=api_version,
    )


def main() -> None:
    deployment = os.environ.get("AZURE_OPENAI_DEPLOYMENT")
    if not deployment:
        raise RuntimeError("Missing AZURE_OPENAI_DEPLOYMENT.")

    state_path = os.environ.get("L2_STATE_PATH", ".l2_state.json")
    client = build_client()

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
    ]

    system_message = (
        "You are an L2 Autonomous Agent with persistent state. "
        "Use tools to store notes and goals, and to search files. "
        "Do not modify files or claim actions you did not take."
    )

    messages: list[dict] = [{"role": "system", "content": system_message}]

    print("L2 Autonomous Agent (Azure OpenAI). Type 'exit' to quit.")
    while True:
        user_input = input("> ").strip()
        if user_input.lower() in {"exit", "quit"}:
            break
        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model=deployment,
            messages=messages,
            tools=tools,
            tool_choice="auto",
        )

        assistant_message = response.choices[0].message
        messages.append(assistant_message)

        if assistant_message.tool_calls:
            state = load_state(state_path)

            for tool_call in assistant_message.tool_calls:
                name = tool_call.function.name
                args = json.loads(tool_call.function.arguments or "{}")

                if name == "search_files":
                    query = args.get("query", "")
                    max_results = int(args.get("max_results", 20))
                    max_results = max(1, min(50, max_results))
                    results = search_files(query=query, max_results=max_results)
                    payload = {"results": results}
                elif name == "add_note":
                    note = args.get("note", "")
                    tag = args.get("tag")
                    payload = {"note": add_note(state, note=note, tag=tag)}
                elif name == "list_notes":
                    tag = args.get("tag")
                    payload = {"notes": list_notes(state, tag=tag)}
                elif name == "add_goal":
                    goal = args.get("goal", "")
                    payload = {"goal": add_goal(state, goal=goal)}
                elif name == "list_goals":
                    payload = {"goals": list_goals(state)}
                else:
                    payload = {"error": f"Unknown tool: {name}"}

                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": json.dumps(payload),
                    }
                )

            save_state(state_path, state)

            follow_up = client.chat.completions.create(
                model=deployment,
                messages=messages,
            )
            print(follow_up.choices[0].message.content or "")
            messages.append(follow_up.choices[0].message)
        else:
            print(assistant_message.content or "")


if __name__ == "__main__":
    main()
