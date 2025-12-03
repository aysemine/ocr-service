from pydantic import BaseModel
from typing import Optional, Dict

class FieldSpec(BaseModel):
    name: str
    description: str
    type: str

class OCRRequest(BaseModel):
    file_id: str
    ocr: Optional[str] = "easyocr"
    field: FieldSpec
    
class OCRResponse(BaseModel):
    file_id: str
    ocr: str
    result: dict
    raw_ocr: str