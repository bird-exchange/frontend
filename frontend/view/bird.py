import pathlib

import httpx
from flask import Blueprint, render_template, request, send_file

from frontend.client.api import app_client

view = Blueprint('bird', __name__)


@view.route('/', methods=['GET', 'POST', 'DELETE'])
def birds():

    if request.method == 'GET':

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

    elif request.method == 'POST':
        form_data = request.form.keys()
        bird_uids = []
        for check_input in form_data:
            bird_uids.append(int(request.form[check_input]))

        for uid in bird_uids:
            image_origin_path = app_client.image.get_url_origin_image(uid)
            bird_name = app_client.bird.get_by_id(uid).name
            image = httpx.get(image_origin_path).content
            pathlib.Path('frontend/temp').mkdir(parents=True, exist_ok=True)

            image_path = pathlib.Path(f'frontend/temp/{bird_name}')
            with open(image_path, 'wb') as f_in:
                f_in.write(image)

        return send_file(
            f'temp/{bird_name}',
            as_attachment=True)

    elif request.method == 'DELETE':
        form_data = request.form.keys()
        bird_uids = []
        for check_input in form_data:
            bird_uids.append(int(request.form[check_input]))
        for uid in bird_uids:
            app_client.bird.delete_by_id(uid)
