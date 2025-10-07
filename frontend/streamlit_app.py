import streamlit as st
import requests
import json

# Backend URL
BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Invoice Extraction AI", page_icon="🧾")

st.title("🧾 Invoice Extraction AI")

uploaded_file = st.file_uploader("Choose a PDF invoice file", type=["pdf"])
if uploaded_file:
    st.write(f"File selected: {uploaded_file.name}")
    if st.button("Extract Details"):
        with st.spinner("Processing..."):
            files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}
            try:
                response = requests.post(f"{BACKEND_URL}/api/invoices/upload", files=files)
                data = response.json()
                if response.status_code == 200 and data.get("success"):
                    st.success("Extraction successful!")
                    st.json(data["extracted_data"])
                else:
                    st.error(f"Extraction failed: {data.get('error')}")
            except Exception as e:
                st.error(f"Connection error: {str(e)}")
