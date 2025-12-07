import requests
import json
from typing import Dict, Any

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"

def generate_ai_response(prompt: str) -> str:
    try:
        payload = {
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return response.json().get("response", "")
    except Exception as e:
        print(f"Error calling Ollama: {e}")
        return "AI Service Unavailable"

def generate_suggestions(resume_text: str, job_description: str) -> Dict[str, Any]:
    prompt = f"""
    Analyze this resume against the job description and provide 3 specific improvement suggestions in JSON format.
    
    Resume: {resume_text[:2000]}
    Job Description: {job_description[:1000]}
    
    Return ONLY valid JSON with this structure:
    {{
        "suggestions": [
            "suggestion 1",
            "suggestion 2",
            "suggestion 3"
        ]
    }}
    """
    
    response_text = generate_ai_response(prompt)
    try:
        # cleanup markdown code blocks if present
        cleaned_text = response_text.replace("```json", "").replace("```", "").strip()
        return json.loads(cleaned_text)
    except json.JSONDecodeError:
        return {"suggestions": ["Could not parse AI response", response_text]}

def generate_cover_letter(resume_text: str, job_description: str) -> str:
    prompt = f"""
    Write a professional cover letter for this candidate.
    
    Resume Info: {resume_text[:2000]}
    Job Description: {job_description[:1000]}
    
    Tone: Professional and enthusiastic.
    Length: Concise (approx 200 words).
    """
    return generate_ai_response(prompt)
