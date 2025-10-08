# Invoice Extraction AI

This project extracts data from PDF invoice files using a Python backend and a Streamlit frontend.

## Requirements

- Python 3.9 or newer
- [uv](https://github.com/astral-sh/uv) package manager
- Git

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/rishabhg8/invoice-extraction-ai.git
   cd invoice-extraction-ai
   ```

2. Create and activate virtual environment:
   ```bash
   uv venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. Install all dependencies:
   ```bash
   uv sync
   ```

## Running the Application

1. Start the FastAPI backend (runs on port 8000):
   ```bash
   uv run uvicorn backend.main:app --reload
   ```

2. In a new terminal, start the Streamlit frontend:
   ```bash
   uv run streamlit run frontend/streamlit_app.py
   ```

3. Open your browser to http://localhost:8501 to access the app.

## Usage

1. Upload a PDF invoice file using the file uploader
2. Click "Extract Details" to process the invoice
3. View the extracted information in a structured format

## Notes

- Ensure both backend and frontend are running simultaneously
- The backend must be running before using the frontend interface
- Supported file format: PDF only (max 200MB)

## Project Structure

```
invoice-extraction-ai/
├── backend/
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   ├── streamlit_app.py
│   └── requirements.txt
└── README.md
```
