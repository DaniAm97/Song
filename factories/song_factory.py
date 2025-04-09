from models.song import SongModel


class SongFactory:
    @staticmethod
    def create_song(title, genre="", performer="", year=0, rating: int = 0):
        return SongModel(title=title, genre=genre, performer=performer, year=year, rating=rating)
