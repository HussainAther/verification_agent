from datetime import datetime, timedelta
from app.tools.db import get_applicant, increment_reminder, update_applicant
from app.tools.email import send_email

REMINDER_LIMIT = 3

def should_send_reminder(applicant_id):
    data = get_applicant(applicant_id)
    if not data:
        return False

    last_updated = datetime.fromisoformat(data["last_updated"])
    reminders_sent = data.get("reminders_sent", 0)

    # Send reminder if it's been at least 24 hours and fewer than 3 reminders sent
    if reminders_sent < REMINDER_LIMIT and datetime.utcnow() - last_updated >= timedelta(hours=24):
        return True
    return False

def send_reminder_if_needed(applicant_id, email, name):
    if should_send_reminder(applicant_id):
        count = increment_reminder(applicant_id)
        subject = f"Reminder {count}: Missing Information"
        body = f"Hi {name},\n\nThis is a reminder to provide your pending verification details.\n\nThank you."
        send_email(email, subject, body)

        if count >= REMINDER_LIMIT:
            update_applicant(applicant_id, {"status": "unverified"})
            return "Reminder sent and marked as unverified"
        return f"Reminder {count} sent"
    return "No reminder needed"

