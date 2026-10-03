import os

from mcp.server import MCPServer
from openiti.helper import funcs

mcp = MCPServer(
    "OpenITI",
    instructions="Access and search texts from the OpenITI corpus."
)


@mcp.tool()
def read_openiti_text(url: str) -> str:
    """Read an OpenITI text from a URL."""
    try:
        return funcs.read_text(url)
    except Exception as e:
        return f"Error reading OpenITI text: {e}"


@mcp.tool()
def read_openiti_header(url: str) -> str:
    """Read metadata/header from an OpenITI text."""
    try:
        return str(funcs.read_header(url))
    except Exception as e:
        return f"Error reading OpenITI header: {e}"


@mcp.tool()
def get_sections(url: str) -> str:
    """Return section titles found in an OpenITI text."""
    try:
        sections = funcs.get_sections(url)
        return "\n".join(str(section) for section in sections)
    except Exception as e:
        return f"Error getting sections: {e}"


@mcp.tool()
def find_section_title(url: str, position: int) -> str:
    """Find the section title at a character position."""
    try:
        return str(funcs.find_section_title(url, position))
    except Exception as e:
        return f"Error finding section: {e}"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "10000"))

    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=port
    )
