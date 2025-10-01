from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.status_type import StatusType


class StatusTypeDAO(GeneralDAO):
    _domain_type = StatusType
