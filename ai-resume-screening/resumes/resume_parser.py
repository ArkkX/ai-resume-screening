# resumes/resume_parser.py
import spacy

nlp = spacy.load("en_core_web_sm")

def parse_resume(resume_text):
    doc = nlp(resume_text)
    
    name = None
    email = None
    skills = []
    experience = 0

    # Extract name and email
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name = ent.text
        elif ent.label_ == "EMAIL":
            email = ent.text
    
    # Example of extracting skills from a predefined list or keywords
    predefined_skills = ['python', 'django', 'data analysis', 'machine learning', 'java', 'javascript']
    for token in doc:
        if token.text.lower() in predefined_skills:
            skills.append(token.text.lower())
    
    # Extract years of experience based on the text (simplified example)
    for token in doc:
        if token.text.lower() == 'years':
            experience = int(token.nbor(-1).text)  # Simplified way to extract experience

    return name, email, skills, experience
