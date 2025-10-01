from my_project.auth.dao.orders.voucher_dao import VoucherDAO
from my_project.auth.domain.orders.voucher import Voucher


class VoucherService:
    def __init__(self):
        self._dao = VoucherDAO()

    def get_all_vouchers(self):
        return self._dao.find_all()

    def create_voucher(self, voucher: Voucher):
        return self._dao.create(voucher)

    def find_by_id(self, voucher_id: int):
        return self._dao.find_by_id(voucher_id)

    def update_voucher(self, voucher_id: int, voucher: Voucher):
        return self._dao.update(voucher_id, voucher)

    def delete_voucher(self, voucher_id: int):
        return self._dao.delete(voucher_id)
