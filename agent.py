import json
from colorama import Fore, Style
from payments import execute_payment
import random

<<<<<<< HEAD

=======
# Load subscriptions
>>>>>>> master
with open("data.json", "r") as f:
    subscriptions = json.load(f)

def predict_usage(hours):
    import random
    predicted = hours + random.randint(-3, 3)
<<<<<<< HEAD
    return max(predicted, 0)
=======
    return max(predicted, 0)  # ensures no negative values
>>>>>>> master

def check_subscriptions(subs):
    decisions = []
    for sub in subs:
        predicted = predict_usage(sub["usage_hours"])
        if predicted < 5:
            decisions.append(f"Cancel {sub['name']} (predicted usage {predicted}h)")
            execute_payment(sub["name"], 0)  # no payment
        elif sub["plan"] == "premium" and predicted < 20:
            decisions.append(f"Switch {sub['name']} to basic plan (predicted {predicted}h)")
            execute_payment(sub["name"], 5)  # mock cheaper payment
        else:
            decisions.append(f"Keep {sub['name']} active (predicted {predicted}h)")
            execute_payment(sub["name"], 10)  # mock payment
    return decisions

actions = check_subscriptions(subscriptions)

print("Agent Decisions:")
for action in actions:
    if "Cancel" in action:
        print(Fore.RED + " - " + action + Style.RESET_ALL)
    elif "Switch" in action:
        print(Fore.YELLOW + " - " + action + Style.RESET_ALL)
    elif "Keep" in action:
        print(Fore.GREEN + " - " + action + Style.RESET_ALL)
    else:
<<<<<<< HEAD
        print(" - " + action)
=======
        print(" - " + action)  # fallback, plain text
>>>>>>> master
