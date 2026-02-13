import json
from decision_engine import analyze_subscriptions
from provider_agent import negotiate_with_provider
from payment_engine import cancel_subscription, create_subscription
from user_input import get_user_subscriptions, save_subscriptions

DATA_FILE = "../data/subscriptions.json"


def load_subscriptions():
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def run_autonomous_agent():
    print("\n=== Autonomous Subscription Agent ===\n")

    # Step 1: Get user data
    subscriptions = get_user_subscriptions()
    save_subscriptions(subscriptions)

    # Step 2: Analyze
    recommendations = analyze_subscriptions(subscriptions)

    # Step 3: Autonomous execution
    print("\n=== Agent Executing Decisions ===\n")

    for rec in recommendations:
        name = rec["name"]
        action = rec["action"]

        print(f"Processing: {name}")

        if action == "cancel":
            cancel_subscription(name)

        elif action == "negotiate":
            new_price = negotiate_with_provider(rec)
            create_subscription(name, new_price)

        else:
            print(f"[AGENT] Keeping {name} unchanged.")

        print()


if __name__ == "__main__":
    run_autonomous_agent()
