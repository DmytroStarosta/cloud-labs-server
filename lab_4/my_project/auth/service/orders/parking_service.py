from my_project.auth.dao.orders.parking_dao import ParkingDAO
from my_project.auth.domain.orders.parking import Parking


class ParkingService:
    def __init__(self):
        self._dao = ParkingDAO()

    def get_all_parkings(self):
        return self._dao.find_all()

    def create_parking(self, parking: Parking):
        return self._dao.create(parking)

    def find_by_id(self, parking_id: int):
        return self._dao.find_by_id(parking_id)

    def update_parking(self, parking_id: int, parking: Parking):
        return self._dao.update(parking_id, parking)

    def delete_parking(self, parking_id: int):
        return self._dao.delete(parking_id)
