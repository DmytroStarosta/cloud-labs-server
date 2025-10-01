from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import type_of_voucher_controller
from my_project.auth.domain.orders.type_of_voucher import TypeOfVoucher

type_of_voucher_bp = Blueprint('type_of_voucher', __name__, url_prefix='/type_of_voucher')


@type_of_voucher_bp.route('', methods=['GET'])
def get_all_types_of_vouchers() -> Response:
    types_of_vouchers = type_of_voucher_controller.find_all()
    type_of_voucher_dto = [type_of_voucher.put_into_dto() for type_of_voucher in types_of_vouchers]
    return make_response(jsonify(type_of_voucher_dto), HTTPStatus.OK)


@type_of_voucher_bp.route('', methods=['POST'])
def create_type_of_voucher() -> Response:
    content = request.get_json()
    type_of_voucher = TypeOfVoucher.create_from_dto(content)
    type_of_voucher_controller.create_type_of_voucher(type_of_voucher)
    return make_response(jsonify(type_of_voucher.put_into_dto()), HTTPStatus.CREATED)


@type_of_voucher_bp.route('/<int:type_of_voucher_id>', methods=['GET'])
def get_type_of_voucher_by_id(type_of_voucher_id: int) -> Response:
    type_of_voucher = type_of_voucher_controller.find_by_id(type_of_voucher_id)
    if type_of_voucher:
        return make_response(jsonify(type_of_voucher.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Type of Voucher not found"}), HTTPStatus.NOT_FOUND)


@type_of_voucher_bp.route('/<int:type_of_voucher_id>', methods=['PUT'])
def update_type_of_voucher(type_of_voucher_id: int) -> Response:
    content = request.get_json()
    type_of_voucher = TypeOfVoucher.create_from_dto(content)
    type_of_voucher_controller.update_type_of_voucher(type_of_voucher_id, type_of_voucher)
    return make_response("Type of Voucher updated", HTTPStatus.OK)


@type_of_voucher_bp.route('/<int:type_of_voucher_id>', methods=['DELETE'])
def delete_type_of_voucher(type_of_voucher_id: int) -> Response:
    type_of_voucher_controller.delete_type_of_voucher(type_of_voucher_id)
    return make_response("Type of Voucher deleted", HTTPStatus.NO_CONTENT)
