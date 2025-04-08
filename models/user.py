from pydantic import BaseModel, Field
from typing import Optional, List
from models.playlist import PlaylistModel


class UserModel(BaseModel):
    user_name: str
    user_password: str
    friends: Optional[List[str]] = Field(default_factory=list)
    playlists: List[PlaylistModel] = Field(default_factory=list)
