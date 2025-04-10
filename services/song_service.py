from infrastructure.api_client import APIClient
from models.song import SongModel
from models.user import UserModel


class SongService:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = APIClient()
        self.api_client = api_client

    def get_song(self, song_title):
        response = self.api_client.get('/songs/get_song', params={"song_title": song_title})
        return response

    def add_song(self, song: SongModel):
        song_data = \
            {
                "song_genre": song.genre,
                "song_performer": song.performer,
                "song_title": song.title,
                "song_year": song.year
            }
        response = self.api_client.post("/songs/add_song", json=song_data)
        return response

    def up_vote_song(self, user: UserModel, song: SongModel):
        data = \
            {
                "playlist_name": user.playlists[0].name,
                "song_title": song.title,
                "user_name": user.user_name,
                "user_password": user.user_password
            }
        response = self.api_client.put('/songs/upvote', json=data)
        return response

    def down_vote_song(self, user: UserModel, song: SongModel):
        data = \
            {
                "playlist_name": user.playlists[0].name,
                "song_title": song.title,
                "user_name": user.user_name,
                "user_password": user.user_password
            }
        response = self.api_client.put('/songs/downvote', json=data)
        return response
