from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import owner_controller
from my_project.auth.domain.orders.owner import Owner
from flask_jwt_extended import jwt_required


owner_bp = Blueprint('owner', __name__, url_prefix='/owners')


@owner_bp.route('', methods=['GET'])
@jwt_required()
def get_all_owners() -> Response:
    """
    Get all Owners
    ---
    tags:
      - Owner
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: JWT token
        example: "Bearer <your_jwt_token>"
    responses:
      200:
        description: List of all owners
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              name:
                type: string
                example: "John"
              surname:
                type: string
                example: "Doe"
              age:
                type: integer
                example: 35
    """
    owners = owner_controller.find_all()
    owner_dto = [owner.put_into_dto() for owner in owners]
    return make_response(jsonify(owner_dto), HTTPStatus.OK)



@owner_bp.route('', methods=['POST'])
def create_owner() -> Response:
    """
    Create a new Owner
    ---
    tags:
      - Owner
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - name
            - surname
            - age
            - password
          properties:
            name:
              type: string
              example: "John"
            surname:
              type: string
              example: "Doe"
            age:
              type: integer
              example: 35
            password:
              type: string
              example: "secure123"
    responses:
      201:
        description: Owner created successfully
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            name:
              type: string
              example: "John"
            surname:
              type: string
              example: "Doe"
            age:
              type: integer
              example: 35
    """
    content = request.get_json()
    owner = Owner.create_from_dto(content)
    owner_controller.create_owner(owner)
    return make_response(jsonify(owner.put_into_dto()), HTTPStatus.CREATED)


@owner_bp.route('/<int:owner_id>', methods=['GET'])
@jwt_required()
def get_owner_by_id(owner_id: int) -> Response:
    """
    Get Owner by ID
    ---
    tags:
      - Owner
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: JWT token
        example: "Bearer <your_jwt_token>"
      - name: owner_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: Owner found
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            name:
              type: string
              example: "John"
            surname:
              type: string
              example: "Doe"
            age:
              type: integer
              example: 35
      404:
        description: Owner not found
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Owner not found"
    """
    owner = owner_controller.find_by_id(owner_id)
    if owner:
        return make_response(jsonify(owner.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Owner not found"}), HTTPStatus.NOT_FOUND)


@owner_bp.route('/<int:owner_id>', methods=['PUT'])
@jwt_required()
def update_owner(owner_id: int) -> Response:
    """
    Update Owner by ID
    ---
    tags:
      - Owner
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: JWT token
        example: "Bearer <your_jwt_token>"
      - name: owner_id
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
            - name
            - surname
            - age
            - password
          properties:
            name:
              type: string
              example: "John"
            surname:
              type: string
              example: "Doe"
            age:
              type: integer
              example: 36
            password:
              type: string
              example: "newpass456"
    responses:
      200:
        description: Owner updated successfully
        schema:
          type: string
          example: "Owner updated"
    """
    content = request.get_json()
    owner = Owner.create_from_dto(content)
    owner_controller.update_owner(owner_id, owner)
    return make_response("Owner updated", HTTPStatus.OK)


@owner_bp.route('/<int:owner_id>', methods=['DELETE'])
@jwt_required()
def delete_owner(owner_id: int) -> Response:
    """
    Delete Owner by ID
    ---
    tags:
      - Owner
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
        description: JWT token
        example: "Bearer <your_jwt_token>"
      - name: owner_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      204:
        description: Owner deleted successfully
        schema:
          type: string
          example: "Owner deleted"
    """
    owner_controller.delete_owner(owner_id)
    return make_response("Owner deleted", HTTPStatus.NO_CONTENT)
