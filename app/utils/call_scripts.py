# app/utils/call_scripts.py

def education_verification_script(applicant_name, course_name, start_date, end_date):
    return f"""\
Hello, my name is [Agent Name], and I’m calling from [Company Name] regarding an education verification.

We’re trying to verify the following details for a former student:

- Name: {applicant_name}
- Course: {course_name}
- Attendance Period: {start_date} to {end_date}

Could you confirm if this information is accurate or direct us to the right department (registrar/admissions)? 
We’re happy to follow your verification process, including submitting a release form if needed.
"""

def nsc_inquiry_script():
    return """\
Hello, I’m trying to verify an academic record through the National Student Clearinghouse. 

Could you confirm if this institution reports to NSC, or if we should verify directly with your office?

Thank you!
"""

def international_call_script(applicant_name):
    return f"""\
Hello, I’m calling regarding the international academic verification for a candidate named {applicant_name}.

Could you please confirm what documentation you require for degree verification?
We can provide a government-issued ID and a native-language diploma if needed.

Is there a verification contact or form you prefer we use?

Thank you!
"""

def name_discrepancy_call_script(applicant_name, aliases):
    alias_str = ", ".join(aliases)
    return f"""\
Hi, I’m calling regarding a verification for {applicant_name}. 

We noticed that the applicant might also be known as: {alias_str}.
Can you confirm if these names appear in your records, or if we need to submit documentation?

Thank you!
"""

