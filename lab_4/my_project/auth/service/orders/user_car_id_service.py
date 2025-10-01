from my_project.auth.dao.orders.user_car_id_dao import UserCarIdDAO
from my_project.auth.domain.orders.user_car_id import UserCarId


class UserCarIdService:
    def __init__(self):
        self._dao = UserCarIdDAO()

    def get_all_user_car_ids(self):
        return self._dao.find_all()

    def create_user_car_id(self, user_car_id: UserCarId):
        return self._dao.create(user_car_id)

    def find_by_user_and_car_id(self, user_id: int, car_id: int):
        return self._dao.find_by_two_id(user_id, car_id)

    def update_user_car_id(self, user_id: int, car_id: int, user_car_id: UserCarId):
        return self._dao.update_by_two_id((user_id, car_id), user_car_id)

    def delete_user_car_id(self, user_id: int, car_id: int):
        return self._dao.delete((user_id, car_id))
