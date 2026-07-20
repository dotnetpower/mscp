# L1 Tool Agent (Azure OpenAI, CLI)

A minimal L1 Tool Agent example that uses Azure OpenAI tool calling to search local files by name. Each user request starts a bounded execution episode. The CLI host may pass an explicit recent transcript into that episode, but the agent owns no persistent world, self, or goal state and cannot initiate work on its own.

The sample also demonstrates several Level 1 safety boundaries:

- one allowlisted, read-only tool
- a maximum of four tool-call rounds per request
- typed success and error results for every tool call
- relative result paths constrained to `L1_SEARCH_ROOT`
- no file modification or autonomous continuation

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
   export L1_SEARCH_ROOT="/path/to/search"
   ```

The sample uses the [Azure OpenAI v1 GA API](https://learn.microsoft.com/azure/foundry/openai/api-version-lifecycle#code-changes), which does not require an `api-version` parameter. The environment variable API key keeps the local example small. For deployed applications, Microsoft recommends Microsoft Entra ID authentication; if a key is required, store it in Azure Key Vault rather than application code.

## Run

```bash
python app.py
```

## Example Prompts

- "Find all markdown files."
- "Search for README files."
- "List files matching Level_*.md"
- "Find files ending with .ko.md"
- "Search for mkdocs.yml"
- "List files matching docs/**/Level_*.md"
- "Find any files with 'katex' in the name"
- "Show up to 5 files matching *.png"
