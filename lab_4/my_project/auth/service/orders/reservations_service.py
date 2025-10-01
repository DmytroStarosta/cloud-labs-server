from my_project.auth.dao.orders.reservations_dao import ReservationsDAO
from my_project.auth.domain.orders.reservations import Reservations


class ReservationsService:
    def __init__(self):
        self._dao = ReservationsDAO()

    def get_all_reservations(self):
        return self._dao.find_all()

    def create_reservation(self, reservation: Reservations):
        return self._dao.create(reservation)

    def find_by_id(self, reservation_id: int):
        return self._dao.find_by_id(reservation_id)

    def update_reservation(self, reservation_id: int, reservation: Reservations):
        return self._dao.update(reservation_id, reservation)

    def delete_reservation(self, reservation_id: int):
        return self._dao.delete(reservation_id)
