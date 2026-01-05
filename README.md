# 📧 Email Triage Automation API

A production‑ready **Flask + MongoDB application** that classifies incoming emails using AI logic, applies deterministic decision rules, and stores results for analytics.  
This project demonstrates **full‑stack engineering, API design, and business‑focused automation** — built to showcase professional polish and recruiter‑ready skills.

---

## 🚀 Features
- **AI Classifier (Mock + Extensible)**  
  Classifies emails into `support`, `sales`, `spam`, or `other` with urgency levels (`high`, `medium`, `low`).
- **Decision Logic Engine**  
  Applies smart rules to determine actions: `escalate`, `auto‑reply`, `ignore`, `priority‑reply`, etc.
- **MongoDB Storage**  
  Persists every triaged email with metadata (sender, subject, body, intent, urgency, decision, timestamp).
- **Analytics Endpoints**  
  Query recent emails, filter by decision, and aggregate counts by intent.
- **Recruiter‑Ready Code Quality**  
  Modular structure (`ai_classifier.py`, `decision_logic.py`, `storage.py`, `app.py`) with environment variables managed via `.env`.

---

## 🛠 Tech Stack
- **Backend Framework**: Flask (Python)
- **Database**: MongoDB (local or Atlas, viewed via Compass)
- **Environment Management**: python‑dotenv
- **Deployment**: Waitress (stable WSGI server for Windows)
- **Optional AI Integration**: OpenAI API (extendable)

---

## 📂 Project Structure

```
email_triage_api/
│
├── .env                # Environment variables (API keys, DB URI)
├── app.py              # Flask API entry point
├── ai_classifier.py    # AI classification logic
├── decision_logic.py   # Decision rules engine
├── storage.py          # MongoDB operations
└── requirements.txt    # Python dependencies
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/email-triage.git
cd email-triage

```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file with:
```env
MONGO_URI=mongodb://localhost:27017/email_triage
OPENAI_API_KEY=your_openai_key  # Optional for AI extension
```

### 4. Run the Application
```bash
python app.py
```
or with Waitress:
```bash
waitress-serve --port=5000 app:app
```
#### Example Workflow
#### 1. POST an email to /triage-email:

json
{
  "sender": "client@example.com",
  "subject": "System outage",
  "body": "Critical issue, production system is down!"
}

#### 2. Classifier Output:

json
{ "intent": "support", "urgency": "high" }

#### 3. Decision Logic:

json
{ "decision": "escalate" }

#### 4. MongoDB Storage:

json
{
  "sender": "client@example.com",
  "subject": "System outage",
  "intent": "support",
  "urgency": "high",
  "decision": "escalate",
  "timestamp": "2026-01-05T23:28:26.917036"
}

---
👨‍💻 Author
Anuj Mundu  
Motivated MCA student, full‑stack developer, and aspiring business technologist.
Skilled in Python, Flask, MongoDB, React.js, Node.js, and AI/ML integration.
Focused on building scalable applications with measurable business impact.