from flask import Blueprint, redirect, render_template, send_from_directory, url_for
from werkzeug import exceptions

from frontend.forms.upload import UploadFileForm

view = Blueprint("image", __name__)


@view.route('/upload/<string:kind>/', methods=['GET', 'POST'])
def upload(kind: str):
    form = UploadFileForm(meta={'csrf': False})

    if form.validate_on_submit():
        form.upload_file(kind=kind)
        return redirect(url_for('bird.birds'))

    return render_template('upload.html', form=form, kind=kind)


@view.route('/<path:filename>')
def send(filename):
    try:
        return send_from_directory("../frontend/media/", filename, as_attachment=True)
    except exceptions.NotFound:
        return 'not found'
