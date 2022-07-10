from flask import Flask

from frontend.view import index


def create_app():
    app = Flask(__name__)

    app.register_blueprint(index.view)
    
    return app
