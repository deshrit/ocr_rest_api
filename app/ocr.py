from flask import Blueprint, request, jsonify
from . import utils

bp = Blueprint("ocr", __name__, url_prefix="/api/v1/ocr")

@bp.route("/eng", methods=["POST"])
def ocr():
    if not request.files:
        return jsonify({"error": "Upload a image file with key 'file'"}), 400

    try:
        file = request.files["file"]
        if utils.validate_file(file.filename):
            res = utils.get_ocr_data(file)
            return jsonify(res)
        return jsonify({"error": "Only image files are allowed"}), 400
    except Exception as e:
        pass

    return {}


@bp.route("/fra", methods=["POST"])
def ocr_fra():
    if not request.files:
        return jsonify({"error": "Upload a image file with key 'file'"}), 400

    try:
        file = request.files["file"]
        if utils.validate_file(file.filename):
            res = utils.get_ocr_data(file, lang=utils.Languages.FRENCH)
            return jsonify(res)
        return jsonify({"error": "Only image files are allowed"}), 400
    except Exception as e:
        pass

    return {}


@bp.route("/spa", methods=["POST"])
def ocr_spa():
    if not request.files:
        return jsonify({"error": "Upload a image file with key 'file'"}), 400

    try:
        file = request.files["file"]
        if utils.validate_file(file.filename):
            res = utils.get_ocr_data(file, lang=utils.Languages.SPANISH)
            return jsonify(res)
        return jsonify({"error": "Only image files are allowed"}), 400
    except Exception as e:
        pass

    return {}
