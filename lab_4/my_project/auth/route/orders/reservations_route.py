from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import reservations_controller
from my_project.auth.domain.orders.reservations import Reservations

reservations_bp = Blueprint('reservations', __name__, url_prefix='/reservations')


@reservations_bp.route('', methods=['GET'])
def get_all_reservations() -> Response:
    reservations = reservations_controller.find_all()
    reservations_dto = [reservation.put_into_dto() for reservation in reservations]
    return make_response(jsonify(reservations_dto), HTTPStatus.OK)


@reservations_bp.route('', methods=['POST'])
def create_reservation() -> Response:
    content = request.get_json()
    reservation = Reservations.create_from_dto(content)
    reservations_controller.create_reservation(reservation)
    return make_response(jsonify(reservation.put_into_dto()), HTTPStatus.CREATED)


@reservations_bp.route('/<int:reservation_id>', methods=['GET'])
def get_reservation_by_id(reservation_id: int) -> Response:
    reservation = reservations_controller.find_by_id(reservation_id)
    if reservation:
        return make_response(jsonify(reservation.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Reservation not found"}), HTTPStatus.NOT_FOUND)


@reservations_bp.route('/<int:reservation_id>', methods=['PUT'])
def update_reservation(reservation_id: int) -> Response:
    content = request.get_json()
    reservation = Reservations.create_from_dto(content)
    reservations_controller.update_reservation(reservation_id, reservation)
    return make_response("Reservation updated", HTTPStatus.OK)


@reservations_bp.route('/<int:reservation_id>', methods=['DELETE'])
def delete_reservation(reservation_id: int) -> Response:
    reservations_controller.delete_reservation(reservation_id)
    return make_response