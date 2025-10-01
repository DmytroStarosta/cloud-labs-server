from my_project.auth.service.orders.parking_place_history_service import ParkingPlaceHistoryService
from my_project.auth.domain.orders.parking_place_history import ParkingPlaceHistory


class ParkingPlaceHistoryController:
    def __init__(self):
        self._service = ParkingPlaceHistoryService()

    def find_all(self):
        return self._service.get_all_parking_place_histories()

    def create_parking_place_history(self, history: ParkingPlaceHistory):
        return self._service.create_parking_place_history(history)

    def find_by_id(self, history_id: int):
        return self._service.find_by_id(history_id)

    def update_parking_place_history(self, history_id: int, history: ParkingPlaceHistory):
        return self._service.update_parking_place_history(history_id, history)

    def delete_parking_place_history(self, history_id: int):
        return self._service.delete_parking_place_history(history_id)
