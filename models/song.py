from pydantic import BaseModel,Field


class SongModel(BaseModel):
    genre: str
    performer: str
    title: str
    year: int
    rating: int = Field(default=0)
