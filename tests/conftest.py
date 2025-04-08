import pytest

from factories.user_factory import UserFactory
from services.user_service import UserService
from factories.song_factory import SongFactory
from services.song_service import SongService


@pytest.fixture
def user_service():
    return UserService()


@pytest.fixture
def user_factory():
    return UserFactory()


@pytest.fixture()
def song_service():
    return SongService()


@pytest.fixture()
def song_factory():
    return SongFactory()
