from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agent import agent_decisions
from payments import execute_payment
from utils import load_transactions, save_transaction
from datetime import datetime
from uuid import uuid4
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PayRequest(BaseModel):
    service: str
    action: str

@app.get("/decisions")
def get_decisions():
    return {"decisions": agent_decisions()}

@app.post("/pay")
def pay(req: PayRequest):
    service = req.service
    action = req.action

    if action.lower() == "cancel":
        amount = 0
        reason = "User opted to cancel subscription"
    elif action.lower() == "switch":
        amount = 5
        reason = "Agent recommended switching to cheaper plan"
    else:
        amount = 10
        reason = "Usage sufficient, keep current plan"

    monthly_cap = 50
    total_spend = sum(t["amount"] for t in load_transactions())
    if total_spend + amount > monthly_cap:
        log_entry = {
            "receipt_id": str(uuid4()),
            "service": service,
            "action": action,
            "amount": amount,
            "status": "Blocked: Cap exceeded",
            "reason": reason,
            "policy": f"Monthly cap {monthly_cap}",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        save_transaction(log_entry)
        return log_entry

    try:
        execute_payment(service, amount)
        status = "Payment executed"
    except Exception:
        try:
            execute_payment(service, amount)
            status = "Payment executed after retry"
        except Exception:
            status = "Fallback: Payment failed, kept plan"
            action = "Keep"

    log_entry = {
        "receipt_id": str(uuid4()),
        "service": service,
        "action": action,
        "amount": amount,
        "status": status,
        "reason": reason,
        "policy": "Spend cap enforced",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    save_transaction(log_entry)
    return log_entry

@app.get("/transactions")
def get_transactions():
    return {"transactions": load_transactions()}

@app.get("/receipts")
def get_receipts():
    return {"receipts": load_transactions()}