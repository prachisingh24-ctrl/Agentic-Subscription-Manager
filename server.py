from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agent import agent_decisions
from payments import execute_payment
import json
import os

app = FastAPI()

# Enable CORS so frontend (port 5500) can talk to backend (port 8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://127.0.0.1:5500"] for stricter control
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/decisions")
def get_decisions():
    return {"decisions": agent_decisions()}

@app.post("/pay")
def pay(service: str, action: str):
    if action.lower() == "cancel":
        amount = 0
    elif action.lower() == "switch":
        amount = 5
    else:  # Keep
        amount = 10

    execute_payment(service, amount)

    log_entry = {
        "service": service,
        "action": action,
        "amount": amount,
        "status": "Payment executed"
    }

    if os.path.exists("transactions.json"):
        with open("transactions.json", "r") as f:
            transactions = json.load(f)
    else:
        transactions = []

    transactions.append(log_entry)

    with open("transactions.json", "w") as f:
        json.dump(transactions, f, indent=2)

    return log_entry

@app.get("/transactions")
def get_transactions():
    if os.path.exists("transactions.json"):
        with open("transactions.json", "r") as f:
            transactions = json.load(f)
    else:
        transactions = []
    return {"transactions": transactions}