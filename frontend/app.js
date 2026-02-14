const container = document.getElementById("subscriptions");
const historyContainer = document.getElementById("transaction-list");

document.querySelectorAll(".tab-btn").forEach(btn => {
  btn.addEventListener("click", () => {
    document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
    document.querySelectorAll(".tab-content").forEach(c => c.classList.remove("active"));
    btn.classList.add("active");
    document.getElementById(btn.dataset.tab).classList.add("active");
  });
});

fetch("http://127.0.0.1:8000/decisions")
  .then(res => res.json())
  .then(data => {
    const decisions = data.decisions;
    decisions.forEach(d => {
      const card = document.createElement("div");
      card.classList.add("card", d.action.toLowerCase());
      card.innerHTML = `
        <div class="card-inner">
          <div class="card-front">
            <h2>${d.service}</h2>
            <p>${d.action}</p>
            <p>${d.detail}</p>
            <p><em>${d.reason}</em></p>
          </div>
          <div class="card-back">
            <h3>Details</h3>
            <p>Plan: ${d.plan}</p>
            <p>Credits: ${d.credits}</p>
            <button class="btn">Confirm ${d.action}</button>
          </div>
        </div>
      `;
      card.querySelector(".btn").addEventListener("click", () => {
        fetch("http://127.0.0.1:8000/pay", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ service: d.service, action: d.action })
        })
        .then(res => res.json())
        .then(result => {
          alert(`${result.service}: ${result.action} confirmed! Payment = ${result.amount}`);
          loadTransactions();
        })
        .catch(err => {
          console.error("Payment error:", err);
          alert("Payment failed!");
        });
      });
      container.appendChild(card);
    });
  })
  .catch(err => {
    console.error("Error fetching decisions:", err);
    container.innerHTML = "<p>Failed to load decisions.</p>";
  });

function loadTransactions() {
  historyContainer.innerHTML = "";
  fetch("http://127.0.0.1:8000/transactions")
    .then(res => res.json())
    .then(data => {
      const transactions = data.transactions;
      if (transactions.length === 0) {
        historyContainer.innerHTML = "<p>No transactions yet.</p>";
        return;
      }
      const totalAmount = transactions.reduce((sum, t) => sum + (t.amount || 0), 0);
      const totalCount = transactions.length;
      const summary = document.createElement("div");
      summary.classList.add("summary-bar");
      summary.innerHTML = `Total Transactions: ${totalCount} | Total Payments: ${totalAmount}`;
      historyContainer.appendChild(summary);
      transactions.forEach(t => {
        const entry = document.createElement("div");
        entry.classList.add("transaction", t.action.toLowerCase());
        entry.innerHTML = `
          <p><strong>${t.service}</strong> → ${t.action}</p>
          <p>Amount: ${t.amount}</p>
          <p>Status: ${t.status}</p>
          <p>Reason: ${t.reason}</p>
          <p>Policy: ${t.policy}</p>
          <p>Receipt ID: ${t.receipt_id}</p>
          <p class="timestamp"><em>Logged at: ${t.timestamp}</em></p>
        `;
        entry.style.opacity = 0;
        historyContainer.appendChild(entry);
        setTimeout(() => {
          entry.style.transition = "opacity 0.5s ease";
          entry.style.opacity = 1;
        }, 50);
      });
      document.querySelectorAll(".filter-btn").forEach(btn => {
        btn.onclick = () => {
          document.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
          btn.classList.add("active");
          const filter = btn.dataset.filter;
          document.querySelectorAll(".transaction").forEach(tr => {
            if (filter === "all" || tr.classList.contains(filter)) {
              tr.style.display = "block";
            } else {
              tr.style.display = "none";
            }
          });
        };
      });
    })
    .catch(err => {
      console.error("Error fetching transactions:", err);
      historyContainer.innerHTML = "<p>Failed to load transactions.</p>";
    });
}

loadTransactions();
setInterval(loadTransactions, 10000);