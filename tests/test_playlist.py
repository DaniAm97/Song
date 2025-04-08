def test_add_song_to_playlist(playlist_service, playlist_factory, user_service, user_factory, song_service,
                              song_factory):
    user_init = user_factory.create_user(username='DaniTest', password="1234")
    user = user_service.add_user(user_init)
    song = song_factory.create_song("SongTest")
    playlist_init = playlist_factory.create_playlist(playlist_name="PlaylistTest1")
    song_added_to_playlist = playlist_service.add_song_to_playlist(playlist=playlist_init, song=song,
                                                                   user=user_init)
    data_response = song_added_to_playlist.json()


    print(data_response)
