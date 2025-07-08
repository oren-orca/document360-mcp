# Document360 MCP

A Model Context Protocol (MCP) server for Document360, enabling programmatic access to your Document360 knowledge base via standardized tools. This project provides tools for listing project versions, searching articles, and retrieving article content using the official Document360 API.

## Features

- List all project versions in your Document360 workspace
- Search for articles within a specific project version and language
- Retrieve full article content by article ID and language
- Fully documented tool arguments using Pydantic's `Field`
- Ready for use with the MCP Inspector for interactive testing

## Usage

### Installing in VSCode

In Settings, Mcp, edit the settings.json and add:
```bash
{
    "mcp": {
        "inputs": [],
        "servers": {
            "document360": {
                "command": "uvx",
                "args": [
                    "--from",
                    "git+https://github.com/oren-orca/document360-mcp.git",
                    "document360-mcp",
                ],
                "env": {
                    "DOCUMENT360_API_TOKEN": "<TOKEN HERE>",
                }
            },
        }
    },
}
```

## Requirements

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) package manager
- A valid Document360 API token (see below)

## Setup

1. **Clone the repository**
2. **Install dependencies**:
   ```bash
   uv add "mcp[cli]" python-dotenv httpx
   ```
3. **Create a `.env` file** in the project root:
   ```env
   DOCUMENT360_API_TOKEN=your_document360_api_token_here
   ```
   - You can generate an API token in Document360 under Settings → Knowledge base portal → API tokens.

### Running the MCP Server

```bash
uv run python main.py
```

### Using the MCP Inspector

Start the server in development mode with the Inspector:

```bash
uv run mcp dev main.py
```
