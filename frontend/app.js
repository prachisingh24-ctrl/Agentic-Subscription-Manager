const decisions = [
  { service: "Netflix", action: "Cancel", detail: "Predicted usage 0h", plan: "Premium", credits: 0 },
  { service: "Spotify", action: "Switch", detail: "Predicted usage 15h", plan: "Premium", credits: 5 },
  { service: "CloudCompute", action: "Keep", detail: "Predicted usage 43h", plan: "Basic", credits: 10 }
];

const container = document.getElementById("subscriptions");

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

  // Add button interaction
  card.querySelector(".btn").addEventListener("click", () => {
    alert(`${d.service}: ${d.action} confirmed!`);
  });

  container.appendChild(card);
});