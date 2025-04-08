from typing import List
from pydantic import BaseModel, Field
from models.song import SongModel


class PlaylistModel(BaseModel):
    name: str
    songs: SongModel = None  # Default to an empty list if no songs are provided


