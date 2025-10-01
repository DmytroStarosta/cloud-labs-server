from my_project.auth.dao.orders.user_dao import UserDAO

class UserService:
    def __init__(self):
        self._dao = UserDAO()

    def get_all_users(self):
        return self._dao.find_all()

    def create_user(self, user):
        return self._dao.create(user)

    def find_by_id(self, user_id):
        return self._dao.find_by_id(user_id)

    def update_user(self, user_id, user):
        return self._dao.update(user_id, user)

    def delete_user(self, user_id):
        return self._dao.delete(user_id)

    def find_by_surname(self, surname: str):
        return self._dao.find_by_surname(surname)

    def find_by_email(self, email):
        return self._dao.find_by_email(email)
