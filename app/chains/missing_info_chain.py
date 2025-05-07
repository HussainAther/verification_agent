from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

prompt = PromptTemplate(
    input_variables=["data"],
    template="List all missing fields from this applicant record:
{data}"
)

missing_info_chain = LLMChain(llm=ChatOpenAI(), prompt=prompt)
