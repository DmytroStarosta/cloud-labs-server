from flask import Flask


def register_routes(app: Flask) -> None:
    from .orders.user_route import users_bp
    from .orders.user_type_route import user_types_bp
    from .orders.cars_route import cars_bp
    from .orders.user_car_id_route import user_car_id_bp
    from .orders.parking_route import parking_bp
    from .orders.parking_place_route import parking_place_bp
    from .orders.parking_place_history_route import parking_place_history_bp
    from .orders.reservations_route import reservations_bp
    from .orders.status_type_route import status_type_bp
    from .orders.adress_route import address_bp
    from .orders.owner_route import owner_bp
    from .orders.parking_network_route import parking_network_bp
    from .orders.type_of_voucher_route import type_of_voucher_bp
    from .orders.voucher_route import voucher_bp

    app.register_blueprint(users_bp)
    app.register_blueprint(user_types_bp)
    app.register_blueprint(cars_bp)
    app.register_blueprint(user_car_id_bp)
    app.register_blueprint(parking_bp)
    app.register_blueprint(parking_place_bp)
    app.register_blueprint(parking_place_history_bp)
    app.register_blueprint(reservations_bp)
    app.register_blueprint(status_type_bp)
    app.register_blueprint(address_bp)
    app.register_blueprint(owner_bp)
    app.register_blueprint(parking_network_bp)
    app.register_blueprint(type_of_voucher_bp)
    app.register_blueprint(voucher_bp)
