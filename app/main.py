from fastapi import FastAPI
from app.routers import ocr
from app.routers import file_upload

app = FastAPI()

app.include_router(ocr.router)
app.include_router(file_upload.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the OCR Service!"}   
