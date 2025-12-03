import fitz
from PIL import Image
import io

def pdf_to_image(pdf_bytes: bytes, zoom_x: float = 2.0, zoom_y: float = 2.0) -> Image.Image:
    """
    Convert a PDF (in bytes) into a single high-resolution combined image.
    zoom_x / zoom_y: scaling factors for width and height (2.0 = 200%)
    """
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    images = []

    for page in doc:
        # Create transformation matrix for scaling
        mat = fitz.Matrix(zoom_x, zoom_y)
        pix = page.get_pixmap(matrix=mat)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        images.append(img)

    # Combine pages vertically
    widths, heights = zip(*(i.size for i in images))
    total_height = sum(heights)
    max_width = max(widths)
    combined = Image.new("RGB", (max_width, total_height), (255, 255, 255))

    y_offset = 0
    for img in images:
        combined.paste(img, (0, y_offset))
        y_offset += img.height

    return combined


def tiff_bmp_converter(file_bytes: bytes, target_format: str = "PNG") -> bytes:

    with Image.open(io.BytesIO(file_bytes)) as img:
        if img.mode in ("P", "1"):
            img = img.convert("RGB")
        
        buf = io.BytesIO()
        img.save(buf, format=target_format)
        return buf.getvalue()
