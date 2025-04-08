def test_add_song(song_factory, song_service):
    new_song = song_factory.create_song("dani dani dani dani shovevani")
    song = song_service.add_song(new_song)
    response_data = song.json()

    assert song.status_code == 200
    assert response_data["data"] == new_song.title
    assert response_data['message'] == "ok".upper()


def test_validate_existing_song(song_factory, song_service):
    new_song = song_factory.create_song("dani dani dani dani shovevani")
    song = song_service.add_song(new_song)
    response_data = song.json()

    assert song.status_code == 200

    #2 ways to get the error message
    assert response_data["error"] == "this song already exist in the collection"
    assert response_data["error"] == response_data.get("error")


def test_get_existing_song(song_factory, song_service):
    song = song_service.get_song('dani dani dani dani shovevani')
    response_data = song.json()
    assert song.status_code == 200
    assert response_data['data']['title'] == 'dani dani dani dani shovevani'
    assert response_data['message'] == "ok".upper()


def test_validate_get_song_that_doesnt_exist(song_factory, song_service):
    song = song_service.get_song('gg')
    response_data = song.json()
    assert song.status_code == 200
    assert response_data['error'] == f'this song does not exsist'
