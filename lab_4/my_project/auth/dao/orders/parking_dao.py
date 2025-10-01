from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.parking import Parking


class ParkingDAO(GeneralDAO):
    _domain_type = Parking
