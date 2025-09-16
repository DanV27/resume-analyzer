# app/routes.py

from fastapi import APIRouter, UploadFile, File
from app.utils import extract_text_from_pdf, analyze_resume

# Create a router instance to manage endpoints under a specific group
router = APIRouter()

@router.post("/analyze-resume")
async def analyze(file: UploadFile = File(...)):
    """
    Endpoint: /analyze-resume
    Method: POST
    Description:
        Accepts a PDF resume file, extracts the text using PyMuPDF,
        and returns the extracted text or an error message.
    """

    # ✅ Check if the uploaded file is a PDF
    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files are supported"}

    # 📄 Extract text from the uploaded PDF using utility function
    text = extract_text_from_pdf(file)

    # ❌ If no text was extracted, return an error
    if not text:
        return {"error": "Could not extract text from the uploaded PDF."}

    # Feedback from OpenAI analysis
    feedback = analyze_resume(text)
    return feedback
