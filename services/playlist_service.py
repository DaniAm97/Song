from infrastructure.api_client import APIClient
f


class PlaylistService:
    def __init__(self, api_client = None):
        if api_client is None:
            api_client = APIClient()
        self.api_Client = api_client


####### before adding song to the playlist - song need to be added to the system(add_song to system)