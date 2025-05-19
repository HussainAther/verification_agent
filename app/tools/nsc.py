from langchain.tools import Tool
import random
import time

# Simulated NSC database check
def verify_with_nsc(input_text):
    time.sleep(1)  # Simulate processing delay
    if "fail" in input_text.lower():
        return "NSC: No record found. Please verify with institution directly."
    
    # Simulate random turnaround or delay
    outcomes = [
        "NSC: Verification in progress. Estimated turnaround: 2 days.",
        "NSC: Verified successfully. Matches applicant record.",
        "NSC: Record found but with a mismatch in course dates."
    ]
    return random.choice(outcomes)

nsc_tool = Tool(
    name="NSCVerifier",
    func=verify_with_nsc,
    description="Simulates verification through the National Student Clearinghouse"
)

