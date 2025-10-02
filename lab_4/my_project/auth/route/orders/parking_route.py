from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import parking_controller
from my_project.auth.domain.orders.parking import Parking

parking_bp = Blueprint('parking', __name__, url_prefix='/parkings')

@parking_bp.get('/<int:park_id>')
def get_park(park_id: int) -> Response:
    """
    Get Park by ID
    ---
    parameters:
      - name: park_id
        in: path
        type: integer
        required: true
        example: 1
    responses:
      200:
        description: Park found
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            name:
              type: string
              example: "Park"
            location:
              type: string
              example: "Lviv"
            maxVisit:
              type: number
              example: 100
            attractionNumber:
              type: number
              example: 1000
            age:
              type: number
              example: 5
      404:
        description: Park not found
    """
    parking = parking_controller.find_by_id(park_id)
    if park:
        return make_response(jsonify(parking.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Parking not found"}), HTTPStatus.NOT_FOUND)

# @parking_bp.route('', methods=['GET'])
# def get_all_parkings() -> Response:
#     parkings = parking_controller.find_all()
#     parking_dto = [parking.put_into_dto() for parking in parkings]
#     return make_response(jsonify(parking_dto), HTTPStatus.OK)
#
#
# @parking_bp.route('', methods=['POST'])
# def create_parking() -> Response:
#     content = request.get_json()
#     parking = Parking.create_from_dto(content)
#     parking_controller.create_parking(parking)
#     return make_response(jsonify(parking.put_into_dto()), HTTPStatus.CREATED)
#
#
# @parking_bp.route('/<int:parking_id>', methods=['GET'])
# def get_parking_by_id(parking_id: int) -> Response:
#     parking = parking_controller.find_by_id(parking_id)
#     if parking:
#         return make_response(jsonify(parking.put_into_dto()), HTTPStatus.OK)
#     return make_response(jsonify({"error": "Parking not found"}), HTTPStatus.NOT_FOUND)
#
#
# @parking_bp.route('/<int:parking_id>', methods=['PUT'])
# def update_parking(parking_id: int) -> Response:
#     content = request.get_json()
#     parking = Parking.create_from_dto(content)
#     parking_controller.update_parking(parking_id, parking)
#     return make_response("Parking updated", HTTPStatus.OK)
#
#
# @parking_bp.route('/<int:parking_id>', methods=['DELETE'])
# def delete_parking(parking_id: int) -> Response:
#     parking_controller.delete_parking(parking_id)
#     return make_response("Parking deleted", HTTPStatus.NO_CONTENT)
