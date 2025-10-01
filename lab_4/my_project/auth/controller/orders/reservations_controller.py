from my_project.auth.service.orders.reservations_service import ReservationsService
from my_project.auth.domain.orders.reservations import Reservations


class ReservationsController:
    def __init__(self):
        self._service = ReservationsService()

    def find_all(self):
        return self._service.get_all_reservations()

    def create_reservation(self, reservation: Reservations):
        return self._service.create_reservation(reservation)

    def find_by_id(self, reservation_id: int):
        return self._service.find_by_id(reservation_id)

    def update_reservation(self, reservation_id: int, reservation: Reservations):
        return self._service.update_reservation(reservation_id, reservation)

    def delete_reservation(self, reservation_id: int):
        return self._service.delete_reservation(reservation_id)
