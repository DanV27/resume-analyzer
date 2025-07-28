from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# app/utils.py
def analyze_resume(file):
    return {"message": "Resume analysis will go here."}




