from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.reservations import Reservations


class ReservationsDAO(GeneralDAO):
    _domain_type = Reservations
