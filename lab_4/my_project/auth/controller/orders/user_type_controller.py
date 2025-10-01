from my_project.auth.service.orders.user_type_service import UserTypeService


class UserTypeController:
    def __init__(self):
        self._service = UserTypeService()

    def find_all(self):
        return self._service.get_all_user_types()

    def create_user_type(self, user_type):
        return self._service.create_user_type(user_type)

    def find_by_id(self, user_type_id):
        return self._service.find_by_id(user_type_id)

    def update_user_type(self, user_type_id, user_type):
        return self._service.update_user_type(user_type_id, user_type)

    def delete_user_type(self, user_type_id):
        return self._service.delete_user_type(user_type_id)

    def get_user_types_by_name(self, type_name):
        return self._service.find_by_type(type_name)
