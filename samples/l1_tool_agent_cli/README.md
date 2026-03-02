# L1 Tool Agent (Azure OpenAI, CLI)

A minimal L1 Tool Agent example that uses Azure OpenAI tool calling to search local files by name. It follows the L1 pattern: deterministic tool invocation with no self-modification.

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
   export L1_SEARCH_ROOT="/path/to/search"
   ```

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
