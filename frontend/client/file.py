import httpx


class FileClient():

    def __init__(self, url):
        self.url = url

    def get_url_origin_file(self, uid: int) -> str:
        response = httpx.get(f'{self.url}/files/origin/{uid}')
        response.raise_for_status()
        return response.text

    def get_url_result_file(self, uid: int) -> str:
        response = httpx.get(f'{self.url}/files/result/{uid}')
        response.raise_for_status()
        return response.text
