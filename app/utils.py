# app/utils.py

# 📦 Standard Library Imports
import os
import shutil
from tempfile import NamedTemporaryFile

# 📚 Third-Party Libraries
from dotenv import load_dotenv
import fitz  # PyMuPDF for PDF handling


# 🔐 Load OpenAI API key from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

from openai import OpenAI
import json

client = OpenAI(api_key=openai_api_key)

def analyze_resume(resume_text: str):
    try:
        prompt = f"""
        You are a professional resume reviewer.

        Analyze the following resume and return your response **as a valid JSON object** with the following fields:
        - summary
        - strengths
        - weaknesses
        - suggestions
        - score

        Resume:
        {resume_text}
        """

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful and structured resume review assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )

        raw_output = response.choices[0].message.content.strip()

        # Try to parse as JSON
        try:
            structured = json.loads(raw_output)
            return structured
        except json.JSONDecodeError:
            print("⚠️ GPT returned invalid JSON")
            return {"raw_analysis": raw_output}

    except Exception as e:
        print("❌ OpenAI error:", e)
        return {"error": "There was an issue analyzing the resume with GPT."}


# 📄 Function to extract raw text from a PDF file uploaded via FastAPI
def extract_text_from_pdf(upload_file):
    try:
        print("✅ Starting PDF processing...")

        # Save uploaded file to a temporary file on disk
        with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            print("📥 Saving uploaded file to temp...")
            shutil.copyfileobj(upload_file.file, tmp)
            tmp_path = tmp.name
            print(f"📄 Temp PDF saved to: {tmp_path}")

        # Open the PDF using PyMuPDF
        doc = fitz.open(tmp_path)
        full_text = ""
        print(f"📄 PDF has {len(doc)} pages")

        # Loop through each page and extract text
        for i, page in enumerate(doc):
            page_text = page.get_text()
            print(f"📄 Page {i + 1} text length: {len(page_text)}")
            full_text += page_text

        doc.close()  # Close the PDF file
        os.remove(tmp_path)  # Clean up temp file

        # If no text was found, return None
        if full_text.strip() == "":
            print("⚠️ No text found in PDF")
            return None

        return full_text

    except Exception as e:
        print("❌ Exception during PDF parsing:", e)
        return None