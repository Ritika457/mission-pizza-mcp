def scheduling_agent(order_id: str, eta: str):
    """
    Simulates a second agent coordinating delivery.
    """

    return {
        "order_id": order_id,
        "delivery_time": "Now + 30 minutes",
        "calendar_event": "Pizza Delivery Scheduled"
    }


if __name__ == "__main__":
    demo = scheduling_agent("demo-id", "30 minutes")
    print(demo)
