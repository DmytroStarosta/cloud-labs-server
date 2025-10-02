from flask import Blueprint, Response, make_response, jsonify
from http import HTTPStatus
from flask_jwt_extended import create_access_token
from my_project.auth.domain.orders.owner import Owner

auth_bp = Blueprint('auth', __name__, url_prefix="/auth")

@auth_bp.post("/login")
def login() -> Response:
    """
        Login
        ---
        parameters:
        - name: body
          in: body
          required: true
          schema:
            type: object
            properties:
              name:
                type: string
                example: "owner"
              password:
                type: string
                example: "password123"
        responses:
          200:
            description: Login successful
            schema:
              type: object
              properties:
                access_token:
                  type: string
                  example: "<access_token>"
    """

    data = request.get_json()
    owner = Owner.query.filter_by(name=data["name"]).first()
    if owner is not None and owner.password == data['password']:
        access_token = create_access_token(identity=str(owner.id))
        return make_response(jsonify({'access_token': access_token}), HTTPStatus.OK)

    return make_response(jsonify({"message": f"Not found Park {data['name']} or bad password"}), HTTPStatus.NOT_FOUND)