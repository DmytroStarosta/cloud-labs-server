from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.voucher import Voucher


class VoucherDAO(GeneralDAO):
    _domain_type = Voucher
