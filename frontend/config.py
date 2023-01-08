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
        host=os.environ['APP_HOST'],
        port=int(os.environ['APP_PORT'])
    )


config = load_from_env()
