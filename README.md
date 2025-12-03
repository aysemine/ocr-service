# OCR Service

This project is a **FastAPI-based OCR service** that supports multiple OCR backends and automatic field extraction from documents.  

It allows users to **upload files**, perform OCR using **EasyOCR** or **OpenAI Vision**, and extract specific fields based on user-provided descriptions.

---

## Features

- **File Upload**
  - Upload PDFs, images (PNG, JPEG, JPG, TIFF, BMP).
  - PDFs are automatically converted to images for OCR processing.
- **OCR Engines**
  - **EasyOCR** for standard text extraction.
  - **OpenAI Vision** (LLM) for advanced OCR and hard-to-read text.
- **Field Extraction**
  - Extract specific fields from OCR text using a keyword.
  - If the field cannot be reliably extracted, automatically fallback to OpenAI for extraction based on description.
- **JSON-based API**
  - Easy integration with other services.
- **Docker-ready**
  - Service can be containerized for deployment.

---
### Install dependencies using `uv`

```bash
# If you do not have uv installed 
pip install uv

# Activate the uv environment
uv activate

# Install all dependencies from pyproject.toml
uv sync

# (Optional) Verify installation
uv info

#This project uses a `.env` file to store sensitive settings like API keys. Create a `.env` file in the project root and add the following:

FILE_DIR=uploads
OPENAI_API_KEY=your_openai_api_key_here

# run API service
uv run fastapi dev
