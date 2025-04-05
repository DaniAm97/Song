from infrastructure.api_client import APIClient

class UserService:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = APIClient()
        self.api_client = api_client