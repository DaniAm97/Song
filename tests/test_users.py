def test_create_user(user_service, user_factory):
    user = user_factory.create_user(
        username="",
        password=""
    )
    response = user_service.add_user(user)

    assert response.status_code == 200

    response_data = response.json()
    assert response_data["data"] == user.user_name
    assert response_data["message"] == "OK"


def test_validate_existing_user(user_service, user_factory):
    user = user_factory.create_user(
        username="test_username",
        password="test_password"
    )
    response = user_service.add_user(user)

    assert response.status_code == 200

    response_data = response.json()
    assert "error" in response_data
    assert response_data["error"] == f"user with name {user.user_name} already exists."


def test_add_playlist_to_user(user_service, user_factory):
    user = user_factory.create_user(
        username="Arnold",
        password="topsicret",
        playlist_name="The best of the best of the best1"
    )
    user_service.add_user(user)

    response = user_service.add_playlist(user)

    assert response.status_code == 200

    response_data = response.json()
    print(response_data)
    assert response_data["data"] == user.playlists[0].name
    assert response_data["message"] == "OK"


def test_validate_existing_playlist_should_return_error(user_service, user_factory):
    user = user_factory.create_user(
        username="test_username2",
        password="TestPassword2",
        playlist_name="NewPlaylist"
    )
    user_service.add_user(user)
    user_service.add_playlist(user)

    response = user_service.add_playlist(user)

    assert response.status_code == 200

    response_data = response.json()
    assert response_data["error"] == f"{user.playlists[0].name} already a playlist of {user.user_name}"


def test_add_new_friend_to_user(user_service, user_factory):
    user = user_factory.create_user(
        username="TestUsername",
        password="TestPassword",
    )
    user_service.add_user(user)
    response = user_service.add_friend(user, "Savi1112")
    assert response.status_code == 200

    response_data = response.json()
    assert response_data["data"] == "Savi1112"
    assert response_data["message"] == "OK"


def test_validate_existing_friend_should_return_error(user_service, user_factory):
    user = user_factory.create_user(
        username="TestUsername",
        password="TestPassword",
    )
    user_service.add_user(user)
    response = user_service.add_friend(user, "Savi111")
    assert response.status_code == 200

    response_data = response.json()
    assert response_data["error"] == f'Savi111 already a friend of {user.user_name}'
