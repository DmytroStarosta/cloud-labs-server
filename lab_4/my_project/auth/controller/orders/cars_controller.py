from my_project.auth.service.orders.cars_service import CarsService
from my_project.auth.domain.orders.cars import Cars


class CarController:
    def __init__(self):
        self._service = CarsService()

    def find_all(self):
        return self._service.get_all_cars()

    def create_car(self, car: Cars):
        return self._service.create_car(car)

    def find_by_id(self, car_id: int):
        return self._service.find_by_id(car_id)

    def update_car(self, car_id: int, car: Cars):
        return self._service.update_car(car_id, car)

    def delete_car(self, car_id: int):
        return self._service.delete_car(car_id)
