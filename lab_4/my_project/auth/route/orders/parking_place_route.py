from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import parking_place_controller
from my_project.auth.domain.orders.parking_place import ParkingPlace

parking_place_bp = Blueprint('parking_place', __name__, url_prefix='/parking_places')


@parking_place_bp.route('', methods=['GET'])
def get_all_parking_places() -> Response:
    parking_places = parking_place_controller.find_all()
    parking_place_dto = [parking_place.put_into_dto() for parking_place in parking_places]
    return make_response(jsonify(parking_place_dto), HTTPStatus.OK)


@parking_place_bp.route('', methods=['POST'])
def create_parking_place() -> Response:
    content = request.get_json()
    parking_place = ParkingPlace.create_from_dto(content)
    parking_place_controller.create_parking_place(parking_place)
    return make_response(jsonify(parking_place.put_into_dto()), HTTPStatus.CREATED)


@parking_place_bp.route('/<int:parking_place_id>', methods=['GET'])
def get_parking_place_by_id(parking_place_id: int) -> Response:
    parking_place = parking_place_controller.find_by_id(parking_place_id)
    if parking_place:
        return make_response(jsonify(parking_place.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Parking Place not found"}), HTTPStatus.NOT_FOUND)


@parking_place_bp.route('/<int:parking_place_id>', methods=['PUT'])
def update_parking_place(parking_place_id: int) -> Response:
    content = request.get_json()
    parking_place = ParkingPlace.create_from_dto(content)
    parking_place_controller.update_parking_place(parking_place_id, parking_place)
    return make_response("Parking Place updated", HTTPStatus.OK)


@parking_place_bp.route('/<int:parking_place_id>', methods=['DELETE'])
def delete_parking_place(parking_place_id: int) -> Response:
    parking_place_controller.delete_parking_place(parking_place_id)
    return make_response("Parking Place deleted", HTTPStatus.NO_CONTENT)
