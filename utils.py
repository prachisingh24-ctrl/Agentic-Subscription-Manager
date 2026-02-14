import json
import os

def load_transactions(file="transactions.json"):
    """Load transactions from a JSON file."""
    if os.path.exists(file):
        with open(file, "r") as f:
            return json.load(f)
    return []

def save_transaction(entry, file="transactions.json"):
    """Append a transaction entry to the JSON file."""
    transactions = load_transactions(file)
    transactions.append(entry)
    with open(file, "w") as f:
        json.dump(transactions, f, indent=2)