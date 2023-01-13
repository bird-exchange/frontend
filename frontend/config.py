import os

from pydantic import BaseModel


class AppConfig(BaseModel):
    endpoint: str
    host: str
    port: int


def load_from_env() -> AppConfig:
    endpoint = os.environ['ENDPOINT']
    return AppConfig(
        endpoint=endpoint,
        host=os.environ['APP_HOST_FRONT'],
        port=int(os.environ['APP_PORT_FRONT'])
    )


config = load_from_env()
