# This is structured for real Stripe integration.
# Replace print statements with Stripe API calls.

def cancel_subscription(subscription_name):
    print(f"[PAYMENT] Cancelling subscription: {subscription_name}")


def create_subscription(subscription_name, new_price):
    print(f"[PAYMENT] Creating subscription: {subscription_name}")
    print(f"[PAYMENT] New monthly price: ₹{new_price}")
