from my_project.auth.service.orders.voucher_service import VoucherService
from my_project.auth.domain.orders.voucher import Voucher


class VoucherController:
    def __init__(self):
        self._service = VoucherService()

    def find_all(self):
        return self._service.get_all_vouchers()

    def create_voucher(self, voucher: Voucher):
        return self._service.create_voucher(voucher)

    def find_by_id(self, voucher_id: int):
        return self._service.find_by_id(voucher_id)

    def update_voucher(self, voucher_id: int, voucher: Voucher):
        return self._service.update_voucher(voucher_id, voucher)

    def delete_voucher(self, voucher_id: int):
        return self._service.delete_voucher(voucher_id)
