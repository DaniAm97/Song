from infrastructure.api_client import APIClient
from models.song import SongModel
from models.user import UserModel
from logger import logger


class SongService:
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = APIClient()
        self.api_client = api_client

    def get_song(self, song: SongModel):
        data = {"song_title": song.title}
        response = self.api_client.get('/songs/get_song', params=data)
        return response

    def add_song(self, song: SongModel):
        song_data = \
            {
                "song_genre": song.genre,
                "song_performer": song.performer,
                "song_title": song.title,
                "song_year": song.year,
                "rating": song.rating
            }
        response = self.api_client.post("/songs/add_song", json=song_data)
        logger.debug(f"Response status of add_song: {response.status_code}")
        logger.debug(f"Response body of add_song: {response.json()}")
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
        logger.debug(f"Response status of up_vote_song: {response.status_code}")
        logger.debug(f"Response body of up_vote_song: {response.json()}")
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
        logger.debug(f"Response status of down_vote_song: {response.status_code}")
        logger.debug(f"Response body of down_vote_song: {response.json()}")
        return response
