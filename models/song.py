from pydantic import BaseModel


class SongModel(BaseModel):
    grade: int
