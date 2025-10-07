from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import invoices

app = FastAPI(
    title="Invoice Extraction AI",
    description="AI-powered invoice data extraction API - No Auth Version",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8501"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include only the invoices router
app.include_router(invoices.router, prefix="/api/invoices", tags=["Invoices"])

@app.get("/")
async def root():
    return {"message": "Invoice Extraction AI Backend - No Auth"}
