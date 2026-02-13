const container = document.getElementById("subscriptions");
const historyContainer = document.getElementById("transactions"); // div with id="transactions" in your HTML

// Fetch current decisions
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
          </div>
          <div class="card-back">
            <h3>Details</h3>
            <p>Plan: ${d.plan}</p>
            <p>Credits: ${d.credits}</p>
            <button class="btn">Confirm ${d.action}</button>
          </div>
        </div>
      `;

      // Add button interaction with backend call
      card.querySelector(".btn").addEventListener("click", () => {
        fetch("http://127.0.0.1:8000/pay", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ service: d.service, action: d.action })
        })
        .then(res => res.json())
        .then(result => {
          alert(`${result.service}: ${result.action} confirmed! Payment = ${result.amount}`);
          // Refresh history after payment
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

// Function to load transaction history
function loadTransactions() {
  historyContainer.innerHTML = ""; // clear old entries
  fetch("http://127.0.0.1:8000/transactions")
    .then(res => res.json())
    .then(data => {
      const transactions = data.transactions;

      if (transactions.length === 0) {
        historyContainer.innerHTML = "<p>No transactions yet.</p>";
        return;
      }

      // Calculate totals
      const totalAmount = transactions.reduce((sum, t) => sum + (t.amount || 0), 0);
      const totalCount = transactions.length;

      // Add summary bar
      const summary = document.createElement("div");
      summary.classList.add("summary-bar");
      summary.innerHTML = `Total Transactions: ${totalCount} | Total Payments: ${totalAmount}`;
      historyContainer.appendChild(summary);

      // Add each transaction entry
      transactions.forEach(t => {
        const entry = document.createElement("div");
        entry.classList.add("transaction", t.action.toLowerCase());

        entry.innerHTML = `
          <p><strong>${t.service}</strong> → ${t.action}</p>
          <p>Amount: ${t.amount}</p>
          <p>Status: ${t.status}</p>
        `;

        // Animate new entries with fade-in
        entry.style.opacity = 0;
        historyContainer.appendChild(entry);
        setTimeout(() => {
          entry.style.transition = "opacity 0.5s ease";
          entry.style.opacity = 1;
        }, 50);
      });
    })
    .catch(err => {
      console.error("Error fetching transactions:", err);
      historyContainer.innerHTML = "<p>Failed to load transactions.</p>";
    });
}

// Load history on page start
loadTransactions();