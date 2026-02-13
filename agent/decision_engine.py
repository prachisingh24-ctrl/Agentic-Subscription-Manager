def analyze_subscriptions(data):
    recommendations = []

    for sub in data:
        usage = sub["usage_hours_last_month"]

        if usage == 0:
            action = "cancel"
        elif usage < 5:
            action = "negotiate"
        else:
            action = "keep"

        recommendations.append({
            "name": sub["name"],
            "provider": sub["provider"],
            "cost": sub["monthly_cost"],
            "usage": usage,
            "action": action
        })

    return recommendations
