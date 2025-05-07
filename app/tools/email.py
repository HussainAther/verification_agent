from langchain.tools import Tool

def send_email(text):
    print(f"Sending email with text: {text}")
    return "Email sent."

send_email_tool = Tool(
    name="SendEmail",
    func=send_email,
    description="Sends emails to applicants or recruiters"
)
