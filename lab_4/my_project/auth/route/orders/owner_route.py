from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import owner_controller
from my_project.auth.domain.orders.owner import Owner

owner_bp = Blueprint('owner', __name__, url_prefix='/owners')


@owner_bp.route('', methods=['GET'])
def get_all_owners() -> Response:
    owners = owner_controller.find_all()
    owner_dto = [owner.put_into_dto() for owner in owners]
    return make_response(jsonify(owner_dto), HTTPStatus.OK)


@owner_bp.route('', methods=['POST'])
def create_owner() -> Response:
    content = request.get_json()
    owner = Owner.create_from_dto(content)
    owner_controller.create_owner(owner)
    return make_response(jsonify(owner.put_into_dto()), HTTPStatus.CREATED)


@owner_bp.route('/<int:owner_id>', methods=['GET'])
def get_owner_by_id(owner_id: int) -> Response:
    owner = owner_controller.find_by_id(owner_id)
    if owner:
        return make_response(jsonify(owner.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Owner not found"}), HTTPStatus.NOT_FOUND)


@owner_bp.route('/<int:owner_id>', methods=['PUT'])
def update_owner(owner_id: int) -> Response:
    content = request.get_json()
    owner = Owner.create_from_dto(content)
    owner_controller.update_owner(owner_id, owner)
    return make_response("Owner updated", HTTPStatus.OK)


@owner_bp.route('/<int:owner_id>', methods=['DELETE'])
def delete_owner(owner_id: int) -> Response:
    owner_controller.delete_owner(owner_id)
    return make_response("Owner deleted", HTTPStatus.NO_CONTENT)
