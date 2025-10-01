from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.address import Address


class AddressDAO(GeneralDAO):
    _domain_type = Address
