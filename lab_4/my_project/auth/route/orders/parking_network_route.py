from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import parking_network_controller
from my_project.auth.domain.orders.parking_network import ParkingNetwork

parking_network_bp = Blueprint('parking_network', __name__, url_prefix='/parking_networks')


@parking_network_bp.route('', methods=['GET'])
def get_all_parking_networks() -> Response:
    parking_networks = parking_network_controller.find_all()
    parking_network_dto = [network.put_into_dto() for network in parking_networks]
    return make_response(jsonify(parking_network_dto), HTTPStatus.OK)


@parking_network_bp.route('', methods=['POST'])
def create_parking_network() -> Response:
    content = request.get_json()
    parking_network = ParkingNetwork.create_from_dto(content)
    parking_network_controller.create_parking_network(parking_network)
    return make_response(jsonify(parking_network.put_into_dto()), HTTPStatus.CREATED)


@parking_network_bp.route('/<int:parking_network_id>', methods=['GET'])
def get_parking_network_by_id(parking_network_id: int) -> Response:
    parking_network = parking_network_controller.find_by_id(parking_network_id)
    if parking_network:
        return make_response(jsonify(parking_network.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Parking Network not found"}), HTTPStatus.NOT_FOUND)


@parking_network_bp.route('/<int:parking_network_id>', methods=['PUT'])
def update_parking_network(parking_network_id: int) -> Response:
    content = request.get_json()
    parking_network = ParkingNetwork.create_from_dto(content)
    parking_network_controller.update_parking_network(parking_network_id, parking_network)
    return make_response("Parking Network updated", HTTPStatus.OK)


@parking_network_bp.route('/<int:parking_network_id>', methods=['DELETE'])
def delete_parking_network(parking_network_id: int) -> Response:
    parking_network_controller.delete_parking_network(parking_network_id)
    return make_response("Parking Network deleted", HTTPStatus.NO_CONTENT)
