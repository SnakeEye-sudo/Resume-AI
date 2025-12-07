from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from app.services.parser import parse_resume
from app.services.matching import match_resume_to_job
from app.services.ai import generate_suggestions, generate_cover_letter
import shutil
import os

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/parse")
async def parse_resume_endpoint(file: UploadFile = File(...)):
    file_location = f"{UPLOAD_DIR}/{file.filename}"
    with open(file_location, "wb+") as file_object:
        shutil.copyfileobj(file.file, file_object)
        
    try:
        parsed_data = parse_resume(file_location, file.filename)
        return parsed_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/match")
async def match_endpoint(
    resume_text: str = Form(...),
    job_description: str = Form(...)
):
    return match_resume_to_job(resume_text, job_description)

@router.post("/suggest")
async def suggest_endpoint(
    resume_text: str = Form(...),
    job_description: str = Form(...)
):
    return generate_suggestions(resume_text, job_description)
