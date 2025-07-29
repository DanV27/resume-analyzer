from dotenv import load_dotenv
import os
import fitz  # PyMuPDF for PDF handling
from tempfile import NamedTemporaryFile
import shutil

# Load environment variables from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# app/utils.py
def analyze_resume(file):
    return {"message": "Resume analysis will go here."}


import fitz
from tempfile import NamedTemporaryFile
def extract_text_from_pdf(upload_file):
    try:
        print("✅ Starting PDF processing...")

        # Save file manually
        with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            print("📥 Saving uploaded file to temp...")
            shutil.copyfileobj(upload_file.file, tmp)
            tmp_path = tmp.name
            print(f"📄 Temp PDF saved to: {tmp_path}")

        # Open and extract text
        doc = fitz.open(tmp_path)
        full_text = ""
        print(f"📄 PDF has {len(doc)} pages")
        for i, page in enumerate(doc):
            page_text = page.get_text()
            print(f"📄 Page {i + 1} text length: {len(page_text)}")
            full_text += page_text

        doc.close()
        os.remove(tmp_path)  # clean up

        if full_text.strip() == "":
            print("⚠️ No text found in PDF")
            return None

        return full_text

    except Exception as e:
        print("❌ Exception during PDF parsing:", e)
        return None

