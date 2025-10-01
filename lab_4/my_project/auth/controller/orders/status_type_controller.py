from my_project.auth.service.orders.status_type_service import StatusTypeService
from my_project.auth.domain.orders.status_type import StatusType


class StatusTypeController:
    def __init__(self):
        self._service = StatusTypeService()

    def find_all(self):
        return self._service.get_all_status_types()

    def create_status_type(self, status_type: StatusType):
        return self._service.create_status_type(status_type)

    def find_by_id(self, status_type_id: int):
        return self._service.find_by_id(status_type_id)

    def update_status_type(self, status_type_id: int, status_type: StatusType):
        return self._service.update_status_type(status_type_id, status_type)

    def delete_status_type(self, status_type_id: int):
        return self._service.delete_status_type(status_type_id)
