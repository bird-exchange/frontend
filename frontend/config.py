import os

from pydantic import BaseModel


class Aws(BaseModel):
    key_id: str
    key: str
    bucket_input_images: str
    bucket_output_images: str
    endpoint: str


class Server(BaseModel):
    port: int
    host: str


class AppConfig(BaseModel):
    endpoint: str
    server: Server
    aws: Aws


def load_from_env() -> AppConfig:
    backend_endpoint = os.environ['ENDPOINT']
    host = os.environ['APP_HOST_FRONT']
    port = int(os.environ['APP_PORT_FRONT'])
    aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
    aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
    aws_bucket_input_images = os.environ['AWS_BUCKET_NAME_INPUT_IMAGES']
    aws_bucket_output_images = os.environ['AWS_BUCKET_NAME_OUTPUT_IMAGES']
    aws_endpoint = os.environ['AWS_ENDPOINT']
    return AppConfig(
        endpoint=backend_endpoint,
        server=Server(port=port, host=host),
        aws=Aws(
            key_id=aws_access_key_id,
            key=aws_secret_access_key,
            bucket_input_images=aws_bucket_input_images,
            bucket_output_images=aws_bucket_output_images,
            endpoint=aws_endpoint
        )
    )


config = load_from_env()
