from my_project.auth.dao.orders.address_dao import AddressDAO
from my_project.auth.domain.orders.address import Address


class AddressService:
    def __init__(self):
        self._dao = AddressDAO()

    def get_all_addresses(self):
        return self._dao.find_all()

    def create_address(self, address: Address):
        return self._dao.create(address)

    def find_by_id(self, address_id: int):
        return self._dao.find_by_id(address_id)

    def update_address(self, address_id: int, address: Address):
        return self._dao.update(address_id, address)

    def delete_address(self, address_id: int):
        return self._dao.delete(address_id)
