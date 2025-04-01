from pydantic import BaseModel


class PlaylistModel(BaseModel):
    name: str

