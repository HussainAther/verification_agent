from app.agents.decision_agent import make_verification_decision

applicant = {
    "institution": "NYU",
    "course": "Computer Science",
    "start_date": "2017",
    "end_date": "2021"
}

institution_response = {
    "institution": "NYU",
    "course": "Computer Science",
    "start_date": "2017",
    "end_date": "2021"
}

status, mismatches = make_verification_decision(applicant, institution_response)

