import spacy
import pdfplumber
import docx
import re
from typing import Dict, Any

# Load SpaCy model (will be loaded on startup)
nlp = spacy.load("en_core_web_trf")

def extract_text_from_pdf(file_path: str) -> str:
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def extract_text_from_docx(file_path: str) -> str:
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_entities(text: str) -> Dict[str, Any]:
    doc = nlp(text)
    
    entities = {
        "name": None,
        "email": None,
        "phone": None,
        "skills": [],
        "education": [],
        "experience": []
    }
    
    # 1. Email & Phone (Regex is often more reliable than NER for these)
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'(\+\d{1,2}\s?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}'
    
    email_match = re.search(email_pattern, text)
    if email_match:
        entities["email"] = email_match.group(0)
        
    phone_match = re.search(phone_pattern, text)
    if phone_match:
        entities["phone"] = phone_match.group(0)

    # 2. Name (SpaCy PERSON)
    for ent in doc.ents:
        if ent.label_ == "PERSON" and not entities["name"]:
            entities["name"] = ent.text
        elif ent.label_ == "ORG":
            entities["experience"].append(ent.text) # Simplified assumption
        elif ent.label_ == "DATE":
             pass # Could use for dates
             
    # 3. Simple Keyword Matching for Skills (Placeholder for more advanced custom NER)
    # In a real app, use a dedicated detailed skills list or EntityRuler
    common_skills = ["Python", "Java", "React", "JavaScript", "TypeScript", "SQL", "Docker", "AWS", "FastAPI", "Node.js"]
    text_lower = text.lower()
    for skill in common_skills:
        if skill.lower() in text_lower:
            entities["skills"].append(skill)
            
    return entities

def parse_resume(file_path: str, filename: str) -> Dict[str, Any]:
    if filename.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif filename.endswith(".docx"):
        text = extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format")
        
    data = extract_entities(text)
    return {"text": text, "data": data}
