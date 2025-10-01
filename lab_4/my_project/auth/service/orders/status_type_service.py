from my_project.auth.dao.orders.status_type_dao import StatusTypeDAO
from my_project.auth.domain.orders.status_type import StatusType


class StatusTypeService:
    def __init__(self):
        self._dao = StatusTypeDAO()

    def get_all_status_types(self):
        return self._dao.find_all()

    def create_status_type(self, status_type: StatusType):
        return self._dao.create(status_type)

    def find_by_id(self, status_type_id: int):
        return self._dao.find_by_id(status_type_id)

    def update_status_type(self, status_type_id: int, status_type: StatusType):
        return self._dao.update(status_type_id, status_type)

    def delete_status_type(self, status_type_id: int):
        return self._dao.delete(status_type_id)
