from my_project.auth.dao.orders.parking_network_dao import ParkingNetworkDAO
from my_project.auth.domain.orders.parking_network import ParkingNetwork


class ParkingNetworkService:
    def __init__(self):
        self._dao = ParkingNetworkDAO()

    def get_all_parking_networks(self):
        return self._dao.find_all()

    def create_parking_network(self, parking_network: ParkingNetwork):
        return self._dao.create(parking_network)

    def find_by_id(self, parking_network_id: int):
        return self._dao.find_by_id(parking_network_id)

    def update_parking_network(self, parking_network_id: int, parking_network: ParkingNetwork):
        return self._dao.update(parking_network_id, parking_network)

    def delete_parking_network(self, parking_network_id: int):
        return self._dao.delete(parking_network_id)
