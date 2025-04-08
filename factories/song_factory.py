from models.song import SongModel


class SongFactory:
    @staticmethod
    def create_song(title):
        return SongModel(title=title, genre="", performer="", year=0)
