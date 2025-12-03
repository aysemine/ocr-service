from app.logic.easy_ocr import easyocr_extract
from app.logic.llm_ocr import llm_vision_extract

def ocr_parser(ocr_type: str, file_path: str) -> str:
    """
    Decide which OCR backend to use and return raw text.
    """
    if ocr_type == "easyocr":
        return easyocr_extract(file_path)

    elif ocr_type == "llm_ocr":
        return llm_vision_extract(file_path)

    else:
        raise ValueError("Unknown OCR type")






