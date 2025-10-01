from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import parking_place_history_controller
from my_project.auth.domain.orders.parking_place_history import ParkingPlaceHistory

parking_place_history_bp = Blueprint('parking_place_history', __name__, url_prefix='/parking_place_histories')


@parking_place_history_bp.route('', methods=['GET'])
def get_all_parking_place_histories() -> Response:
    histories = parking_place_history_controller.find_all()
    histories_dto = [history.put_into_dto() for history in histories]
    return make_response(jsonify(histories_dto), HTTPStatus.OK)


@parking_place_history_bp.route('', methods=['POST'])
def create_parking_place_history() -> Response:
    content = request.get_json()
    history = ParkingPlaceHistory.create_from_dto(content)
    parking_place_history_controller.create_parking_place_history(history)
    return make_response(jsonify(history.put_into_dto()), HTTPStatus.CREATED)


@parking_place_history_bp.route('/<int:history_id>', methods=['GET'])
def get_parking_place_history_by_id(history_id: int) -> Response:
    history = parking_place_history_controller.find_by_id(history_id)
    if history:
        return make_response(jsonify(history.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Parking Place History not found"}), HTTPStatus.NOT_FOUND)


@parking_place_history_bp.route('/<int:history_id>', methods=['PUT'])
def update_parking_place_history(history_id: int) -> Response:
    content = request.get_json()
    history = ParkingPlaceHistory.create_from_dto(content)
    parking_place_history_controller.update_parking_place_history(history_id, history)
    return make_response("Parking Place History updated", HTTPStatus.OK)


@parking_place_history_bp.route('/<int:history_id>', methods=['DELETE'])
def delete_parking_place_history(history_id: int) -> Response:
    parking_place_history_controller.delete_parking_place_history(history_id)
    return make_response("Parking Place History deleted", HTTPStatus.NO_CONTENT)
