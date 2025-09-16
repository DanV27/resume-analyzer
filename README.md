# 📄 Resume Analyzer - FastAPI + GPT + PDF Upload

This project extracts text from uploaded PDF resumes and uses OpenAI’s GPT to generate feedback. It showcases backend development, PDF processing, API integration, and environment configuration.

## 🚀 Features

- Upload PDF resumes via API
- Extract raw text from PDF using PyMuPDF
- Analyze resume content with OpenAI GPT-3.5
- Secure API key using a `.env` file
- Error handling for invalid files and API failures
- FastAPI framework for rapid backend development

## 🗂 Project Structure

```
resume-analyzer/
├── app/
│   ├── __init__.py
│   ├── routes.py         # Endpoint: /analyze-resume
│   └── utils.py          # PDF and GPT logic
├── main.py               # FastAPI app runner
├── .env                  # Stores OpenAI API key
├── .gitignore            # Ignores .env, __pycache__, etc.
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## 🛠 How to Run Locally

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/resume-analyzer.git
   cd resume-analyzer
   ```

2. **Set up a virtual environment**  
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file in the root directory**  
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Run the server**  
   ```bash
   uvicorn main:app --reload --port 8001
   ```

6. **Open Swagger UI**  
   [http://127.0.0.1:8001/docs](http://127.0.0.1:8001/docs)

## 📡 API Usage

### `POST /analyze-resume`

- Upload a PDF file using form-data
- Returns JSON containing GPT analysis

#### Example Response
```json
{
  "analysis": "Strong Python experience. Could add front-end tools. Score: 7.5/10"
}
```

## 🧠 Planned Enhancements

- Match resume against job description
- Frontend interface (React or Streamlit)
- Save and export results
- Batch resume processing

## 👤 Author

**Daniel Valenzuela‑Mendoza**  
WGU Computer Science Student  
GitHub: [danv27](https://github.com/danv27)  
LinkedIn: www.linkedin.com/in/danielvalen27

## 🪪 License

MIT License