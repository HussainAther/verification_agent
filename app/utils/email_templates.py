# app/utils/email_templates.py

def build_missing_info_email(fields: list, applicant_name: str):
    field_list = ", ".join(fields)
    subject = "Missing Information for Verification"
    body = f"""\
Hi {applicant_name},

We're currently processing your background verification and noticed the following missing information:

- {field_list}

Please respond to this email or use the applicant portal to upload the missing data.

Thank you,  
Verification Team
"""
    return subject, body

def build_reminder_email(applicant_name: str, days_pending: int):
    subject = f"Reminder: Pending Verification Information (Day {days_pending})"
    body = f"""\
Hi {applicant_name},

This is a reminder that we are still awaiting the necessary information to complete your verification process.

Please submit the required details as soon as possible.

Regards,  
Verification Team
"""
    return subject, body

def build_nsc_delay_email(applicant_name: str, recruiter_name: str, est_days: int):
    subject = f"NSC Verification Update: {applicant_name}"
    body = f"""\
Hi {recruiter_name},

We've submitted the education verification request for {applicant_name} via the National Student Clearinghouse.

The estimated turnaround time is approximately {est_days} days. We'll notify you as soon as we receive a response.

Thank you,  
Verification Team
"""
    return subject, body

