import os
from uuid import uuid4
from fastapi import UploadFile, HTTPException
from app.config import settings
from app.logic.file_converter import pdf_to_image, tiff_bmp_converter

os.makedirs(settings.FILE_DIR, exist_ok=True)

async def save_file(file: UploadFile) -> str:

    file_id = str(uuid4())
    ext = file.filename.split(".")[-1].lower() if "." in file.filename else "bin"
    file_bytes = await file.read()

    if ext == "pdf":
        try:
            combined_image = pdf_to_image(file_bytes)
            file_path = os.path.join(settings.FILE_DIR, f"{file_id}.png")
            combined_image.save(file_path, "PNG")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"File save failed: {e}")

    elif ext in ["png", "jpg", "jpeg"]:
        file_path = os.path.join(settings.FILE_DIR, f"{file_id}.{ext}")
        with open(file_path, "wb") as f:
            f.write(file_bytes)
    
    elif ext in ["tiff", "tif", "bmp"]:
        try:
            converted_bytes = tiff_bmp_converter(file_bytes, target_format="PNG")
            file_path = os.path.join(settings.FILE_DIR, f"{file_id}.png")
            with open(file_path, "wb") as f:
                f.write(converted_bytes)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"File save failed: {e}")
    
    else:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    return file_path


def get_file_path(file_id: str) -> str:
    """
    Finds the file path for a given file_id.
    Raises 404 if file does not exist.
    """
    for filename in os.listdir(settings.FILE_DIR):
        if filename.startswith(file_id):
            return os.path.join(settings.FILE_DIR, filename)

    raise HTTPException(status_code=404, detail="File not found")


