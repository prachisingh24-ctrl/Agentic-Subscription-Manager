import json
import random

# ----------------------------------------
# Agentic Subscription Manager - Decision Logic
# ----------------------------------------

def load_subscriptions(file="data.json"):
    """Load subscriptions from a JSON file."""
    with open(file, "r") as f:
        return json.load(f)

def predict_usage(hours):
    """Predict usage hours with a small random variation, never below 0."""
    predicted = hours + random.randint(-3, 3)
    return max(predicted, 0)  # ensures no negative values

def evaluate_subscription(sub):
    """Evaluate a single subscription and recommend an action."""
    predicted = predict_usage(sub.get("usage_hours", 0))

    if predicted < 5:
        action = "Cancel"
        detail = f"Predicted usage {predicted}h"
    elif sub.get("plan", "").lower() == "premium" and predicted < 20:
        action = "Switch"
        detail = f"Predicted usage {predicted}h"
    else:
        action = "Keep"
        detail = f"Predicted usage {predicted}h"

    return {
        "service": sub.get("name", "Unknown"),
        "plan": sub.get("plan", "Unknown"),
        "credits": sub.get("credits", 0),
        "action": action,
        "detail": detail
    }

def agent_decisions():
    """Return a list of decisions for all subscriptions."""
    data = load_subscriptions()
    subs = data.get("subscriptions", [])
    return [evaluate_subscription(sub) for sub in subs]

if __name__ == "__main__":
    print("Agent Decisions:")
    for decision in agent_decisions():
        print(decision)