from PIL import Image
import pytesseract
import werkzeug


def get_logger():
    import logging
    logger = logging.getLogger("ocr_logger")
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("[%(asctime)s]:%(name)s:%(levelname)s: %(message)s")
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


LOGGER = get_logger()


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
    
    LOGGER.info(f"Extracting OCR of file '{file.filename}'")
    result = pytesseract.image_to_data(
        Image.open(file), output_type=pytesseract.Output.DICT, lang=lang
    )
    return result
