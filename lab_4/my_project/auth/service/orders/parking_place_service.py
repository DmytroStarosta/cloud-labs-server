from my_project.auth.dao.orders.parking_place_dao import ParkingPlaceDAO
from my_project.auth.domain.orders.parking_place import ParkingPlace


class ParkingPlaceService:
    def __init__(self):
        self._dao = ParkingPlaceDAO()

    def get_all_parking_places(self):
        return self._dao.find_all()

    def create_parking_place(self, parking_place: ParkingPlace):
        return self._dao.create(parking_place)

    def find_by_id(self, parking_place_id: int):
        return self._dao.find_by_id(parking_place_id)

    def update_parking_place(self, parking_place_id: int, parking_place: ParkingPlace):
        return self._dao.update(parking_place_id, parking_place)

    def delete_parking_place(self, parking_place_id: int):
        return self._dao.delete(parking_place_id)
