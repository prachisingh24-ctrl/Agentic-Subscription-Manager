import random


def negotiate_with_provider(subscription):
    name = subscription["name"]
    original_cost = subscription["cost"]

    print(f"[AGENT] Negotiating with {name} provider...")

    # Simulated negotiation
    discount = random.randint(10, 40)
    new_price = original_cost * (1 - discount / 100)

    print(f"[AGENT] {discount}% discount received.")

    return round(new_price, 2)
