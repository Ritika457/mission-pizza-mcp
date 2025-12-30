from ordering_agent import ordering_agent
from scheduling_agent import scheduling_agent

def main():
    print("User: Order a large Margherita")

    order_result = ordering_agent("Order a large Margherita")
    print("Ordering Agent Output:", order_result)

    schedule_result = scheduling_agent(
        order_result["order_id"],
        order_result["eta"]
    )
    print("Scheduling Agent Output:", schedule_result)

    print("\n✅ Order and delivery successfully coordinated")

if __name__ == "__main__":
    main()
