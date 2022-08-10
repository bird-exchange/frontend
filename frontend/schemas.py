from pydantic import BaseModel
from typing import Optional


class Bird(BaseModel):
    uid: int
    name: str
    type: int
    was_fitted: int
    url_origin: Optional[str]
    url_result: Optional[str]
