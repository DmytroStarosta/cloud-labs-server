from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import user_type_controller
from my_project.auth.domain.orders.user_type import UserType

user_types_bp = Blueprint('user_types', __name__, url_prefix='/user_types')


@user_types_bp.route('', methods=['GET'])
def get_all_user_types() -> Response:
    user_types = user_type_controller.find_all()
    user_type_dto = [user_type.put_into_dto() for user_type in user_types]
    return make_response(jsonify(user_type_dto), HTTPStatus.OK)


@user_types_bp.route('', methods=['POST'])
def create_user_type() -> Response:
    content = request.get_json()
    user_type = UserType.create_from_dto(content)
    user_type_controller.create_user_type(user_type)
    return make_response(jsonify(user_type.put_into_dto()), HTTPStatus.CREATED)


@user_types_bp.route('/<int:user_type_id>', methods=['GET'])
def get_user_type_by_id(user_type_id: int) -> Response:
    user_type = user_type_controller.find_by_id(user_type_id)
    if user_type:
        return make_response(jsonify(user_type.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "User type not found"}), HTTPStatus.NOT_FOUND)


@user_types_bp.route('/<int:user_type_id>', methods=['PUT'])
def update_user_type(user_type_id: int) -> Response:
    content = request.get_json()
    user_type = UserType.create_from_dto(content)
    user_type_controller.update_user_type(user_type_id, user_type)
    return make_response("User type updated", HTTPStatus.OK)


@user_types_bp.route('/<int:user_type_id>', methods=['DELETE'])
def delete_user_type(user_type_id: int) -> Response:
    user_type_controller.delete_user_type(user_type_id)
    return make_response("User type deleted", HTTPStatus.NO_CONTENT)


@user_types_bp.route('/type/<string:type_name>', methods=['GET'])
def get_user_types_by_name(type_name: str) -> Response:
    user_types = user_type_controller.get_user_types_by_name(type_name)
    return make_response(jsonify([user_type.put_into_dto() for user_type in user_types]), HTTPStatus.OK)
