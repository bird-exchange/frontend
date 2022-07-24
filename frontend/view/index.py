from flask import Blueprint, render_template

view = Blueprint("index", __name__)


@view.route('/')
def index():
    return render_template('index.html')
