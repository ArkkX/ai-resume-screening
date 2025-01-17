import spacy
from pdfminer.high_level import extract_text
from docx import Document

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    try:
        return extract_text(pdf_path)
    except Exception as e:
        return f"Error extracting text from PDF: {e}"

def extract_text_from_docx(docx_path):
    try:
        doc = Document(docx_path)
        return "\n".join([paragraph.text for paragraph in doc.paragraphs])
    except Exception as e:
        return f"Error extracting text from DOCX: {e}"

def preprocess_text(text):
    return text.lower().strip()

def extract_entities(text):
    doc = nlp(text)
    entities = {"skills": [], "education": [], "experience": []}
    for ent in doc.ents:
        if ent.label_ == "ORG" and "university" in ent.text.lower():
            entities["education"].append(ent.text)
        elif ent.label_ == "DATE":
            entities["experience"].append(ent.text)
        else:
            entities["skills"].append(ent.text)
    for key in entities:
        entities[key] = list(set(entities[key]))
    return entities
