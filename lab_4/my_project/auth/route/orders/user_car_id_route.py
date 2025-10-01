from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import user_car_id_controller
from my_project.auth.domain.orders.user_car_id import UserCarId

user_car_id_bp = Blueprint('user_car_id', __name__, url_prefix='/user_car_id')


@user_car_id_bp.route('', methods=['GET'])
def get_all_user_car_ids() -> Response:
    user_car_ids = user_car_id_controller.find_all()
    user_car_id_dto = [user_car_id.put_into_dto() for user_car_id in user_car_ids]
    return make_response(jsonify(user_car_id_dto), HTTPStatus.OK)


@user_car_id_bp.route('', methods=['POST'])
def create_user_car_id() -> Response:
    content = request.get_json()
    user_car_id = UserCarId.create_from_dto(content)
    user_car_id_controller.create_user_car_id(user_car_id)
    return make_response(jsonify(user_car_id.put_into_dto()), HTTPStatus.CREATED)


@user_car_id_bp.route('/<int:user_id>/<int:car_id>', methods=['GET'])
def get_user_car_id_by_user_and_car_id(user_id: int, car_id: int) -> Response:
    user_car_id = user_car_id_controller.find_by_user_and_car_id(user_id, car_id)
    if user_car_id:
        return make_response(jsonify(user_car_id.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "UserCarId not found"}), HTTPStatus.NOT_FOUND)


@user_car_id_bp.route('/<int:user_id>/<int:car_id>', methods=['PUT'])
def update_user_car_id(user_id: int, car_id: int) -> Response:
    content = request.get_json()
    user_car_id = UserCarId.create_from_dto(content)
    user_car_id_controller.update_user_car_id(user_id, car_id, user_car_id)
    return make_response("UserCarId updated", HTTPStatus.OK)


@user_car_id_bp.route('/<int:user_id>/<int:car_id>', methods=['DELETE'])
def delete_user_car_id(user_id: int, car_id: int) -> Response:
    user_car_id_controller.delete_user_car_id(user_id, car_id)
    return make_response("UserCarId deleted", HTTPStatus.NO_CONTENT)
