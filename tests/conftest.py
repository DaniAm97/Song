import logging

import pytest
from faker import Faker
from infrastructure.api_client import APIClient
from factories.playlist_factory import PlaylistFactory
from factories.user_factory import UserFactory
from logger import logger
from models.song import SongModel
from services.playlist_service import PlaylistService
from services.user_service import UserService
from factories.song_factory import SongFactory
from services.song_service import SongService


# admin fixture
@pytest.fixture(scope="session")
def delete_all_users():
    api_client = APIClient()
    response = api_client.delete('/admin/delete_all_users')
    return response


@pytest.fixture(scope="session")
def delete_all_songs():
    api_client = APIClient()
    response = api_client.delete('/admin/delete_all_songs')
    return response


@pytest.fixture(scope="function")
def add_song_fixture():
    fake = Faker()
    song = SongModel(
        title='test_' + fake.sentence(nb_words=5),
        genre=fake.word(),
        performer=fake.name(),
        year=fake.year(),
        rating=0
    )
    return SongService().add_song(song)


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


@pytest.fixture()
def playlist_service():
    return PlaylistService()


@pytest.fixture()
def playlist_factory():
    return PlaylistFactory()


@pytest.fixture(autouse=True)
def log_test_start_and_end(request):
    logger.info(f"========== Starting test: {request.node.name} ==========")
    yield
    logger.info(f"========== Finished test: {request.node.name} ==========")
