import os
import dotenv

import httpx
from mcp.server.fastmcp import FastMCP
from pydantic import Field

dotenv.load_dotenv()

DOCUMENT360_API_TOKEN = os.environ.get("DOCUMENT360_API_TOKEN")
if not DOCUMENT360_API_TOKEN:
    raise ValueError(
        "DOCUMENT360_API_TOKEN environment variable is not set. "
        "Please create a .env file with your Document360 API token:\n"
        "DOCUMENT360_API_TOKEN=your_token_here\n\n"
        "You can generate an API token in Document360 under Settings → Knowledge base portal → API tokens."
    )
DOCUMENT360_API_URL = "https://apihub.document360.io/v2"

mcp = FastMCP("Document360 MCP")


@mcp.tool()
def list_project_versions() -> dict:
    """List all project versions in Document360."""
    headers = {
        "api_token": DOCUMENT360_API_TOKEN,
        "Content-Type": "application/json",
    }
    url = f"{DOCUMENT360_API_URL}/ProjectVersions"
    response = httpx.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


@mcp.tool()
def search_articles(
    project_version_id: str = Field(
        description="The ID of the project version to search in."
    ),
    lang_code: str = Field(
        default="en", description="The language code for the articles (default: 'en')."
    ),
    search_query: str = Field(
        default="", description="The phrase to search for inside the project version."
    ),
    page: int = Field(
        default=0, description="The page number to retrieve (zero-based)."
    ),
    hits_per_page: int = Field(default=10, description="Number of results per page."),
) -> dict:
    """Search for a phrase inside a project version."""
    headers = {
        "api_token": DOCUMENT360_API_TOKEN,
        "Content-Type": "application/json",
    }
    params = {
        "searchQuery": search_query,
        "page": page,
        "hitsPerPage": hits_per_page,
    }
    url = f"{DOCUMENT360_API_URL}/ProjectVersions/{project_version_id}/{lang_code}"
    response = httpx.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()


@mcp.tool()
def get_article(
    article_id: str = Field(description="The ID of the article to retrieve."),
    lang_code: str = Field(
        default="en", description="The language code for the article (default: 'en')."
    ),
) -> dict:
    """Get an article by ID and language code."""
    headers = {
        "api_token": DOCUMENT360_API_TOKEN,
        "Content-Type": "application/json",
    }
    url = f"{DOCUMENT360_API_URL}/Articles/{article_id}/{lang_code}"
    response = httpx.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def main():
    mcp.run()


if __name__ == "__main__":
    main()
