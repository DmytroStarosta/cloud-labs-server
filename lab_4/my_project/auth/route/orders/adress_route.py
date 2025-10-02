from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import address_controller
from my_project.auth.domain.orders.address import Address
from flask_jwt_extended import jwt_required

address_bp = Blueprint('address', __name__, url_prefix='/address')


@address_bp.route('', methods=['GET'])
@jwt_required()
def get_all_addresses() -> Response:
    """
    Get all Addresses
    ---
    tags:
      - Address
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: JWT token
        example: "Bearer <your_jwt_token>"
    responses:
      200:
        description: List of all addresses
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              street:
                type: string
                example: "Shevchenka"
              number:
                type: integer
                example: 12
              index:
                type: integer
                example: 79000
    """
    addresses = address_controller.find_all()
    address_dto = [address.put_into_dto() for address in addresses]
    return make_response(jsonify(address_dto), HTTPStatus.OK)


@address_bp.route('', methods=['POST'])
def create_address() -> Response:
    """
    Create a new Address
    ---
    tags:
      - Address
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - street
            - number
            - index
          properties:
            street:
              type: string
              example: "Shevchenka"
            number:
              type: integer
              example: 12
            index:
              type: integer
              example: 79000
    responses:
      201:
        description: Address created successfully
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            street:
              type: string
              example: "Shevchenka"
            number:
              type: integer
              example: 12
            index:
              type: integer
              example: 79000
    """
    content = request.get_json()
    address = Address.create_from_dto(content)
    address_controller.create_address(address)
    return make_response(jsonify(address.put_into_dto()), HTTPStatus.CREATED)


@address_bp.route('/<int:address_id>', methods=['GET'])
@jwt_required()
def get_address_by_id(address_id: int) -> Response:
    """
    Get Address by ID
    ---
    tags:
      - Address
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        example: "Bearer <your_jwt_token>"
      - name: address_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: Address found
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            street:
              type: string
              example: "Shevchenka"
            number:
              type: integer
              example: 12
            index:
              type: integer
              example: 79000
      404:
        description: Address not found
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Address not found"
    """
    address = address_controller.find_by_id(address_id)
    if address:
        return make_response(jsonify(address.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Address not found"}), HTTPStatus.NOT_FOUND)


@address_bp.route('/<int:address_id>', methods=['PUT'])
@jwt_required()
def update_address(address_id: int) -> Response:
    """
    Update Address by ID
    ---
    tags:
      - Address
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        example: "Bearer <your_jwt_token>"
      - name: address_id
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
            - street
            - number
            - index
          properties:
            street:
              type: string
              example: "Bandery"
            number:
              type: integer
              example: 15
            index:
              type: integer
              example: 79001
    responses:
      200:
        description: Address updated successfully
        schema:
          type: string
          example: "Address updated"
    """
    content = request.get_json()
    address = Address.create_from_dto(content)
    address_controller.update_address(address_id, address)
    return make_response("Address updated", HTTPStatus.OK)


@address_bp.route('/<int:address_id>', methods=['DELETE'])
@jwt_required()
def delete_address(address_id: int) -> Response:
    """
    Delete Address by ID
    ---
    tags:
      - Address
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        example: "Bearer <your_jwt_token>"
      - name: address_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      204:
        description: Address deleted successfully
        schema:
          type: string
          example: "Address deleted"
    """
    address_controller.delete_address(address_id)
    return make_response("Address deleted", HTTPStatus.NO_CONTENT)
