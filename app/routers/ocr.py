from fastapi import APIRouter, HTTPException
from app.schemas import OCRRequest, OCRResponse
from app.logic.ocr_parser import ocr_parser
from app.logic.field_extractor import extract_field_llm, extract_field_basic
from app.logic.file_manager import get_file_path

router = APIRouter(
    tags=["OCR"]
)

@router.post("/ocr", response_model=OCRResponse)
async def perform_ocr(request: OCRRequest):
    try:
        file_path = get_file_path(request.file_id)
    except Exception:
        raise HTTPException(status_code=404, detail="File not found")

    raw_text = ocr_parser(request.ocr, file_path)
    raw_text = " ".join(raw_text.split()) 

    result = {}
    if request.field:
        value = extract_field_basic(raw_text, request.field.name, request.field.type)

        if value is None:
            value = extract_field_llm(raw_text, request.field.name, request.field.type, request.field.description)
        
        result[request.field.name] = value

    return OCRResponse(
        file_id=request.file_id,
        ocr=request.ocr,
        result=result,
        raw_ocr=raw_text
    )