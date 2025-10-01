from .orders.user_service import UserService
from .orders.user_type_service import UserTypeService
from .orders.cars_service import CarsService
from .orders.user_car_id_service import UserCarIdService
from .orders.parking_service import ParkingService
from .orders.parking_place_service import ParkingPlaceService
from .orders.parking_place_history_service import ParkingPlaceHistoryService
from .orders.reservations_service import ReservationsService
from .orders.status_type_service import StatusTypeService
from .orders.address_service import AddressService
from .orders.owner_service import OwnerService
from .orders.parking_network_service import ParkingNetworkService
from .orders.type_of_voucher_service import TypeOfVoucherService
from .orders.voucher_service import VoucherService

user_service = UserService()
user_type_service = UserTypeService()
cars_service = CarsService()
user_car_id_service = UserCarIdService()
parking_service = ParkingService()
parking_place_service = ParkingPlaceService()
parking_place_history_service = ParkingPlaceHistoryService()
reservations_service = ReservationsService()
status_type_service = StatusTypeService()
address_service = AddressService()
owner_service = OwnerService()
parking_network_service = ParkingNetworkService()
type_of_voucher_service = TypeOfVoucherService()
voucher_service = VoucherService()


def user_service():
    return None