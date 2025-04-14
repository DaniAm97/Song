from infrastructure.api_client import APIClient
from models.user import UserModel
from logger import logger


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
        logger.debug(f"Response status of add_user: {response.status_code}")
        logger.debug(f"Response body of add_user: {response.json()}")
        return response

    def get_user(self, user: UserModel):
        data = {
            "user_name": user.user_name,
        }
        response = self.api_client.get("/users/get_user", params=data)
        logger.debug(f"Response status of get_user: {response.status_code}")
        logger.debug(f"Response body of get_user: {response.json()}")
        return response

    def add_playlist(self, user_model: UserModel):
        data = {
            "playlist_name": user_model.playlists[0].name,
            "user_name": user_model.user_name,
            "user_password": user_model.user_password
        }
        response = self.api_client.post('/users/add_playlist', json=data)
        logger.debug(f"Response status of add_playlist: {response.status_code}")
        logger.debug(f"Response body of add_playlist: {response.json()}")
        return response

    def add_friend(self, user_model: UserModel, friend_name: str):
        data = {
            "friend_name": friend_name,
            "user_name": user_model.user_name,
            "user_password": user_model.user_password
        }

        response = self.api_client.put('/users/add_friend', json=data)
        logger.debug(f"Response status of add_friend: {response.status_code}")
        logger.debug(f"Response body of add_friend: {response.json()}")
        return response
