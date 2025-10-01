from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.user_type import UserType


class UserTypeDAO(GeneralDAO):
    _domain_type = UserType

    def create(self, user_type: UserType) -> None:
        self._session.add(user_type)
        self._session.commit()

    def find_all(self) -> List[UserType]:
        return self._session.query(UserType).all()

    def find_by_id(self, user_type_id: int) -> UserType:
        return self._session.query(UserType).filter(UserType.id == user_type_id).first()

    def find_by_type(self, type_name: str) -> List[UserType]:
        return self._session.query(UserType).filter(UserType.type == type_name).order_by(UserType.type).all()
