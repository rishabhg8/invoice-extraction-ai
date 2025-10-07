# 🧾 Invoice Extraction AI

Invoice Extraction AI is a demo application built with FastAPI and Streamlit that extracts structured data from PDF invoices. This no-auth version focuses on showcasing PDF text extraction and data parsing.

## Features

- PDF text extraction using `pdfplumber`
- Demo data extraction showing key invoice fields and line items
- Live Streamlit frontend for file upload and display
- Easy local setup and deployment on Streamlit Community Cloud

## Project Structure

```plaintext
Invoice_Extraction_AI/
├── backend/
│   ├── app/
│   │   ├── routers/
│   │   │   └── invoices.py
│   │   └── services/
│   │       └── ai_service.py
│   ├── main.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── streamlit_app.py
│   └── requirements.txt
├── packages.txt
├── .gitignore
└── README.md
```

## Local Setup

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/invoice-extraction-ai.git
cd invoice-extraction-ai
```

### 2. Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate       # Windows
# source .venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

### 3. Frontend

```bash
cd ../frontend
# Activate same .venv from backend
pip install -r requirements.txt
streamlit run streamlit_app.py --server.port 8501
```

Open [http://localhost:8501](http://localhost:8501) to upload a PDF invoice and see demo extraction results.

## Deployment on Streamlit Cloud

1. Push to GitHub (main branch).
2. In Streamlit Community Cloud, select your repo.
3. Set **Main file** to `frontend/streamlit_app.py`.
4. Add any required environment variables.
5. Deploy and share the live URL.

## License

MIT License
