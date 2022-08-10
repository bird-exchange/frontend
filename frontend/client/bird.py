import httpx

from frontend.schemas import Bird


class BirdClient:

    def __init__(self, url: str):
        self.url = f'{url}/bird'

    def get_all(self, kind: str) -> list[Bird]:
        response = httpx.get(f'{self.url}/?kind={kind}')
        response.raise_for_status()
        birds = response.json()
        return [Bird(**bird) for bird in birds]

    def get_by_id(self, uid: int) -> Bird:
        response = httpx.get(f'{self.url}/bird/{uid}')
        response.raise_for_status()
        bird = response.json()
        return Bird(**bird)

    def delete_all(self) -> None:
        response = httpx.delete(f'{self.url}/')
        response.raise_for_status()

    def delete_by_id(self, uid: int) -> None:
        response = httpx.delete(f'{self.url}/{uid}')
        response.raise_for_status()
