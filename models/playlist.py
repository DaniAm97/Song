from typing import List
from pydantic import BaseModel, Field


class PlaylistModel(BaseModel):
    name: str
    songs: List[str] = Field(default_factory=list)


