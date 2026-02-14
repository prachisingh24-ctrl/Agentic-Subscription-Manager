 🚀 Agentic Subscription Manager

An AI‑powered tool that helps you **take control of your subscriptions**.
It predicts usage, recommends whether to **Cancel**, **Switch**, or **Keep**, and displays everything on a glowing, futuristic **3D flip‑card dashboard**.

## ❗ Problem
Subscription services often drain money silently — users lose track of usage and overspend without transparency.

## 💡 Solution
The **Agentic Subscription Manager** uses an autonomous AI agent to:
- Monitor subscription usage
- Recommend Cancel / Switch / Keep actions
- Enforce monthly spend caps
- Generate transparent receipts with audit logs

## ✨ Features
- 🔮 **Smart Predictions**: Python backend analyzes subscription usage hours.
- 🎛️ **Actionable Decisions**: Cancel, Switch, or Keep recommendations.
- 💻 **Interactive Dashboard**: HTML/CSS/JS frontend with neon glow, 3D flip animations, and hover effects.
- 🤖 **Agentic AI Core**: Autonomous backend agent that reasons about data and outputs intelligent decisions.
- 👥 **Team‑Friendly**: Easy to clone, run, and extend for collaboration.

## 🤖 Agentic AI Core
The intelligence of this project lies in the **Python backend agent**:
- Reads subscription data (`data.json`).
- Predicts usage hours using heuristics or models.
- Makes autonomous decisions (Cancel, Switch, Keep).
- Outputs results in a color‑coded, human‑readable format.

This agentic behavior powers the interactive dashboard, ensuring decisions feel **AI‑driven** rather than manual.

## 🛠️ Setup Instructions

### Backend (Python)
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate it:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
3. Install dependencies:
   ```bash
   pip install colorama fastapi uvicorn
   ```
4. Run the backend:
   ```bash
   uvicorn server:app --reload
   ```

### Frontend (Dashboard)
1. Navigate to the `frontend` folder.
2. Open `index.html` in your browser.
3. Explore the glowing 3D dashboard with interactive cards.

## 📂 Project Structure
```
Agentic-Subscription-Manager/
│
├── backend/
│   ├── agent.py
│   ├── payments.py
│   ├── server.py
│   └── data.json
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
└── README.md
```

## 🌟 Demo Preview
Imagine a dashboard where:
- **Netflix** flips to reveal “Cancel – Predicted usage 0h”
- **Spotify** glows gold with “Switch – Predicted usage 15h”
- **CloudCompute** pulses green with “Keep – Predicted usage 43h”

Each card flips in 3D, showing details and glowing buttons for confirmation.

## 📌 Future Improvements
- Add **modal popups** for confirmation instead of alerts.
- Connect frontend actions to backend APIs.
- Add **user authentication** for personalized subscription tracking.
- Deploy as a web app for live demos.

## 🤝 Contributing
Pull requests are welcome! 
For major changes, please open an issue first to discuss what you’d like to change.

## 📜 License
MIT License – free to use, modify, and share with attribution.

## 🔗 Repository Link
[Agentic Subscription Manager](https://github.com/prachisingh24-ctrl/Agentic-Subscription-Manager)

## 🌐 Live Demo
[Try the Dashboard](https://prachisingh.github.io/Agentic-Subscription-Manager/)
