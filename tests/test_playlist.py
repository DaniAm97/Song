def test_add_song_to_playlist(playlist_service, user_service, user_factory, song_service,
                              song_factory):
    user = user_factory.create_user("testttt1", "123456", "test_playlist")
    user_service.add_user(user)
    user_service.add_playlist(user)
    new_song = song_factory.create_song("Song 12141")
    song_service.add_song(new_song)
    response = playlist_service.add_song_to_playlist(song=new_song, user=user, playlist=user.playlists[0])
    response_data = response.json()

    assert response.status_code == 200
    assert response_data['data'] == new_song.title
    assert response_data["message"] == "OK"


def test_validation_add_song_that_already_in_the_playlist(playlist_service, user_service, user_factory, song_service,
                                                          song_factory):
    user = user_factory.create_user("testttt", "123456", "test_playlist")
    user_service.add_user(user)
    user_service.add_playlist(user)
    new_song = song_factory.create_song("Song 1212")
    song_service.add_song(new_song)
    response = playlist_service.add_song_to_playlist(song=new_song, user=user, playlist=user.playlists[0])
    response_data = response.json()

    assert response.status_code == 200
    assert response_data['error'] == (f"the song {new_song.title} already exist in the playlist or not in the songs "
                                      f"collection")


def test_validation_add_song_that_not_exist_in_the_system_to_the_playlist(playlist_service, user_service, user_factory,
                                                                          song_service,
                                                                          song_factory):
    user = user_factory.create_user("testttt", "123456", "test_playlist")
    user_service.add_user(user)
    user_service.add_playlist(user)
    new_song = song_factory.create_song("x")
    response = playlist_service.add_song_to_playlist(song=new_song, user=user, playlist=user.playlists[0])
    response_data = response.json()

    assert response.status_code == 200
    assert response_data['error'] == (f'the song {new_song.title} already exist in the playlist or not in the songs '
                                      f"collection")
