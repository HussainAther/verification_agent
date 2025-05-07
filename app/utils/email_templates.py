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

def build_international_verification_request(applicant_name: str):
    subject = "Additional Documents Required for International Education Verification"
    body = f"""\
Hi {applicant_name},

For international education verification, we require the following documents:

1. A copy of your state-issued ID or passport
2. A scanned copy of your degree or certificate
3. Both documents must be in the native language of the issuing institution

Please upload these documents via the portal or reply to this email.

Thank you,  
Verification Team
"""
    return subject, body

def build_name_mismatch_alert(applicant_name: str, known_aliases: list):
    alias_list = ", ".join(known_aliases)
    subject = f"Possible Name Discrepancy for {applicant_name}"
    body = f"""\
Dear Recruiter,

We encountered a potential name discrepancy during the verification process for {applicant_name}.
The applicant may also be known as: {alias_list}

Please confirm if these aliases are acceptable, or provide additional identification or clarification.

Regards,  
Verification Team
"""
    return subject, body

def build_multilingual_template(applicant_name: str, language_code="en"):
    templates = {
        "en": f"""\
Hi {applicant_name},

We require some additional documents for your verification. Please check your applicant portal or contact support.

Thank you,
Verification Team
""",
        "es": f"""\
Hola {applicant_name},

Necesitamos documentos adicionales para su verificación. Por favor, revise su portal de aplicación o contacte al soporte.

Gracias,  
Equipo de Verificación
""",
        "fr": f"""\
Bonjour {applicant_name},

Nous avons besoin de documents supplémentaires pour votre vérification. Veuillez consulter votre portail ou contacter le support.

Merci,  
Équipe de vérification
"""
    }
    return "Verification Follow-Up", templates.get(language_code, templates["en"])

