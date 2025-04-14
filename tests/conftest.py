import pytest
from faker import Faker
from infrastructure.api_client import APIClient
from factories.playlist_factory import PlaylistFactory
from factories.user_factory import UserFactory
from logger import logger
from models.playlist import PlaylistModel
from models.song import SongModel
from models.user import UserModel
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


faker = Faker()


@pytest.fixture
def fake_user():
    # Create and return the fake user
    fake_user = UserModel(user_name=faker.user_name(), user_password=faker.password())
    logger.info(f'created fake user:\n {fake_user}')
    return fake_user


@pytest.fixture
def fake_user_with_playlist():
    # Create a fake playlist
    fake_playlist = \
        PlaylistModel(name=faker.word(), songs=[])
    fake_user = UserModel(user_name=faker.user_name(), user_password=faker.password(), playlists=[fake_playlist])
    logger.info(f'created fake user:\n {fake_user}')
    # Create a nd return the fake user
    return fake_user


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
    logger.info(f"=============================== Starting test: {request.node.name}===============================")
    yield
    logger.info(f"=============================== Finished test: {request.node.name}==============================="'\n')
