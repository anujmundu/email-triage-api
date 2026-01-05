from pymongo import MongoClient
from datetime import datetime
import os

MONGO_URI = os.getenv("MONGO_URI") 
DB_NAME = os.getenv("MONGO_DB") 
COLLECTION_NAME = os.getenv("MONGO_COLLECTION")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def store_email(email, ai_output, decision):
    record = {
        "sender": email.get("sender"),
        "subject": email.get("subject"),
        "body": email.get("body"),
        "intent": ai_output.get("intent"),
        "urgency": ai_output.get("urgency"),
        "confidence": ai_output.get("confidence", None),
        "decision": decision,
        "timestamp": datetime.now().isoformat()
    }
    collection.insert_one(record)
    print("Email stored in MongoDB:", record)

def get_all_emails(limit=10):
    return list(collection.find().sort("timestamp", -1).limit(limit))

def get_by_decision(decision, limit=10):
    return list(collection.find({"decision": decision}).sort("timestamp", -1).limit(limit))

def count_by_intent():
    pipeline = [
        {"$group": {"_id": "$intent", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]
    return list(collection.aggregate(pipeline))
