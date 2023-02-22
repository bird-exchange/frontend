from flask import Flask

from frontend.view import bird, image, index


def create_app():
    app = Flask(__name__)

    app.register_blueprint(index.view)
    app.register_blueprint(bird.view, url_prefix='/birds')
    app.register_blueprint(image.view, url_prefix='/image')

    return app
