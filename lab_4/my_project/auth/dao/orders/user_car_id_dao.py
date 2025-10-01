from sqlalchemy import inspect
from sqlalchemy.orm import Mapper
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.user_car_id import UserCarId


class UserCarIdDAO(GeneralDAO):
    _domain_type = UserCarId

    def find_by_two_id(self, user_id: int, car_id: int) -> object:
        return self._session.query(self._domain_type).filter(
            self._domain_type.user_id == user_id,
            self._domain_type.car_id == car_id
        ).one()

    def update_by_two_id(self, keys: tuple[int], in_obj: object) -> None:
        domain_obj = self._session.query(self._domain_type).filter(
            self._domain_type.user_id == keys[0],
            self._domain_type.car_id == keys[1]
        ).one()
        mapper: Mapper = inspect(type(in_obj))
        columns = mapper.columns._collection
        for column_name, column_obj, *_ in columns:
            value = getattr(in_obj, column_name)
            setattr(domain_obj, column_name, value)
        self._session.commit()


