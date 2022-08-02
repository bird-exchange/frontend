from flask import Blueprint, render_template

from frontend.forms.upload import UploadFileForm

view = Blueprint("upload", __name__)


@view.route('/<string:kind>/', methods=['GET', 'POST'])
def upload(kind: str):
    form = UploadFileForm(meta={'csrf': False})

    if form.validate_on_submit():
        form.upload_file(kind=kind)

    return render_template('upload.html', form=form, kind=kind)
