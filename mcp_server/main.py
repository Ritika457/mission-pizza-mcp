from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI(title="Mission Pizza MCP Server")

# ----  Data ----
MENU = [
    {"name": "Margherita", "sizes": ["small", "medium", "large"]},
    {"name": "Farmhouse", "sizes": ["medium", "large"]}
]

ORDERS = {}


class OrderRequest(BaseModel):
    pizza: str
    size: str


@app.get("/menu")
def get_menu():
    """
    MCP Tool: get_menu
    """
    return MENU


@app.post("/order")
def place_order(order: OrderRequest):
    """
    MCP Tool: place_order
    """
    order_id = str(uuid.uuid4())
    ORDERS[order_id] = {
        "pizza": order.pizza,
        "size": order.size,
        "status": "Preparing",
        "eta": "30 minutes"
    }

    return {
        "order_id": order_id,
        "eta": "30 minutes"
    }


@app.get("/order/{order_id}")
def track_order(order_id: str):
    """
    MCP Tool: track_order
    """
    return ORDERS.get(order_id, {"error": "Order not found"})
