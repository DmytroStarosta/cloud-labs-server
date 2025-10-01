from my_project.auth.dao.orders.type_of_voucher_dao import TypeOfVoucherDAO
from my_project.auth.domain.orders.type_of_voucher import TypeOfVoucher


class TypeOfVoucherService:
    def __init__(self):
        self._dao = TypeOfVoucherDAO()

    def get_all_types_of_vouchers(self):
        return self._dao.find_all()

    def create_type_of_voucher(self, type_of_voucher: TypeOfVoucher):
        return self._dao.create(type_of_voucher)

    def find_by_id(self, type_of_voucher_id: int):
        return self._dao.find_by_id(type_of_voucher_id)

    def update_type_of_voucher(self, type_of_voucher_id: int, type_of_voucher: TypeOfVoucher):
        return self._dao.update(type_of_voucher_id, type_of_voucher)

    def delete_type_of_voucher(self, type_of_voucher_id: int):
        return self._dao.delete(type_of_voucher_id)
