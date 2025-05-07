from app.tools.email import send_email_tool
from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI

def run_verification_flow(applicant_id):
    # Dummy applicant data
    applicant_data = {
        "name": "John Doe",
        "email": "john@example.com",
        "institution": "",
        "course": "Computer Science"
    }

    if not applicant_data.get("institution"):
        agent = initialize_agent(
            tools=[send_email_tool],
            llm=ChatOpenAI(),
            agent="zero-shot-react-description",
            verbose=True
        )
        agent.run(f"send_email to {applicant_data['email']} requesting missing institution name")
