from my_project.auth.dao.orders.owner_dao import OwnerDAO
from my_project.auth.domain.orders.owner import Owner


class OwnerService:
    def __init__(self):
        self._dao = OwnerDAO()

    def get_all_owners(self):
        return self._dao.find_all()

    def create_owner(self, owner: Owner):
        return self._dao.create(owner)

    def find_by_id(self, owner_id: int):
        return self._dao.find_by_id(owner_id)

    def update_owner(self, owner_id: int, owner: Owner):
        return self._dao.update(owner_id, owner)

    def delete_owner(self, owner_id: int):
        return self._dao.delete(owner_id)
