from flask import Flask

from frontend.view import bird, index, upload


def create_app():
    app = Flask(__name__)

    app.register_blueprint(index.view)
    app.register_blueprint(bird.view, url_prefix='/birds')
    app.register_blueprint(upload.view, url_prefix='/upload')

    return app
