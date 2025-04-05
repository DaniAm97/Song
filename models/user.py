from pydantic import BaseModel
from typing import Optional
from models.playlist import PlaylistModel


class UserModel(BaseModel):
    user_name: str
    user_password: str
    friends: Optional[list] = None
    playlist: Optional[PlaylistModel] = None
