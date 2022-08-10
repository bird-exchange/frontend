import httpx


class ImageClient():

    def __init__(self, url):
        self.url = url

    def get_url_origin_image(self, uid: int) -> str:
        response = httpx.get(f'{self.url}/image/origin/{uid}')
        response.raise_for_status()
        return response.text

    def get_url_result_image(self, uid: int) -> str:
        response = httpx.get(f'{self.url}/image/result/{uid}')
        response.raise_for_status()
        return response.text
