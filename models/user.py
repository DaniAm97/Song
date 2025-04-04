from pydantic import BaseModel
from typing import Optional



class UserModel(BaseModel):
    user_name: str
    user_password: str
    friends: Optional[list] = None
    playlist: Optional[list] = None


