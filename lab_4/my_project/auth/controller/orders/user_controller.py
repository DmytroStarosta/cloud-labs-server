from my_project.auth.service.orders.user_service import UserService

class UserController:
    def __init__(self):
        self._service = UserService()

    def find_all(self):
        return self._service.get_all_users()

    def create_user(self, user):
        return self._service.create_user(user)

    def find_by_id(self, user_id):
        return self._service.find_by_id(user_id)

    def update_user(self, user_id, user):
        return self._service.update_user(user_id, user)

    def delete_user(self, user_id):
        return self._service.delete_user(user_id)

    def find_by_surname(self, surname: str):
        return self._service.find_by_surname(surname)

    def get_users_by_email(self, email):
        return self._service.find_by_email(email)
