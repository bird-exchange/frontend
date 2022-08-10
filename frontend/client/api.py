from frontend.client.bird import BirdClient
from frontend.client.image import ImageClient
from frontend.config import config


class AppClient:

    def __init__(self, endpoint: str) -> None:
        self.bird = BirdClient(endpoint)
        self.image = ImageClient(endpoint)


app_client = AppClient(endpoint=config.endpoint)
