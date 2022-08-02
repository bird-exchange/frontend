import httpx
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from werkzeug.utils import secure_filename

from frontend.config import config

upload_url = f'{config.endpoint}/files/'


class UploadFileForm(FlaskForm):
    file = FileField(
        'File',
        validators=[
            FileRequired(),
            FileAllowed(['jpg', 'jpeg', 'png'], 'Image only!')
        ]
    )

    def upload_file(self, kind: str) -> bool:
        file = self.file.data
        filename = secure_filename(file.filename)
        files = {'file': (filename, file)}
        data = {'kind': kind}
        timeout = httpx.Timeout(5.0, connect=5.0, read=50.0, write=5.0)
        answer = httpx.post(upload_url, files=files, params=data, timeout=timeout)

        return answer.status_code == 201
