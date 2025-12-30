import json
from pathlib import Path


def openapi_to_mcp(openapi_path: str):
    """
    Converts OpenAPI paths into MCP-style tool definitions.
    This is intentionally minimal and extensible.
    """
    with open(openapi_path, "r") as f:
        spec = json.load(f)

    tools = []

    for path, methods in spec.get("paths", {}).items():
        for http_method, meta in methods.items():
            tool_name = f"{http_method}_{path.strip('/').replace('/', '_').replace('{', '').replace('}', '')}"

            tools.append({
                "name": tool_name,
                "description": meta.get("summary", "No description provided"),
                "http_method": http_method.upper(),
                "path": path
            })

    return tools


if __name__ == "__main__":
    openapi_file = Path("../openapi/pizza_openapi.json")
    tools = openapi_to_mcp(openapi_file)

    print("Generated MCP Tools:\n")
    print(json.dumps(tools, indent=2))
