from logger import logger


def test_create_user(delete_all_users, user_service, user_factory):
    user = user_factory.create_user(
        username="testUser",
        password="testUserPassword"
    )
    logger.debug(f"Creating user with payload: {user}")
    response = user_service.add_user(user)
    logger.debug(f"Response status: {response.status_code}")
    logger.debug(f"Response body: {response.json()}")

    assert response.status_code == 200

    response_data = response.json()
    assert response_data["data"] == user.user_name
    assert response_data["message"] == "OK"


def test_validate_existing_user(user_service, user_factory):
    user = user_factory.create_user(
        username="testUser1",
        password="testUserPassword1"
    )

    user_service.add_user(user)
    response_user_already_exist = user_service.add_user(user)

    assert response_user_already_exist.status_code == 200

    response_data = response_user_already_exist.json()
    assert "error" in response_data
    assert response_data["error"] == f"user with name {user.user_name} already exists."


def test_get_user(user_service, user_factory):
    user = user_factory.create_user('bomboclat', '123456')
    user_service.add_user(user)
    response = user_service.get_user(user)
    data_response = response.json()

    assert response.status_code == 200
    assert data_response['data']['user_name'] == user.user_name
    assert data_response['message'] == "OK"

    response = user_service.get_user(user)
    response_data = response.json()
    print(response_data)

    assert response.status_code == 200
    assert response_data['data']['user_name'] == user.user_name
    assert response_data['message'] == "OK"


def test_add_playlist_to_user(user_service, user_factory):
    user = user_factory.create_user(
        username="Arnold",
        password="topsicret",
        playlist_name="The best of the best of the best5555"
    )
    user_service.add_user(user)

    response = user_service.add_playlist(user)

    assert response.status_code == 200

    response_data = response.json()
    assert response_data["data"] == user.playlists[0].name
    assert response_data["message"] == "OK"


def test_add_playlist_to_user_with_wrong_user_password(user_service, user_factory):
    user = user_factory.create_user(
        username="Arnold",
        password="123456",
        playlist_name="The best of the best of the best5555"
    )
    user_service.add_user(user)
    wrong_user = user_factory.create_user(
        username=user.user_name,
        password="wrong_password",
        playlist_name=user.playlists[0].name
    )

    response = user_service.add_playlist(wrong_user)

    assert response.status_code == 200

    response_data = response.json()
    assert response_data["error"] == "either the user name or the password are wrong"


def test_validate_adding_the_same_playlist_of_another_user(user_service, user_factory):
    user = user_factory.create_user(
        username="Arnold2",
        password="topsicret2",
        playlist_name="The best of the best of the best5555"
    )
    user_service.add_user(user)
    response = user_service.add_playlist(user)

    assert response.status_code == 200

    response_data = response.json()
    assert response_data["data"] == f"{user.playlists[0].name}"
    assert response_data['message'] == "OK"


def test_validate_existing_playlist_should_return_error(user_service, user_factory):
    user = user_factory.create_user(
        username="Arnold2",
        password="topsicret2",
        playlist_name="duplicate"
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
    response = user_service.add_friend(user, "Savi6")
    assert response.status_code == 200

    response_data = response.json()
    assert response_data["data"] == "Savi6"
    assert response_data["message"] == "OK"


def test_add_new_friend_to_user_with_wrong_user_password(user_service, user_factory):
    user = user_factory.create_user(
        username="TestUsername",
        password="TestPassword",
    )
    user_service.add_user(user)
    wrong_user = user_factory.create_user(
        username=user.user_name,
        password="wrong_password"
    )

    response = user_service.add_friend(wrong_user, "wrong")

    response_data = response.json()
    assert response.status_code == 200
    assert response_data['error'] == "either the user name or the password are wrong"


def test_validate_existing_friend_should_return_error(user_service, user_factory):
    user = user_factory.create_user(
        username="TestUsernamex",
        password="TestPasswordx",
    )
    user_service.add_user(user)
    user_service.add_friend(user, friend_name="Savix")
    response = user_service.add_friend(user, friend_name="Savix")
    assert response.status_code == 200

    response_data = response.json()
    assert response_data["error"] == f'Savix already a friend of {user.user_name}'
