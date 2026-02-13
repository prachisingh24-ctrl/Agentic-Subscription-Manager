import json

DATA_FILE = "../data/subscriptions.json"


def get_user_subscriptions():
    subscriptions = []

    print("\nEnter your subscriptions.")
    print("Type 'done' as name when finished.\n")

    while True:
        name = input("Subscription name: ")

        if name.lower() == "done":
            break

        cost = float(input("Monthly cost (₹): "))
        usage = float(input("Usage hours last month: "))
        provider = input("Provider name: ")

        subscriptions.append({
            "name": name,
            "monthly_cost": cost,
            "usage_hours_last_month": usage,
            "provider": provider
        })

        print("Subscription added.\n")

    return subscriptions


def save_subscriptions(subscriptions):
    with open(DATA_FILE, "w") as f:
        json.dump(subscriptions, f, indent=4)
