from flask import Blueprint, Response, make_response, jsonify, request
from http import HTTPStatus

health_bp = Blueprint('health', __name__, url_prefix="/health")

@health_bp.get("/")
def health_check() -> Response:
   return make_response(jsonify({"message": "OK"}), HTTPStatus.OK)


