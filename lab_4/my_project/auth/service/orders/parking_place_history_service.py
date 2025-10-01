from my_project.auth.dao.orders.parking_place_history_dao import ParkingPlaceHistoryDAO
from my_project.auth.domain.orders.parking_place_history import ParkingPlaceHistory


class ParkingPlaceHistoryService:
    def __init__(self):
        self._dao = ParkingPlaceHistoryDAO()

    def get_all_parking_place_histories(self):
        return self._dao.find_all()

    def create_parking_place_history(self, history: ParkingPlaceHistory):
        return self._dao.create(history)

    def find_by_id(self, history_id: int):
        return self._dao.find_by_id(history_id)

    def update_parking_place_history(self, history_id: int, history: ParkingPlaceHistory):
        return self._dao.update(history_id, history)

    def delete_parking_place_history(self, history_id: int):
        return self._dao.delete(history_id)
