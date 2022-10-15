import shutil
import pathlib
import zipfile

import httpx
from flask import Blueprint, redirect, render_template, send_file, url_for

from frontend.client.api import app_client

view = Blueprint('bird', __name__)


@view.route('/')
def birds():

    sparrows = app_client.bird.get_all(kind='sparrow')
    tits = app_client.bird.get_all(kind='tit')

    for sparrow in sparrows:
        sparrow.url_origin = app_client.image.get_url_origin_image(sparrow.uid)
        sparrow.url_result = app_client.image.get_url_result_image(sparrow.uid)

    for tit in tits:
        tit.url_origin = app_client.image.get_url_origin_image(tit.uid)
        tit.url_result = app_client.image.get_url_result_image(tit.uid)

    return render_template(
        'birds.html',
        sparrows=sparrows,
        tits=tits)


@view.route('/download/<int:bird_id>')
def download(bird_id: int):
    image_origin_path = app_client.image.get_url_origin_image(bird_id)
    image_result_path = app_client.image.get_url_result_image(bird_id)

    bird_name = app_client.bird.get_by_id(bird_id).name
    image_origin = httpx.get(image_origin_path).content
    image_result = httpx.get(image_result_path).content

    pathlib.Path('frontend/temp').mkdir(parents=True, exist_ok=True)

    image_origin_path = pathlib.Path(f'frontend/temp/origin_{bird_name}')
    image_result_path = pathlib.Path(f'frontend/temp/result_{bird_name}')

    with open(image_origin_path, 'wb') as f_in:
        f_in.write(image_origin)
    with open(image_result_path, 'wb') as f_in:
        f_in.write(image_result)

    zipfolder = zipfile.ZipFile('frontend/Birdfiles.zip', 'w', compression=zipfile.ZIP_STORED)

    zipfolder.write(image_origin_path, arcname='origin.jpg')
    zipfolder.write(image_result_path, arcname='result.jpg')
    zipfolder.close()

    shutil.rmtree('frontend/temp')

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
