# app/routes.py
from fastapi import APIRouter, UploadFile, File
from app.utils import analyze_resume
from app.utils import extract_text_from_pdf

router = APIRouter()

@router.post("/analyze-resume")
async def analyze(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files are supported"}

    text = extract_text_from_pdf(file)

    if not text:
        return {"error": "Could not extract text from the uploaded PDF."}

    return {"extracted_text": text[:1000]}
