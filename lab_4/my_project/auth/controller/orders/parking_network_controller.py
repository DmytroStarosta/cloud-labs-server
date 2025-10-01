from my_project.auth.service.orders.parking_network_service import ParkingNetworkService
from my_project.auth.domain.orders.parking_network import ParkingNetwork


class ParkingNetworkController:
    def __init__(self):
        self._service = ParkingNetworkService()

    def find_all(self):
        return self._service.get_all_parking_networks()

    def create_parking_network(self, parking_network: ParkingNetwork):
        return self._service.create_parking_network(parking_network)

    def find_by_id(self, parking_network_id: int):
        return self._service.find_by_id(parking_network_id)

    def update_parking_network(self, parking_network_id: int, parking_network: ParkingNetwork):
        return self._service.update_parking_network(parking_network_id, parking_network)

    def delete_parking_network(self, parking_network_id: int):
        return self._service.delete_parking_network(parking_network_id)
