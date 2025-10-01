from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import address_controller
from my_project.auth.domain.orders.address import Address

address_bp = Blueprint('address', __name__, url_prefix='/address')


@address_bp.route('', methods=['GET'])
def get_all_addresses() -> Response:
    addresses = address_controller.find_all()
    address_dto = [address.put_into_dto() for address in addresses]
    return make_response(jsonify(address_dto), HTTPStatus.OK)


@address_bp.route('', methods=['POST'])
def create_address() -> Response:
    content = request.get_json()
    address = Address.create_from_dto(content)
    address_controller.create_address(address)
    return make_response(jsonify(address.put_into_dto()), HTTPStatus.CREATED)


@address_bp.route('/<int:address_id>', methods=['GET'])
def get_address_by_id(address_id: int) -> Response:
    address = address_controller.find_by_id(address_id)
    if address:
        return make_response(jsonify(address.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Address not found"}), HTTPStatus.NOT_FOUND)


@address_bp.route('/<int:address_id>', methods=['PUT'])
def update_address(address_id: int) -> Response:
    content = request.get_json()
    address = Address.create_from_dto(content)
    address_controller.update_address(address_id, address)
    return make_response("Address updated", HTTPStatus.OK)


@address_bp.route('/<int:address_id>', methods=['DELETE'])
def delete_address(address_id: int) -> Response:
    address_controller.delete_address(address_id)
    return make_response("Address deleted", HTTPStatus.NO_CONTENT)
