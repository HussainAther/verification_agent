import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.agents.verification_agent import run_verification_flow

if __name__ == "__main__":
    print("Starting verification test for applicant A001...")
    run_verification_flow("A001")
    print("Verification process completed.")

