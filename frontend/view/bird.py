from flask import Blueprint, render_template

from frontend.client.api import app_client

view = Blueprint('bird', __name__)


@view.route('/')
def birds():
    sparrows = app_client.bird.get_all(kind='sparrow')
    tits = app_client.bird.get_all(kind='tit')

    files_sparrows = []
    for sparrow in sparrows:
        file_origin = app_client.file.get_url_origin_file(sparrow.uid)
        file_result = app_client.file.get_url_result_file(sparrow.uid)
        files_sparrows.append((file_origin, file_result))

    files_tits = []
    for tit in tits:
        file_origin = app_client.file.get_url_origin_file(tit.uid)
        file_result = app_client.file.get_url_result_file(tit.uid)
        files_tits.append((file_origin, file_result))

    return render_template(
        'birds.html',
        files_sparrows=files_sparrows,
        files_tits=files_tits,
        tits=tits)
