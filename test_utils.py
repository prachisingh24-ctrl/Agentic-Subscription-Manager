import unittest
import uuid
import tempfile
import os
from utils import load_transactions, save_transaction

class TestUtils(unittest.TestCase):
    def test_load_transactions_empty(self):
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp_file = tmp.name
        os.remove(tmp_file)  # ensure it's gone
        self.assertEqual(load_transactions(tmp_file), [])

    def test_save_and_load_transaction(self):
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp_file = tmp.name
        entry = {
            "receipt_id": str(uuid.uuid4()),
            "service": "Netflix",
            "action": "Keep",
            "amount": 10,
            "status": "Payment executed",
            "reason": "Usage sufficient, keep current plan",
            "policy": "Spend cap enforced",
            "timestamp": "2026-02-14 13:10:00"
        }
        save_transaction(entry, tmp_file)
        transactions = load_transactions(tmp_file)
        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["service"], "Netflix")
        os.remove(tmp_file)

    def test_multiple_transactions(self):
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp_file = tmp.name
        entry1 = {"receipt_id": str(uuid.uuid4()), "service": "Spotify", "action": "Switch", "amount": 5}
        entry2 = {"receipt_id": str(uuid.uuid4()), "service": "YouTube", "action": "Cancel", "amount": 0}
        save_transaction(entry1, tmp_file)
        save_transaction(entry2, tmp_file)
        transactions = load_transactions(tmp_file)
        self.assertEqual(len(transactions), 2)
        self.assertEqual(transactions[0]["service"], "Spotify")
        self.assertEqual(transactions[1]["service"], "YouTube")
        os.remove(tmp_file)

if __name__ == "__main__":
    unittest.main()