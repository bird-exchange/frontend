from flask import Flask

from frontend.view import index, image, upload


def create_app():
    app = Flask(__name__)

    app.register_blueprint(index.view)
    app.register_blueprint(image.view, url_prefix='/images')
    app.register_blueprint(upload.view, url_prefix='/upload')

    return app
