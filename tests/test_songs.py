def test_add_song(song_factory, song_service):
    new_song = song_factory.create_song("dani dani dani dani shovevani3")
    song = song_service.add_song(new_song)
    response_data = song.json()

    assert song.status_code == 200
    assert response_data["data"] == new_song.title
    assert response_data['message'] == "ok".upper()


def test_validate_existing_song(song_factory, song_service):
    new_song = song_factory.create_song("dani dani dani dani shovevani3")
    song = song_service.add_song(new_song)
    response_data = song.json()

    assert song.status_code == 200

    #2 ways to get the error message
    assert response_data["error"] == "this song already exist in the collection"
    assert response_data["error"] == response_data.get("error")


def test_get_existing_song(song_factory, song_service):
    song = song_service.get_song('dani dani dani dani shovevani3')
    response_data = song.json()
    assert song.status_code == 200
    assert response_data['data']['title'] == 'dani dani dani dani shovevani3'
    assert response_data['message'] == "ok".upper()


def test_validate_get_song_that_doesnt_exist(song_factory, song_service):
    song = song_service.get_song('gg')
    response_data = song.json()
    assert song.status_code == 200
    assert response_data['error'] == f'this song does not exsist'


def test_upvote_song(song_factory, song_service, user_factory, user_service, playlist_factory, playlist_service):
    user = user_factory.create_user("testcheckx", "test1", "playlistcheck1")
    user_service.add_user(user)
    user_service.add_playlist(user)
    new_song = song_factory.create_song("Song x10")
    response = song_service.add_song(new_song)
    playlist_service.add_song_to_playlist(song=new_song, playlist=user.playlists[0], user=user)
    song_got_upvote = song_service.up_vote_song(user, new_song)
    response_data = song_got_upvote.json()

    assert song_got_upvote.status_code == 200
    assert response_data['data']['song_title'] == new_song.title
    assert response_data['message'] == "OK"
    assert response_data['data']['rating'] == 1


def test_validation_upvote_song_that_not_exist(song_factory, song_service, user_factory, user_service, playlist_factory,
                                               playlist_service):
    user = user_factory.create_user("TestStack", "test1", "playlist check1")
    user_service.add_user(user)
    user_service.add_playlist(user)
    new_song = song_factory.create_song("")
    response = song_service.up_vote_song(user, new_song)
    response_data = response.json()

    assert response.status_code == 200
    assert response_data['error'] == 'no such song in the songs collection'


def test_down_vote_song(user_service, user_factory, song_service, song_factory, playlist_service):
    user = user_factory.create_user("danidani", "dani123", "psadlasdasd")
    user_service.add_user(user)
    user_service.add_playlist(user)
    new_song = song_factory.create_song("down_vote_song", rating=2)
    song_service.add_song(new_song)
    playlist_service.add_song_to_playlist(user=user, song=new_song, playlist=user.playlists[0])
    song_got_down_vote = song_service.down_vote_song(user=user, song=new_song)
    response_data = song_got_down_vote.json()

    assert song_got_down_vote.status_code == 200
    assert response_data['data']['song_title'] == new_song.title
    assert response_data['data']['rating'] == 1


def test_validation_down_vote_song_with_rating_zero(user_service, user_factory, song_service, song_factory,
                                                    playlist_service):
    user = user_factory.create_user("danidani", "dani123", "psadlasdasd")
    user_service.add_user(user)
    user_service.add_playlist(user)
    new_song = song_factory.create_song(
        "down_vote_song_with_rating_zero")  # the default of rating is 0 so no need to create one.
    song_service.add_song(new_song)
    playlist_service.add_song_to_playlist(user=user, song=new_song, playlist=user.playlists[0])
    song_got_down_vote = song_service.down_vote_song(user=user, song=new_song)
    response_data = song_got_down_vote.json()

    assert song_got_down_vote.status_code == 200
    assert response_data['data']['song_title'] == new_song.title
    assert response_data['data']['rating'] == 0
