import os
import unittest
import logging

import requests


# logger factory


def create_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s:%(name)s:%(levelname)s:%(message)s")

    if not os.path.exists(os.path.join(os.getcwd(), "logs")):
        os.mkdir(os.path.join(os.getcwd(), "logs"))

    log_file_path = os.path.join(os.getcwd(), "logs", "test_app.log")
    file_handler = logging.FileHandler(log_file_path, mode="w")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


# logger object
logger = create_logger()


# Test runner
class TestRunner(unittest.TestCase):
    """
    The application test runner class
    """

    URL = "http://127.0.0.1:5002/api/v1"

    def test_healthz(self):
        res = requests.get(url=self.URL + "/healthz")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()), 1)
        logger.info("#1 'test_healthz' passed")

    def test_info(self):
        res = requests.get(url=self.URL + "/info")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()), 3)
        expected_output = {
            "languages": ["string"],
            "max_file_size": 0,
            "supported_formats": ["string"],
        }
        logger.info("#2 'test_info' passed")

    def test_ocr(self):
        expected_output = {
            "block_num": [0],
            "conf": [0],
            "height": [0],
            "left": [0],
            "level": [0],
            "line_num": [0],
            "page_num": [0],
            "par_num": [0],
            "text": ["string"],
            "top": [0],
            "width": [0],
            "word_num": [0],
        }
        # English
        payload = {"file": open(os.path.join(os.getcwd(), "tests", "ocr_images", "english.png"), "rb")}
        res = requests.post(self.URL + "/ocr", files=payload)
        self.assertEqual(res.status_code, 200)
        self.assertListEqual(list(res.json().keys()), list(expected_output.keys()))
        payload["file"].close()

        # French
        payload = {"file": open(os.path.join(os.getcwd(), "tests", "ocr_images", "french.jpg"), "rb")}
        res = requests.post(self.URL + "/ocr/fra", files=payload)
        self.assertEqual(res.status_code, 200)
        self.assertListEqual(list(res.json().keys()), list(expected_output.keys()))
        payload["file"].close()

        # Spanish
        payload = {"file": open(os.path.join(os.getcwd(), "tests", "ocr_images", "spanish.png"), "rb")}
        res = requests.post(self.URL + "/ocr/spa", files=payload)
        self.assertEqual(res.status_code, 200)
        self.assertListEqual(list(res.json().keys()), list(expected_output.keys()))
        payload["file"].close()

        logger.info("#3 'test_ocr' passed")


if __name__ == "__main__":
    unittest.main()
