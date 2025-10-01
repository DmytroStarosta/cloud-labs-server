from my_project.auth.service.orders.user_car_id_service import UserCarIdService
from my_project.auth.domain.orders.user_car_id import UserCarId


class UserCarIdController:
    def __init__(self):
        self._service = UserCarIdService()

    def find_all(self):
        return self._service.get_all_user_car_ids()

    def create_user_car_id(self, user_car_id: UserCarId):
        return self._service.create_user_car_id(user_car_id)

    def find_by_user_and_car_id(self, user_id: int, car_id: int):
        return self._service.find_by_user_and_car_id(user_id, car_id)

    def update_user_car_id(self, user_id: int, car_id: int, user_car_id: UserCarId):
        return self._service.update_user_car_id(user_id, car_id, user_car_id)

    def delete_user_car_id(self, user_id: int, car_id: int):
        return self._service.delete_user_car_id(user_id, car_id)
