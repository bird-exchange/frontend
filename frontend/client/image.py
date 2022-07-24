import httpx

from frontend.schemas import Image


class ImageClient:

    def __init__(self, url: str):
        self.url = f'{url}/image'

    def get_all(self, kind: str) -> list[Image]:
        response = httpx.get(f'{self.url}/?kind={kind}')
        response.raise_for_status()
        images = response.json()
        return [Image(**image) for image in images]

    def get_by_id(self, uid: int) -> Image:
        response = httpx.get(f'{self.url}/image/{uid}')
        response.raise_for_status()
        image = response.json()
        return Image(**image)

    def delete_all(self) -> None:
        response = httpx.delete(f'{self.url}/')
        response.raise_for_status()

    def delete_by_id(self, uid: int) -> None:
        response = httpx.delete(f'{self.url}/{uid}')
        response.raise_for_status()
