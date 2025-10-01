from my_project.auth.dao.orders.cars_dao import CarsDAO
from my_project.auth.domain.orders.cars import Cars


class CarsService:
    def __init__(self):
        self._dao = CarsDAO()

    def get_all_cars(self):
        return self._dao.find_all()

    def create_car(self, car: Cars):
        return self._dao.create(car)

    def find_by_id(self, car_id: int):
        return self._dao.find_by_id(car_id)

    def update_car(self, car_id: int, car: Cars):
        return self._dao.update(car_id, car)

    def delete_car(self, car_id: int):
        return self._dao.delete(car_id)
