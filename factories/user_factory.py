from models.user import UserModel


class UserFactory:
    @staticmethod
    def create_user(username, user_password):
        # Return the UserModel object as it is
        return UserModel(user_name=username, user_password=user_password)

    @staticmethod
    def get_user():
        # Return a hardcoded user response
        user_data = UserModel(
            user_name="user_name",
            user_password="user_password"
        )
        return user_data

