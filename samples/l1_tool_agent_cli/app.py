import json
import os
import fnmatch
from pathlib import Path

from openai import OpenAI


MAX_TOOL_ROUNDS = 4
MAX_CONTEXT_MESSAGES = 20


def search_files(query: str, max_results: int = 20) -> list[str]:
    """Search for files in the current repo by name or simple glob."""
    root = Path(os.getenv("L1_SEARCH_ROOT", ".")).expanduser().resolve()
    if not root.is_dir():
        raise ValueError("L1_SEARCH_ROOT must be an existing directory")

    results: list[str] = []

    # Treat query as a glob if it includes glob chars; otherwise use substring.
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


def execute_tool_call(tool_call: object) -> str:
    """Execute one allowlisted tool call and return a typed JSON result."""
    if tool_call.function.name != "search_files":
        return json.dumps(
            {"status": "failed", "error_code": "unknown_tool"},
        )

    try:
        args = json.loads(tool_call.function.arguments or "{}")
    except json.JSONDecodeError:
        return json.dumps(
            {"status": "failed", "error_code": "invalid_json_arguments"},
        )

    query = args.get("query")
    if not isinstance(query, str) or not query.strip():
        return json.dumps(
            {"status": "failed", "error_code": "invalid_query"},
        )

    max_results = args.get("max_results", 20)
    if not isinstance(max_results, int) or isinstance(max_results, bool):
        return json.dumps(
            {"status": "failed", "error_code": "invalid_max_results"},
        )

    try:
        results = search_files(
            query=query.strip(),
            max_results=max(1, min(50, max_results)),
        )
    except (OSError, ValueError):
        return json.dumps(
            {"status": "failed", "error_code": "search_unavailable"},
        )

    return json.dumps({"status": "succeeded", "results": results})


def run_episode(
    client: OpenAI,
    deployment: str,
    user_input: str,
    host_context: list[dict],
    tools: list[dict],
) -> str:
    """Run one externally triggered episode with a bounded tool-call budget."""
    system_message = (
        "You are an L1 Tool Agent. "
        "Use the allowlisted tool only when needed to answer the current request. "
        "Do not modify files, initiate new work, or claim actions you did not take."
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
                    "content": execute_tool_call(tool_call),
                }
            )

    return "I stopped because the tool-call budget was exhausted."


def main() -> None:
    deployment = os.environ.get("AZURE_OPENAI_DEPLOYMENT")
    if not deployment:
        raise RuntimeError("Missing AZURE_OPENAI_DEPLOYMENT.")

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
        }
    ]

    host_context: list[dict] = []

    print("L1 Tool Agent (Azure OpenAI). Type 'exit' to quit.")
    while True:
        user_input = input("> ").strip()
        if user_input.lower() in {"exit", "quit"}:
            break
        if not user_input:
            continue

        answer = run_episode(client, deployment, user_input, host_context, tools)
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
