from my_project.auth.service.orders.address_service import AddressService
from my_project.auth.domain.orders.address import Address


class AddressController:
    def __init__(self):
        self._service = AddressService()

    def find_all(self):
        return self._service.get_all_addresses()

    def create_address(self, address: Address):
        return self._service.create_address(address)

    def find_by_id(self, address_id: int):
        return self._service.find_by_id(address_id)

    def update_address(self, address_id: int, address: Address):
        return self._service.update_address(address_id, address)

    def delete_address(self, address_id: int):
        return self._service.delete_address(address_id)
