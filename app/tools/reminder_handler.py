from datetime import datetime, timedelta
from app.tools.db import get_applicant, increment_reminder, update_applicant
from app.tools.email import send_email

REMINDER_LIMIT = 3

def should_send_reminder(sent_timestamps):
    now = datetime.utcnow()
    if len(sent_timestamps) >= 3:
        return False
    if not sent_timestamps:
        return True
    return now - sent_timestamps[-1] >= timedelta(hours=24)
def should_send_reminder(sent_timestamps):
    now = datetime.utcnow()
    if len(sent_timestamps) >= 3:
        return False
    if not sent_timestamps:
        return True
    return now - sent_timestamps[-1] >= timedelta(hours=24)
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

