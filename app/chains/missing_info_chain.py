from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

# Prompt that checks for common required fields in applicant data
prompt = PromptTemplate(
    input_variables=["data"],
    template="""You are a verification agent. Review the following applicant data and return a list of any missing or incomplete fields.

Applicant Data:
{data}

Expected fields: Full Name, Email, Institution, Course Name, Start Date, End Date, Nationality, Government ID (for international candidates), Degree Copy (if applicable)

Return your response as a plain list of missing fields.
"""
)

def get_missing_fields(applicant_data: dict) -> str:
    if not applicant_data.get("institution"):
        return "Missing fields: institution"
    return "All required fields present"


missing_info_chain = LLMChain(llm=ChatOpenAI(temperature=0), prompt=prompt)
