from langchain.tools import Tool

# Simulated institution contact database
MOCK_INSTITUTIONS = {
    "nyu": {
        "name": "New York University",
        "contact_url": "https://www.nyu.edu/registrar",
        "phone": "+1-212-998-4800",
        "email": "registrar@nyu.edu"
    },
    "harvard": {
        "name": "Harvard University",
        "contact_url": "https://www.harvard.edu/contact",
        "phone": "+1-617-495-1000",
        "email": "registrar@harvard.edu"
    }
}

def search_institution(name):
    key = name.strip().lower()
    result = MOCK_INSTITUTIONS.get(key)
    if result:
        return f"Found: {result['name']} | Contact: {result['email']} | Phone: {result['phone']}"
    return "Institution not found in directory."

search_tool = Tool(
    name="InstitutionSearch",
    func=search_institution,
    description="Finds contact information for an educational institution by name"
)

