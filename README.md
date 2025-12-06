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
## Prerequisites

Before running the project, install:

**Docker**  
**Docker Compose**  
**uv**  
```bash
  pip install uv
```
## Installation

1. Clone the repository
```
git clone https://github.com/aysemine/ocr-service.git

cd ocr-service
```
2. Copy example .env and update to your variables
```
cp .env.example .env
```
3. Activate the uv environment
```
uv activate
```
4. Install all dependencies 
from pyproject.toml`
```
uv sync
```
(Optional) Verify installation
```
uv info
```
## Docker deployment

5. Build the docker image
```
docker compose build
```
6. Run the service
```
docker compose up
