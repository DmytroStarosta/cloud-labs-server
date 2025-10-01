from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.parking_network import ParkingNetwork


class ParkingNetworkDAO(GeneralDAO):
    _domain_type = ParkingNetwork
