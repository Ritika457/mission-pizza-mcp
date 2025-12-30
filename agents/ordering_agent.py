import requests

MCP_SERVER = "http://localhost:8000"


def ordering_agent(user_input: str):
    """
    Simulates an AI agent that understands intent
    and uses MCP tools to place an order.
    """
    menu = requests.get(f"{MCP_SERVER}/menu").json()

    pizza = "Margherita"
    size = "large"

    response = requests.post(
        f"{MCP_SERVER}/order",
        json={"pizza": pizza, "size": size}
    )

    return response.json()


if __name__ == "__main__":
    result = ordering_agent("I want a large Margherita")
    print("Order Agent Result:")
    print(result)
