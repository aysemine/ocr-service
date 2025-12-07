import re
from openai import OpenAI
from app.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def extract_field_basic(raw_text: str, field_name: str, field_type: str):
    """
    Extracts a single field value from raw OCR text using the field name as keyword.
    Supports integers (including spaced or dotted numbers) and strings.
    """
    lines = raw_text.splitlines()

    for line in lines:
        if field_name.lower() in line.lower():
            after = line.split(field_name)[-1].strip().strip(": ")

            if field_type.lower() == "integer":
                number = re.sub(r"[^\d]", "", after)
                return number if number else None
            else:
                cleaned = " ".join(after.split())
                return cleaned if cleaned else None

    return None



def extract_field_llm(raw_text: str, field_name: str, field_type: str, field_description: str) -> str:
    """
    Uses an LLM to extract a single field value from raw text based on field description.
    """
    prompt = f"""
    You are an OCR text parser.
    Extract the value for the field: "{field_name}".
    Description: {field_description}
    The OCR text is below:
    \"\"\"
    {raw_text}
    \"\"\"
    Return the value in "{field_type}" format. If the value is not found, return "None".
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": prompt}
                ]
            }
        ]
    )

    text = response.output_text.strip()

    # Optionally, convert to integer if field_type is integer
    if field_type.lower() == "integer":
        digits = "".join(c for c in text if c.isdigit())
        return digits if digits else None

    return text if text else None
