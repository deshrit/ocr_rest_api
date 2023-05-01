import os

from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

from . import info
from . import ocr


def create_app():
    # flask app
    app = Flask(__name__)
    CORS(app)
    
    app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024
    # app.config["UPLOAD_FOLDER"] = os.path.join(os.getcwd(), "uploads")

    # swagger ui
    SWAGGER_URL = "/api/v1/docs"
    API_URL = "/static/swagger.json"
    swagger_ui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL, API_URL, config={"app_name": "OCR REST API"}
    )

    # docs
    app.register_blueprint(swagger_ui_blueprint)

    # functions
    app.register_blueprint(info.bp)
    app.register_blueprint(ocr.bp)
    return app
