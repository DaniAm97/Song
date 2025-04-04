from infrastructure.api_client import APIClient
from models.user import UserModel


class UserService:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = APIClient()
        self.api_client = api_client

    def create_user(self, username: str, password: str):
        user_data = UserModel(user_name=username, user_password=password)
        response = self.api_client.post('/users/add_user', json=user_data.model_dump())
        return response
