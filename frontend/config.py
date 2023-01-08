import os

from pydantic import BaseModel


class AppConfig(BaseModel):
    endpoint: str
    host: str
    port: int


def load_from_env() -> AppConfig:
    endpoint = os.environ['ENDPOINT']
    host = os.environ['APP_HOST']
    port = int(os.environ['APP_PORT'])
    return AppConfig(endpoint=endpoint, host=host, port=port)


config = load_from_env()
