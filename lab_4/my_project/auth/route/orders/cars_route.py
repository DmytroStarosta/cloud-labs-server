from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import cars_controller
from my_project.auth.domain.orders.cars import Cars

cars_bp = Blueprint('cars', __name__, url_prefix='/cars')


@cars_bp.route('', methods=['GET'])
def get_all_cars() -> Response:
    cars = cars_controller.find_all()
    car_dto = [car.put_into_dto() for car in cars]
    return make_response(jsonify(car_dto), HTTPStatus.OK)


@cars_bp.route('', methods=['POST'])
def create_car() -> Response:
    content = request.get_json()
    car = Cars.create_from_dto(content)
    cars_controller.create_car(car)
    return make_response(jsonify(car.put_into_dto()), HTTPStatus.CREATED)


@cars_bp.route('/<int:car_id>', methods=['GET'])
def get_car_by_id(car_id: int) -> Response:
    car = cars_controller.find_by_id(car_id)
    if car:
        return make_response(jsonify(car.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Car not found"}), HTTPStatus.NOT_FOUND)


@cars_bp.route('/<int:car_id>', methods=['PUT'])
def update_car(car_id: int) -> Response:
    content = request.get_json()
    car = Cars.create_from_dto(content)
    cars_controller.update_car(car_id, car)
    return make_response("Car updated", HTTPStatus.OK)


@cars_bp.route('/<int:car_id>', methods=['DELETE'])
def delete_car(car_id: int) -> Response:
    cars_controller.delete_car(car_id)
    return make_response("Car deleted", HTTPStatus.NO_CONTENT)
