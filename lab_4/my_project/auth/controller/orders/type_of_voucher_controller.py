from my_project.auth.service.orders.type_of_voucher_service import TypeOfVoucherService
from my_project.auth.domain.orders.type_of_voucher import TypeOfVoucher


class TypeOfVoucherController:
    def __init__(self):
        self._service = TypeOfVoucherService()

    def find_all(self):
        return self._service.get_all_types_of_vouchers()

    def create_type_of_voucher(self, type_of_voucher: TypeOfVoucher):
        return self._service.create_type_of_voucher(type_of_voucher)

    def find_by_id(self, type_of_voucher_id: int):
        return self._service.find_by_id(type_of_voucher_id)

    def update_type_of_voucher(self, type_of_voucher_id: int, type_of_voucher: TypeOfVoucher):
        return self._service.update_type_of_voucher(type_of_voucher_id, type_of_voucher)

    def delete_type_of_voucher(self, type_of_voucher_id: int):
        return self._service.delete_type_of_voucher(type_of_voucher_id)
