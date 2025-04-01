from infra.api_client import APIClient
from model.user import UserModel


class User:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client


