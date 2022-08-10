from flask import Blueprint, render_template

from frontend.client.api import app_client

view = Blueprint('bird', __name__)


@view.route('/')
def birds():
    sparrows = app_client.bird.get_all(kind='sparrow')
    tits = app_client.bird.get_all(kind='tit')

    images_sparrows = []
    for sparrow in sparrows:
        image_origin = app_client.image.get_url_origin_image(sparrow.uid)
        image_result = app_client.image.get_url_result_image(sparrow.uid)
        images_sparrows.append((image_origin, image_result))

    images_tits = []
    for tit in tits:
        image_origin = app_client.image.get_url_origin_image(tit.uid)
        image_result = app_client.image.get_url_result_image(tit.uid)
        images_tits.append((image_origin, image_result))

    return render_template(
        'birds.html',
        images_sparrows=images_sparrows,
        images_tits=images_tits,
        tits=tits)
