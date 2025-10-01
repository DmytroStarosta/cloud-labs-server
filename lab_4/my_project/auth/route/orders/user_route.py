from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import user_controller
from my_project.auth.domain.orders.user import User

users_bp = Blueprint('users', __name__, url_prefix='/users')


@users_bp.route('', methods=['GET'])
def get_all_users() -> Response:
    users = user_controller.find_all()
    user_dto = [user.put_into_dto() for user in users]
    return make_response(jsonify(user_dto), HTTPStatus.OK)


@users_bp.route('', methods=['POST'])
def create_user() -> Response:
    content = request.get_json()
    user = User.create_from_dto(content)
    user_controller.create_user(user)
    return make_response(jsonify(user.put_into_dto()), HTTPStatus.CREATED)


@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id: int) -> Response:
    user = user_controller.find_by_id(user_id)
    if user:
        return make_response(jsonify(user.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "User not found"}), HTTPStatus.NOT_FOUND)


@users_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id: int) -> Response:
    content = request.get_json()
    user = User.create_from_dto(content)
    user_controller.update_user(user_id, user)
    return make_response("User updated", HTTPStatus.OK)


@users_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int) -> Response:
    user_controller.delete_user(user_id)
    return make_response("User deleted", HTTPStatus.NO_CONTENT)


@users_bp.route('/surname/<surname>', methods=['GET'])
def get_user_by_surname(surname: str) -> Response:
    users = user_controller.find_by_surname(surname)
    if users:
        user_dto = [user.put_into_dto() for user in users]
        return make_response(jsonify(user_dto), HTTPStatus.OK)
    return make_response(jsonify({"error": "User not found"}), HTTPStatus.NOT_FOUND)


@users_bp.route('/email/<string:email>', methods=['GET'])
def get_users_by_email(email: str) -> Response:
    users = user_controller.get_users_by_email(email)
    return make_response(jsonify([user.put_into_dto() for user in users]), HTTPStatus.OK)
