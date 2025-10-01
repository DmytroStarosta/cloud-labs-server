from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.cars import Cars


class CarsDAO(GeneralDAO):
    _domain_type = Cars
