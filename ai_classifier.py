import os
import openai
from dotenv import load_dotenv
load_dotenv()# Load variables from .env file
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

def classify_email(email):
    subject = (email.get("subject") or "").lower()
    body = (email.get("body") or "").lower()
    text = subject + " " + body

    # Intent detection
    if any(word in text for word in ["outage", "error", "issue", "down", "urgent", "help", "support"]):
        intent = "support"
    elif any(word in text for word in ["pricing", "quote", "cost", "plan", "buy", "purchase", "sales"]):
        intent = "sales"
    elif any(word in text for word in ["win", "prize", "lottery", "free", "offer", "click here"]):
        intent = "spam"
    else:
        intent = "other"

    # Urgency scoring
    urgency = "low"
    if any(word in text for word in ["urgent", "immediately", "critical", "asap", "down", "outage"]):
        urgency = "high"
    elif any(word in text for word in ["soon", "important", "problem", "delay"]):
        urgency = "medium"

    return {"intent": intent, "urgency": urgency}

