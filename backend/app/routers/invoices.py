import os
import shutil
import json
from typing import List, Dict, Any
from fastapi import APIRouter, HTTPException, status, UploadFile, File
from app.services.ai_service import InvoiceAIProcessor

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_and_extract_invoice(file: UploadFile = File(...)):
    # Validate file
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF files are allowed"
        )
    
    if file.size > 10 * 1024 * 1024:  # 10MB limit
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="File size cannot exceed 10MB"
        )
    
    # Save file temporarily
    file_path = os.path.join(UPLOAD_DIR, f"temp_{file.filename}")
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Process with AI
        processor = InvoiceAIProcessor()
        extracted_data = processor.extract_invoice_data(file_path)
        
        if 'error' in extracted_data:
            return {
                "success": False,
                "filename": file.filename,
                "error": extracted_data['error']
            }
        else:
            return {
                "success": True,
                "filename": file.filename,
                "extracted_data": {
                    "invoice_number": extracted_data.get('invoice_number'),
                    "invoice_date": extracted_data.get('invoice_date'),
                    "due_date": extracted_data.get('due_date'),
                    "total_amount": extracted_data.get('total_amount'),
                    "currency": extracted_data.get('currency', 'USD'),
                    "subtotal": extracted_data.get('subtotal'),
                    "tax_amount": extracted_data.get('tax_amount'),
                    "vendor_name": extracted_data.get('vendor_name'),
                    "vendor_address": extracted_data.get('vendor_address'),
                    "vendor_email": extracted_data.get('vendor_email'),
                    "vendor_phone": extracted_data.get('vendor_phone'),
                    "customer_name": extracted_data.get('customer_name'),
                    "customer_address": extracted_data.get('customer_address'),
                    "customer_email": extracted_data.get('customer_email'),
                    "description": extracted_data.get('description'),
                    "payment_terms": extracted_data.get('payment_terms'),
                    "line_items": extracted_data.get('line_items', [])
                }
            }
    
    except Exception as e:
        return {
            "success": False,
            "filename": file.filename,
            "error": f"Processing failed: {str(e)}"
        }
    
    finally:
        # Clean up temporary file
        if os.path.exists(file_path):
            os.remove(file_path)

@router.get("/health")
async def health_check():
    return {"status": "healthy", "message": "Invoice extraction service is running"}
