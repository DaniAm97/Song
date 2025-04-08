from models.playlist import PlaylistModel
from models.user import UserModel
from models.song import SongModel


class UserFactory:
    @staticmethod
    def create_user(username, password, playlist_name=None, song=None):
        playlists = []

        if playlist_name:
            if song:
                song_data = SongModel(title=song)
                playlists = [PlaylistModel(name=playlist_name, songs=[song_data])]
            else:
                playlists = [PlaylistModel(name=playlist_name, songs=[])]  # Empty list if no song is provided

        return UserModel(user_name=username, user_password=password, playlists=playlists, friends=[])

    # @staticmethod
    # def get_user():
    #     user_data = UserModel(
    #         user_name="test_username",
    #         user_password="test_password",
    #         playlist=PlaylistModel(name="Existing Playlist", songs=[])
    #     )
    #     return user_data
