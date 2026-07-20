# L2 Autonomous Agent (Azure OpenAI, CLI)

A minimal Level 2 example with governed persistent state, deterministic autonomous goal candidates, external admission policy, finite budgets, expiry, cancellation, and revocable timer triggers.

The sample demonstrates the three Level 2 distinctions from Level 1:

- **Causal persistence**: notes and goals are retrieved from a versioned local state file and influence later events.
- **Autonomous goal origination**: two notes with the same tag produce one bounded AUTO goal candidate without a direct `add_goal` request.
- **Authorized continuation**: admission registers a timer that a scheduler can execute through `--run-due`; mandate, status, expiry, and budget are checked again before execution.

This remains a deliberately narrow local example. AUTO goals can only emit one follow-up receipt; they cannot modify files, expand tool authority, or acquire resources. State writes are atomic, records expire, goals can be cancelled, and trigger/admission decisions are audited.

The JSON store is a single-writer demonstration. Serialize interactive and scheduler processes when using the same `L2_STATE_PATH`; production deployments should use a transactional store with concurrency control.

## Prerequisites

- Python 3.10+
- An Azure OpenAI resource with a chat model deployment that supports tool calling

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set environment variables (required unless noted):
   ```bash
   export AZURE_OPENAI_ENDPOINT="https://<your-resource>.openai.azure.com"
   export AZURE_OPENAI_API_KEY="<your-key>"
   export AZURE_OPENAI_DEPLOYMENT="<your-deployment-name>"
   # Optional: limit search root
   export L2_SEARCH_ROOT="/path/to/search"
   # Optional: persistent state file path
   export L2_STATE_PATH=".l2_state.json"
   # Optional: delay before an admitted AUTO goal becomes due
   export L2_TRIGGER_DELAY_SECONDS="60"
   ```

The sample uses the [Azure OpenAI v1 GA API](https://learn.microsoft.com/azure/foundry/openai/api-version-lifecycle#code-changes), which does not require an `api-version` parameter. The environment variable API key keeps the local example small. For deployed applications, Microsoft recommends Microsoft Entra ID authentication; if a key is required, store it in Azure Key Vault rather than application code.

## Run

```bash
python app.py
```

To process due continuation triggers from cron, a task scheduler, or another authorized supervisor without Azure OpenAI credentials:

```bash
python app.py --run-due
```

The command executes one bounded scheduler event and exits. It does not run a daemon or create its own operating-system schedule.

## Example Prompts

- "Remember this note with tag research: Review Level 2 state governance."
- "Remember this note with tag research: Verify Level 2 trigger cancellation."
- "List my notes."
- "List my notes tagged research."
- "Set a goal: Track all Level 2 changes."
- "List my goals."
- "Cancel goal <goal-id>."
- "Find files matching Level_*.md"

After the second `research` note, inspect `list_goals`: one AUTO goal with provenance, a one-action budget, expiry, stop condition, and trigger ID should be present. Run `python app.py --run-due` after the delay to process its continuation event.
