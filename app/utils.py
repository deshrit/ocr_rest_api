from PIL import Image
import pytesseract
import werkzeug

SUPPORTED_FORMATS = [
    "JPEG",
    "JPG",
    "JPEG2000",
    "PNG",
    "PBM",
    "PGM",
    "PPM",
    "TIFF",
    "BMP",
    "GIF",
    "WEBP",
]


class Languages:
    ENGLISH = "eng"
    FRENCH = "fra"
    SPANISH = "spa"


def validate_file(file_name: str) -> bool:
    ext = file_name.split(".")[-1].upper()
    return ext in SUPPORTED_FORMATS


def get_ocr_data(
    file: werkzeug.datastructures.FileStorage, lang: str = Languages.ENGLISH
) -> dict:
    result = pytesseract.image_to_data(
        Image.open(file), output_type=pytesseract.Output.DICT, lang=lang
    )
    return result
