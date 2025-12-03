from fastapi import APIRouter, UploadFile, HTTPException
from app.logic.file_manager import save_file  

router = APIRouter(tags=["File Upload"])


@router.post("/file-upload")
async def upload_file(file: UploadFile):
    """
    Upload a file, save it to disk, and return a unique file_id.
    """
    if not file:
        raise HTTPException(status_code=400, detail="No file uploaded")

    try:
        file_id = await save_file(file)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File save failed: {str(e)}")

    return {"file_id": file_id}
