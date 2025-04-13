from pydantic import BaseModel, Field
from typing import Optional


class SongModel(BaseModel):
    genre: Optional[str] = None
    performer: Optional[str] = None
    title: str
    year: Optional[int] = None
    rating: int = 0
