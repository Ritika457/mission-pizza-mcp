# mission-pizza-mcp

# 1. Overview

This project demonstrates how traditional OpenAPI-based REST APIs can be automatically transformed into MCP-compatible servers, making them usable by AI agents. A simulated pizza-ordering workflow is used to showcase agent discovery, tool usage, and agent-to-agent coordination.

The goal is not to build a production-grade pizza system, but to show how existing APIs can be exposed to the agentic ecosystem with minimal manual effort.


## Problem Understanding

Most existing APIs are designed for human-driven applications (web/mobile). With AI agents becoming the new interface layer, APIs need to be discoverable and callable as structured tools.

This project explores an automated approach where OpenAPI specifications are programmatically converted into MCP-style tool definitions, allowing AI agents to interact with them directly.


## 3. Architecture Overview

```
OpenAPI Specification
        ↓
OpenAPI → MCP Generator
        ↓
MCP Server (FastAPI)
        ↓
Ordering Agent
        ↓
Scheduling Agent
```

## 4. OpenAPI → MCP Automation

The automation layer reads an OpenAPI JSON file and extracts:

* Endpoint paths
* HTTP methods
* Endpoint summaries

Each endpoint is converted into an MCP-style tool definition containing:

* Tool name
* Description
* HTTP method
* API path

## 5. MCP Server

The MCP server is implemented using FastAPI and exposes the generated tools as callable endpoints.

* Backend logic is mocked using in-memory data structures
* No database is used
* Focus is on protocol compatibility rather than business logic accuracy

This aligns with the assignment requirement to prioritize MCP integration over backend completeness.

## 6. Agent Design

### Ordering Agent

* Accepts natural language user input
* Determines ordering intent
* Calls MCP tools (`get_menu`, `place_order`)
* Returns structured order details such as `order_id` and ETA

The agent logic is intentionally simple to emphasize correct tool usage rather than complex NLP.

### Scheduling Agent

* Receives order details from the ordering agent
* Simulates interaction with an external MCP-enabled scheduling service
* Demonstrates agent-to-agent (A2A) communication using structured data exchange

#7. End-to-End Workflow

1. User requests a pizza order
2. Ordering agent processes intent
3. MCP server places the order and returns confirmation
4. Scheduling agent schedules delivery
5. Final confirmation is returned to the user


## 8. How to Run

```bash
# Start MCP server
uvicorn mcp_server.main:app --reload

# Run end-to-end demo
python agents/run_demo.py
```

## Conclusion

This project demonstrates a practical and extensible approach to making existing APIs AI-ready by bridging OpenAPI and MCP, while highlighting agent coordination and automation principles.
