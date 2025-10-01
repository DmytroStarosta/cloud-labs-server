from my_project.auth.service.orders.parking_service import ParkingService
from my_project.auth.domain.orders.parking import Parking


class ParkingController:
    def __init__(self):
        self._service = ParkingService()

    def find_all(self):
        return self._service.get_all_parkings()

    def create_parking(self, parking: Parking):
        return self._service.create_parking(parking)

    def find_by_id(self, parking_id: int):
        return self._service.find_by_id(parking_id)

    def update_parking(self, parking_id: int, parking: Parking):
        return self._service.update_parking(parking_id, parking)

    def delete_parking(self, parking_id: int):
        return self._service.delete_parking(parking_id)
