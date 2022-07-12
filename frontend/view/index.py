from flask import Blueprint, render_template
from frontend.forms.upload import UploadFileForm


view = Blueprint("index", __name__)


@view.route('/', methods=['GET', 'POST'])
def index():
    form = UploadFileForm(meta={'csrf': False})

    if form.validate_on_submit():
        form.upload_file()

    return render_template('index.html', form=form)
