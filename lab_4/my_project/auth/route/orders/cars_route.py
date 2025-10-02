from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import cars_controller
from my_project.auth.domain.orders.cars import Cars
from flask_jwt_extended import jwt_required

cars_bp = Blueprint('cars', __name__, url_prefix='/cars')


@cars_bp.route('', methods=['GET'])
@jwt_required()
def get_all_cars() -> Response:
    """
    Get all Cars
    ---
    tags:
      - Cars
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: JWT token
        example: "Bearer <your_jwt_token>"
    responses:
      200:
        description: List of all cars
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              car_owner:
                type: string
                example: "Ivan Petrenko"
              car_brand:
                type: string
                example: "Toyota"
              car_model:
                type: string
                example: "Corolla"
              car_number:
                type: string
                example: "AA1234BC"
    """
    cars = cars_controller.find_all()
    car_dto = [car.put_into_dto() for car in cars]
    return make_response(jsonify(car_dto), HTTPStatus.OK)


@cars_bp.route('', methods=['POST'])
def create_car() -> Response:
    """
    Create a new Car
    ---
    tags:
      - Cars
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - car_owner
            - car_brand
            - car_model
            - car_number
          properties:
            car_owner:
              type: string
              example: "Ivan Petrenko"
            car_brand:
              type: string
              example: "Toyota"
            car_model:
              type: string
              example: "Corolla"
            car_number:
              type: string
              example: "AA1234BC"
    responses:
      201:
        description: Car created successfully
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            car_owner:
              type: string
              example: "Ivan Petrenko"
            car_brand:
              type: string
              example: "Toyota"
            car_model:
              type: string
              example: "Corolla"
            car_number:
              type: string
              example: "AA1234BC"
    """
    content = request.get_json()
    car = Cars.create_from_dto(content)
    cars_controller.create_car(car)
    return make_response(jsonify(car.put_into_dto()), HTTPStatus.CREATED)


@cars_bp.route('/<int:car_id>', methods=['GET'])
@jwt_required()
def get_car_by_id(car_id: int) -> Response:
    """
    Get Car by ID
    ---
    tags:
      - Cars
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        example: "Bearer <your_jwt_token>"
      - name: car_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: Car found
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            car_owner:
              type: string
              example: "Ivan Petrenko"
            car_brand:
              type: string
              example: "Toyota"
            car_model:
              type: string
              example: "Corolla"
            car_number:
              type: string
              example: "AA1234BC"
      404:
        description: Car not found
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Car not found"
    """
    car = cars_controller.find_by_id(car_id)
    if car:
        return make_response(jsonify(car.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Car not found"}), HTTPStatus.NOT_FOUND)


@cars_bp.route('/<int:car_id>', methods=['PUT'])
@jwt_required()
def update_car(car_id: int) -> Response:
    """
    Update Car by ID
    ---
    tags:
      - Cars
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        example: "Bearer <your_jwt_token>"
      - name: car_id
        in: path
        required: true
        type: integer
        example: 1
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - car_owner
            - car_brand
            - car_model
            - car_number
          properties:
            car_owner:
              type: string
              example: "Ivan Petrenko"
            car_brand:
              type: string
              example: "Honda"
            car_model:
              type: string
              example: "Civic"
            car_number:
              type: string
              example: "BB5678CD"
    responses:
      200:
        description: Car updated successfully
        schema:
          type: string
          example: "Car updated"
    """
    content = request.get_json()
    car = Cars.create_from_dto(content)
    cars_controller.update_car(car_id, car)
    return make_response("Car updated", HTTPStatus.OK)


@cars_bp.route('/<int:car_id>', methods=['DELETE'])
@jwt_required()
def delete_car(car_id: int) -> Response:
    """
    Delete Car by ID
    ---
    tags:
      - Cars
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        example: "Bearer <your_jwt_token>"
      - name: car_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      204:
        description: Car deleted successfully
        schema:
          type: string
          example: "Car deleted"
    """
    cars_controller.delete_car(car_id)
    return make_response("Car deleted", HTTPStatus.NO_CONTENT)
