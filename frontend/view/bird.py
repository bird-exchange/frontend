import pathlib
import zipfile

from flask import Blueprint, redirect, render_template, send_file, url_for

from frontend.client.api import app_client

view = Blueprint('bird', __name__)


@view.route('/')
def birds():

    sparrows = app_client.bird.get_all(kind='sparrow')
    tits = app_client.bird.get_all(kind='tit')

    for sparrow in sparrows:
        app_client.image.download_image_by_name(filename=sparrow.name, bucket='input-images')
        app_client.image.download_image_by_name(filename=sparrow.name, bucket='output-images')

    for tit in tits:
        app_client.image.download_image_by_name(filename=tit.name, bucket='input-images')
        app_client.image.download_image_by_name(filename=tit.name, bucket='output-images')

    return render_template(
        'birds.html',
        sparrows=sparrows,
        tits=tits)


@view.route('/download/<int:bird_id>')
def download(bird_id: int):

    bird_name = app_client.bird.get_by_id(bird_id).name

    image_origin_path = pathlib.Path(f'frontend/media/input-images/{bird_name}')
    image_result_path = pathlib.Path(f'frontend/media/output-images/{bird_name}')

    zipfolder = zipfile.ZipFile('frontend/Birdfiles.zip', 'w', compression=zipfile.ZIP_STORED)

    zipfolder.write(image_origin_path, arcname='origin.jpg')
    zipfolder.write(image_result_path, arcname='result.jpg')
    zipfolder.close()

    return send_file(
        'Birdfiles.zip',
        mimetype='zip',
        attachment_filename='Birdfiles.zip',
        as_attachment=True
    )


@view.route('/delete/<int:bird_id>')
def delete(bird_id: int):
    app_client.bird.delete_by_id(bird_id)
    return redirect(url_for('bird.birds'))
