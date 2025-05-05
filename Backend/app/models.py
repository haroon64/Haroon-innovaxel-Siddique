from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Dict
import string# Models


class URLCreateRequest(BaseModel):
    url: HttpUrl

class URLUpdateRequest(BaseModel):
    url: HttpUrl

class URLResponse(BaseModel):
    id: str
    url: str
    shortCode: str
    createdAt: str
    updatedAt: str
    accessCount: int


class URLStatsResponse(URLResponse):
    accessCount: int