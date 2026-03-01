import json
import os
import fnmatch

from openai import AzureOpenAI


def search_files(query: str, max_results: int = 20) -> list[str]:
    """Search for files in the current repo by name or simple glob."""
    root = os.path.abspath(os.getenv("L1_SEARCH_ROOT", "."))
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

            results.append(os.path.join(dirpath, filename))
            if len(results) >= max_results:
                return results

    return results


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

    system_message = (
        "You are an L1 Tool Agent. "
        "Use tools to answer questions. "
        "Do not modify files or claim actions you did not take."
    )

    messages: list[dict] = [{"role": "system", "content": system_message}]

    print("L1 Tool Agent (Azure OpenAI). Type 'exit' to quit.")
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
            for tool_call in assistant_message.tool_calls:
                if tool_call.function.name == "search_files":
                    args = json.loads(tool_call.function.arguments or "{}")
                    query = args.get("query", "")
                    max_results = int(args.get("max_results", 20))
                    max_results = max(1, min(50, max_results))
                    results = search_files(query=query, max_results=max_results)

                    messages.append(
                        {
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "content": json.dumps({"results": results}),
                        }
                    )

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
