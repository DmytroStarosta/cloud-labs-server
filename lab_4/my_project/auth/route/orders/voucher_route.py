from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import voucher_controller
from my_project.auth.domain.orders.voucher import Voucher

voucher_bp = Blueprint('voucher', __name__, url_prefix='/voucher')


@voucher_bp.route('', methods=['GET'])
def get_all_vouchers() -> Response:
    vouchers = voucher_controller.find_all()
    voucher_dto = [voucher.put_into_dto() for voucher in vouchers]
    return make_response(jsonify(voucher_dto), HTTPStatus.OK)


@voucher_bp.route('', methods=['POST'])
def create_voucher() -> Response:
    content = request.get_json()
    voucher = Voucher.create_from_dto(content)
    voucher_controller.create_voucher(voucher)
    return make_response(jsonify(voucher.put_into_dto()), HTTPStatus.CREATED)


@voucher_bp.route('/<int:voucher_id>', methods=['GET'])
def get_voucher_by_id(voucher_id: int) -> Response:
    voucher = voucher_controller.find_by_id(voucher_id)
    if voucher:
        return make_response(jsonify(voucher.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Voucher not found"}), HTTPStatus.NOT_FOUND)


@voucher_bp.route('/<int:voucher_id>', methods=['PUT'])
def update_voucher(voucher_id: int) -> Response:
    content = request.get_json()
    voucher = Voucher.create_from_dto(content)
    voucher_controller.update_voucher(voucher_id, voucher)
    return make_response("Voucher updated", HTTPStatus.OK)


@voucher_bp.route('/<int:voucher_id>', methods=['DELETE'])
def delete_voucher(voucher_id: int) -> Response:
    voucher_controller.delete_voucher(voucher_id)
    return make_response("Voucher deleted", HTTPStatus.NO_CONTENT)
