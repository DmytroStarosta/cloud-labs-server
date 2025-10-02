import os
from flask import Flask
from flask_jwt_extended import JWTManager
from my_project.auth.route.orders.parking_route import parking_bp
from my_project.config import Config
from my_project import db


def create_app(config_object=None):
    app = Flask(__name__)

    if config_object is None:
        app.config.from_object(Config)
    else:
        app.config.from_object(config_object)

    db.init_app(app)
    jwt = JWTManager(app)

    app.register_blueprint(parking_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
