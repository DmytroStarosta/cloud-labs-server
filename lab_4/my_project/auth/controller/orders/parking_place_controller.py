from my_project.auth.service.orders.parking_place_service import ParkingPlaceService
from my_project.auth.domain.orders.parking_place import ParkingPlace


class ParkingPlaceController:
    def __init__(self):
        self._service = ParkingPlaceService()

    def find_all(self):
        return self._service.get_all_parking_places()

    def create_parking_place(self, parking_place: ParkingPlace):
        return self._service.create_parking_place(parking_place)

    def find_by_id(self, parking_place_id: int):
        return self._service.find_by_id(parking_place_id)

    def update_parking_place(self, parking_place_id: int, parking_place: ParkingPlace):
        return self._service.update_parking_place(parking_place_id, parking_place)

    def delete_parking_place(self, parking_place_id: int):
        return self._service.delete_parking_place(parking_place_id)
