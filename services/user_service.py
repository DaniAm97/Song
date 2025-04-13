from infrastructure.api_client import APIClient
from models.user import UserModel


class UserService:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = APIClient()
        self.api_client = api_client

    def add_user(self, user: UserModel):
        data = {
            "user_name": user.user_name,
            "user_password": user.user_password
        }
        response = self.api_client.post('/users/add_user', json=data)
        return response

    def get_user(self, user: UserModel):
        data = {
            "user_name": user.user_name,
        }
        response = self.api_client.get("/users/get_user", params=data)
        return response

    def add_playlist(self, user_model: UserModel):
        data = {
            "playlist_name": user_model.playlists[0].name,
            "user_name": user_model.user_name,
            "user_password": user_model.user_password
        }
        response = self.api_client.post('/users/add_playlist', json=data)
        return response

    def add_friend(self, user_model: UserModel, friend_name: str):
        data = {
            "friend_name": friend_name,
            "user_name": user_model.user_name,
            "user_password": user_model.user_password
        }

        response = self.api_client.put('/users/add_friend', json=data)
        return response
