from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.parking_place import ParkingPlace


class ParkingPlaceDAO(GeneralDAO):
    _domain_type = ParkingPlace
