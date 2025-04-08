from typing import List
from pydantic import BaseModel, Field
from models.song import SongModel


class PlaylistModel(BaseModel):
    name: str
    songs: List[SongModel] = Field(default_factory=list)


