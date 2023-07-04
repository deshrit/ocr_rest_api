from flask import Blueprint, jsonify
from . import utils

bp = Blueprint("info", __name__, url_prefix="/api/v1")


@bp.route("/", methods=["GET"])
@bp.route("/healthz", methods=["GET"])
def healthz():
    return jsonify({"message": "Server is live"})


@bp.route("/info", methods=["GET"])
def info():
    ocr_langs = ["eng", "fra", "spa"]
    res = {
        "languages": ocr_langs,
        "max_file_size": 5,
        "supported_formats": utils.SUPPORTED_FORMATS,
    }
    return jsonify(res)
