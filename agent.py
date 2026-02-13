# ----------------------------------------
# AI Subscription Agent (Interactive)
# ----------------------------------------

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

        subscriptions.append({
            "name": name,
            "monthly_cost": cost,
            "usage_hours_last_month": usage
        })

        print("Subscription added.\n")

    return subscriptions


# -------------------------------
# Agent logic
# -------------------------------
def analyze_subscriptions(data):
    recommendations = []

    for sub in data:
        usage = sub["usage_hours_last_month"]
        cost = sub["monthly_cost"]
        name = sub["name"]

        if usage == 0:
            action = "Cancel"
        elif usage < 5:
            action = "Consider Downgrade"
        else:
            action = "Keep"

        recommendations.append({
            "name": name,
            "cost": cost,
            "usage": usage,
            "action": action
        })

    return recommendations


# -------------------------------
# Simulated execution
# -------------------------------
def execute_actions(recommendations):
    for rec in recommendations:
        if rec["action"] == "Cancel":
            print(f"❌ Cancelling {rec['name']} subscription...")
        elif rec["action"] == "Consider Downgrade":
            print(f"⚠️ Suggest downgrading {rec['name']}.")
        else:
            print(f"✅ Keeping {rec['name']}.")


# -------------------------------
# Main agent loop
# -------------------------------
def run_agent():
    print("\n--- AI Subscription Agent ---\n")

    subscriptions = get_user_subscriptions()

    if not subscriptions:
        print("No subscriptions entered.")
        return

    recommendations = analyze_subscriptions(subscriptions)

    print("\n--- Recommendations ---\n")
    for rec in recommendations:
        print(
            f"{rec['name']} | "
            f"Cost: ₹{rec['cost']} | "
            f"Usage: {rec['usage']} hrs | "
            f"Action: {rec['action']}"
        )

    print("\n--- Executing Actions ---\n")
    execute_actions(recommendations)


if __name__ == "__main__":
    run_agent()

