from typing import Optional
from models.song import SongModel
from models.playlist import PlaylistModel


class PlaylistFactory:
    @staticmethod
    def create_playlist(playlist_name: str, song: Optional[SongModel] = None):

        songs = []
        if song:
            song_data = SongModel(title=song)
            songs.append(song_data)

        return PlaylistModel(name=playlist_name, songs=songs)
