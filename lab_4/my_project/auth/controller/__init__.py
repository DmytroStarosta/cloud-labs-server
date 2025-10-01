from .orders.user_controller import UserController
from .orders.user_type_controller import UserTypeController
from .orders.cars_controller import CarController
from .orders.user_car_id_controller import UserCarIdController
from .orders.parking_controller import ParkingController
from .orders.parking_place_controller import ParkingPlaceController
from .orders.parking_place_history_controller import ParkingPlaceHistoryController
from .orders.reservations_controller import ReservationsController
from .orders.status_type_controller import StatusTypeController
from .orders.address_controller import AddressController
from .orders.owner_controller import OwnerController
from .orders.parking_network_controller import ParkingNetworkController
from .orders.type_of_voucher_controller import TypeOfVoucherController
from .orders.voucher_controller import VoucherController


user_controller = UserController()
user_type_controller = UserTypeController()
cars_controller = CarController()
user_car_id_controller = UserCarIdController()
parking_controller = ParkingController()
parking_place_controller = ParkingPlaceController()
parking_place_history_controller = ParkingPlaceHistoryController()
reservations_controller = ReservationsController()
status_type_controller = StatusTypeController()
address_controller = AddressController()
owner_controller = OwnerController()
parking_network_controller = ParkingNetworkController()
type_of_voucher_controller = TypeOfVoucherController()
voucher_controller = VoucherController()
