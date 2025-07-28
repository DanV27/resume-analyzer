# app/routes.py
from fastapi import APIRouter, UploadFile, File
from app.utils import analyze_resume

router = APIRouter()

@router.post("/analyze-resume")
async def analyze(file: UploadFile = File(...)):
    return analyze_resume(file)
