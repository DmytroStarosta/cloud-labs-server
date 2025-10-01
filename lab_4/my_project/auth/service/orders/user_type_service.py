from typing import List
from my_project.auth.dao.orders.user_type_dao import UserTypeDAO
from my_project.auth.domain.orders.user_type import UserType


class UserTypeService:
    def __init__(self):
        self._dao = UserTypeDAO()

    def get_all_user_types(self) -> List[UserType]:
        return self._dao.find_all()

    def create_user_type(self, user_type: UserType) -> None:
        self._dao.create(user_type)

    def find_by_id(self, user_type_id: int) -> UserType:
        return self._dao.find_by_id(user_type_id)

    def update_user_type(self, user_type_id: int, user_type: UserType) -> None:
        self._dao.update(user_type_id, user_type)

    def delete_user_type(self, user_type_id: int) -> None:
        self._dao.delete(user_type_id)

    def find_by_type(self, type_name: str) -> List[UserType]:
        return self._dao.find_by_type(type_name)
