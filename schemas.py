
from pydantic import BaseModel
import uuid

class LongURL(BaseModel):
    url: str

class ShortenedURLResponse(BaseModel):
    id: str
    old_url: str
    new_url: str
