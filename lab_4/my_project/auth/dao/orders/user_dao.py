from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.user import User


class UserDAO(GeneralDAO):
    _domain_type = User

    def create(self, user: User) -> None:
        self._session.add(user)
        self._session.commit()

    def find_all(self) -> List[User]:
        return self._session.query(User).all()

    def find_by_email(self, email: str) -> List[User]:
        return self._session.query(User).filter(User.email == email).order_by(User.email).all()  # reviewed

    def find_by_name(self, name: str) -> List[User]:
        return self._session.query(User).filter(User.name == name).order_by(User.name).all()  # reviewed

    def find_by_surname(self, surname: str):
        return self._session.query(User).filter_by(surname=surname).all()
