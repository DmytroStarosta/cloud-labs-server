from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.parking_place_history import ParkingPlaceHistory


class ParkingPlaceHistoryDAO(GeneralDAO):
    _domain_type = ParkingPlaceHistory
