from flask import Blueprint, render_template

view = Blueprint('image', __name__)


@view.route('/')
def images():
    return render_template('images.html')
