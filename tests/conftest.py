import pytest

from factories.user_factory import UserFactory
from services.user_service import UserService


@pytest.fixture
def user_service():
    return UserService()


@pytest.fixture
def user_factory():
    return UserFactory()
