import pytest
from infra.api_client import APIClient



@pytest.fixture
def create_user_request():
    api_client = APIClient()
    payload = \
        {
            "user_name": "test",
            "user_password": "123456"
        }
    new_user_request = api_client.post("/users/add_user", json=payload)
    return new_user_request.json()
