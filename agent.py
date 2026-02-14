import json
import random

def load_subscriptions(file="data.json"):
    with open(file, "r") as f:
        return json.load(f)

def predict_usage(hours):
    predicted = hours + random.randint(-3, 3)
    return max(predicted, 0)

def evaluate_subscription(sub):
    predicted = predict_usage(sub.get("usage_hours", 0))

    if predicted < 5:
        action = "Cancel"
        detail = f"Predicted usage {predicted}h"
        reason = "Low predicted usage, cancel recommended"
    elif sub.get("plan", "").lower() == "premium" and predicted < 20:
        action = "Switch"
        detail = f"Predicted usage {predicted}h"
        reason = "Premium plan underutilized, switch suggested"
    else:
        action = "Keep"
        detail = f"Predicted usage {predicted}h"
        reason = "Usage sufficient, keep current plan"

    return {
        "service": sub.get("name", "Unknown"),
        "plan": sub.get("plan", "Unknown"),
        "credits": sub.get("credits", 0),
        "action": action,
        "detail": detail,
        "reason": reason
    }

def agent_decisions():
    data = load_subscriptions()
    subs = data.get("subscriptions", [])
    return [evaluate_subscription(sub) for sub in subs]

if __name__ == "__main__":
    print("Agent Decisions:")
    for decision in agent_decisions():
        print(decision)