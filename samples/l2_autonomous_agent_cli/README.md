# L2 Autonomous Agent (Azure OpenAI, CLI)

A minimal Level 2 example that adds persistent state (notes + goals) on top of the L1 tool pipeline. State is stored in a local JSON file to demonstrate a simple world model and goal system.

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
   # Optional: override API version
   export AZURE_OPENAI_API_VERSION="2024-02-15-preview"
   # Optional: limit search root
   export L2_SEARCH_ROOT="/path/to/search"
   # Optional: persistent state file path
   export L2_STATE_PATH=".l2_state.json"
   ```

## Run

```bash
python app.py
```

## Example Prompts

- "Remember this note: Use MSCP L2 for stateful agents."
- "Remember this note with tag research: Review Level 2 limitations."
- "List my notes."
- "List my notes tagged research."
- "Set a goal: Track all Level 2 changes."
- "Set a goal: Summarize Level 2 docs this week."
- "List my goals."
- "Find files matching Level_*.md"
