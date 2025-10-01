from .orders.user_dao import UserDAO
from .orders.user_type_dao import UserTypeDAO
from .orders.cars_dao import CarsDAO
from .orders.user_car_id_dao import UserCarIdDAO
from .orders.parking_dao import ParkingDAO
from .orders.parking_place_dao import ParkingPlaceDAO
from .orders.parking_place_history_dao import ParkingPlaceHistoryDAO
from .orders.reservations_dao import ReservationsDAO
from .orders.status_type_dao import StatusTypeDAO
from .orders.address_dao import AddressDAO
from .orders.owner_dao import OwnerDAO
from .orders.parking_network_dao import ParkingNetworkDAO
from .orders.type_of_voucher_dao import TypeOfVoucherDAO
from .orders.voucher_dao import VoucherDAO

user_dao = UserDAO()
user_type_dao = UserTypeDAO()
cars_dao = CarsDAO()
user_car_id_dao = UserCarIdDAO()
parking_dao = ParkingDAO()
parking_place_dao = ParkingPlaceDAO()
parking_place_history_dao = ParkingPlaceHistoryDAO()
reservations_dao = ReservationsDAO()
status_type_dao = StatusTypeDAO()
address_dao = AddressDAO()
owner_dao = OwnerDAO()
parking_network_dao = ParkingNetworkDAO()
type_of_voucher_dao = TypeOfVoucherDAO()
voucher_dao = VoucherDAO()
