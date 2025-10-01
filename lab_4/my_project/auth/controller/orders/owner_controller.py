from my_project.auth.service.orders.owner_service import OwnerService
from my_project.auth.domain.orders.owner import Owner


class OwnerController:
    def __init__(self):
        self._service = OwnerService()

    def find_all(self):
        return self._service.get_all_owners()

    def create_owner(self, owner: Owner):
        return self._service.create_owner(owner)

    def find_by_id(self, owner_id: int):
        return self._service.find_by_id(owner_id)

    def update_owner(self, owner_id: int, owner: Owner):
        return self._service.update_owner(owner_id, owner)

    def delete_owner(self, owner_id: int):
        return self._service.delete_owner(owner_id)
