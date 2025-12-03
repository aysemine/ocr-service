from easyocr import Reader

reader = Reader(['tr'], gpu=False)

def easyocr_extract(image_path: str) -> str:
    result = reader.readtext(image_path, detail=0)
    return " ".join(result).lower()
