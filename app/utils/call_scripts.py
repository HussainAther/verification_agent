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

