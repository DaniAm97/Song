from models.playlist import PlaylistModel
from models.user import UserModel
from models.song import SongModel


class UserFactory:
    @staticmethod
    def create_user(username, password, playlist_name=None, song=None):
        # Initialize playlists as an empty list by default
        playlists = []

        if playlist_name:
            if song:
                song_data = SongModel(title=song)
            else:
                song_data = None
            # Create a playlist and add it to the playlists list
            playlists = [PlaylistModel(name=playlist_name, songs=song_data)]

        # Create and return the user model with the playlists
        return UserModel(user_name=username, user_password=password, playlists=playlists, friends=[])

    # @staticmethod
    # def get_user():
    #     user_data = UserModel(
    #         user_name="test_username",
    #         user_password="test_password",
    #         playlist=PlaylistModel(name="Existing Playlist", songs=[])
    #     )
    #     return user_data
