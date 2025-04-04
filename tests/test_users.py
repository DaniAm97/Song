import pytest
from unittest.mock import patch


def test_create_user(user_service, user_factory):
    user = user_factory.create_user("test_user1", "test_password2")
    response = user_service.create_user(user.user_name, user.user_password)
    assert response.status_code == 200
    response_data = response.json()
    assert "data" in response_data
    assert response_data["data"] == user.user_name
    assert response_data["message"] == "OK"


def test_validate_existing_user(user_service, user_factory):
    user = user_factory.get_user()
    response = user_service.create_user(user.user_name, user.user_password)
    assert response.status_code == 200
    response_data = response.json()
    assert "error" in response_data
    assert response_data["error"] == f"user with name {user.user_name} already exists."
