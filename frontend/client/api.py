from frontend.client.image import ImageClient
from frontend.client.file import FileClient
from frontend.config import config


class AppClient:

    def __init__(self, endpoint: str) -> None:
        self.image = ImageClient(endpoint)
        self.file = FileClient(endpoint)


app_client = AppClient(endpoint=config.endpoint)
