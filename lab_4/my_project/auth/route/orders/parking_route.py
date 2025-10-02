from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from flask_jwt_extended import jwt_required
from my_project.auth.controller import parking_controller
from my_project.auth.domain.orders.parking import Parking

parking_bp = Blueprint('parking', __name__, url_prefix='/parkings')

@parking_bp.get('/<int:parking_id>')
@jwt_required()
def get_parking(parking_id: int) -> Response:
    parking = parking_controller.find_by_id(parking_id)
    if parking:
        return make_response(jsonify(parking.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Parking not found"}), HTTPStatus.NOT_FOUND)

@parking_bp.get('')
@jwt_required()
def get_all_parkings() -> Response:
    parkings = parking_controller.find_all()
    parking_dto = [parking.put_into_dto() for parking in parkings]
    return make_response(jsonify(parking_dto), HTTPStatus.OK)

@parking_bp.post('')
@jwt_required()
def create_parking() -> Response:
    content = request.get_json()
    parking = Parking.create_from_dto(content)
    parking_controller.create_parking(parking)
    return make_response(jsonify(parking.put_into_dto()), HTTPStatus.CREATED)

@parking_bp.put('/<int:parking_id>')
@jwt_required()
def update_parking(parking_id: int) -> Response:
    content = request.get_json()
    parking = Parking.create_from_dto(content)
    parking_controller.update_parking(parking_id, parking)
    return make_response("Parking updated", HTTPStatus.OK)

@parking_bp.delete('/<int:parking_id>')
@jwt_required()
def delete_parking(parking_id: int) -> Response:
    parking_controller.delete_parking(parking_id)
    return make_response("Parking deleted", HTTPStatus.NO_CONTENT)
