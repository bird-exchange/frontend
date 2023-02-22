import botocore

from frontend.aws import s3_client


class ImageClient():

    def __init__(self, url):
        self.url = url

    def download_image_by_name(self, filename: str, bucket: str):
        try:
            s3_client.download_file(
                Bucket=bucket,
                Key=filename,
                Filename=f'frontend/media/{bucket}/{filename}'
            )
        except botocore.exceptions.ClientError:
            pass
