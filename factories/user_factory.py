from models.playlist import PlaylistModel
from models.user import UserModel


class UserFactory:
    @staticmethod
    def create_user(username, password, playlist_name=None, song=None):
        playlist = None
        if playlist_name:
            if song is None:
                song = []
            playlist = PlaylistModel(name=playlist_name, songs=song)

        return UserModel(user_name=username, user_password=password, playlist=playlist, friends=[])

    @staticmethod
    def get_user():
        user_data = UserModel(
            user_name="test_username",
            user_password="test_password",
            playlist=PlaylistModel(name="Existing Playlist", songs=["Song 1", "Song 2"])
        )
        return user_data
