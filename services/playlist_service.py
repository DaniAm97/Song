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
        song_service = SongService()
        response = song_service.get_song(song.title)
        response_data = response.json()
        if response_data.get("error") == "this song does not exsist":
            song_service.add_song(song)
            print(f"this song was not in the system,\n f' the song {song.title}' has been added to the system.")
        data =\
            {
                "playlist_name": playlist.name,
                "song_title": song.title,
                "user_name": user.user_name,
                "user_password": user.user_password
            }
        response = self.api_Client.post('/playlists/add_song', json=data)
        return response
