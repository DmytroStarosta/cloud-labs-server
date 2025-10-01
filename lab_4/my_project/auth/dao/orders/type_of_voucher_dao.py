from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.type_of_voucher import TypeOfVoucher


class TypeOfVoucherDAO(GeneralDAO):
    _domain_type = TypeOfVoucher
