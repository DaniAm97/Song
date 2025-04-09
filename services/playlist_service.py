from infrastructure.api_client import APIClient
from models.playlist import PlaylistModel
from models.user import UserModel
from models.song import SongModel
from services.song_service import SongService


class PlaylistService:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = APIClient()
        self.api_Client = api_client

    def add_song_to_playlist(self, user: UserModel, song: SongModel, playlist: PlaylistModel):
        data = \
            {
                "playlist_name": playlist.name,
                "song_title": song.title,
                "user_name": user.user_name,
                "user_password": user.user_password
            }
        response = self.api_Client.post('/playlists/add_song', json=data)
        return response
