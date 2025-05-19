import json
import os
from datetime import datetime

DB_FILE = "verification_agent/app/data/applicants.json"

# Ensure the data directory and file exist
os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)
if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump({}, f)

def load_db():
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_applicant(applicant_id):
    db = load_db()
    return db.get(applicant_id)

def update_applicant(applicant_id, updates):
    db = load_db()
    db.setdefault(applicant_id, {
        "status": "pending",
        "reminders_sent": 0,
        "last_updated": str(datetime.utcnow()),
        "history": []
    })
    db[applicant_id].update(updates)
    db[applicant_id]["last_updated"] = str(datetime.utcnow())
    save_db(db)

def increment_reminder(applicant_id):
    db = load_db()
    if applicant_id in db:
        db[applicant_id]["reminders_sent"] += 1
        db[applicant_id]["last_updated"] = str(datetime.utcnow())
        save_db(db)
        return db[applicant_id]["reminders_sent"]
    return 0

