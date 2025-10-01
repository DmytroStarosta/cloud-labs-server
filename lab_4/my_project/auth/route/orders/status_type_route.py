from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import status_type_controller
from my_project.auth.domain.orders.status_type import StatusType

status_type_bp = Blueprint('status_type', __name__, url_prefix='/status_types')


@status_type_bp.route('', methods=['GET'])
def get_all_status_types() -> Response:
    status_types = status_type_controller.find_all()
    status_type_dto = [status_type.put_into_dto() for status_type in status_types]
    return make_response(jsonify(status_type_dto), HTTPStatus.OK)


@status_type_bp.route('', methods=['POST'])
def create_status_type() -> Response:
    content = request.get_json()
    status_type = StatusType.create_from_dto(content)
    status_type_controller.create_status_type(status_type)
    return make_response(jsonify(status_type.put_into_dto()), HTTPStatus.CREATED)


@status_type_bp.route('/<int:status_type_id>', methods=['GET'])
def get_status_type_by_id(status_type_id: int) -> Response:
    status_type = status_type_controller.find_by_id(status_type_id)
    if status_type:
        return make_response(jsonify(status_type.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Status Type not found"}), HTTPStatus.NOT_FOUND)


@status_type_bp.route('/<int:status_type_id>', methods=['PUT'])
def update_status_type(status_type_id: int) -> Response:
    content = request.get_json()
    status_type = StatusType.create_from_dto(content)
    status_type_controller.update_status_type(status_type_id, status_type)
    return make_response("Status Type updated", HTTPStatus.OK)


@status_type_bp.route('/<int:status_type_id>', methods=['DELETE'])
def delete_status_type(status_type_id: int) -> Response:
    status_type_controller.delete_status_type(status_type_id)
    return make_response("Status Type deleted", HTTPStatus.NO_CONTENT)
