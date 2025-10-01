from __future__ import annotations
from typing import Dict, Any
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Reservations(db.Model, IDto):
    __tablename__ = "reservations"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    car_id = db.Column(db.Integer, ForeignKey('cars.id'), nullable=False)
    parking_place_id = db.Column(db.Integer, ForeignKey('parking_place.id'), nullable=False)
    reservation_start = db.Column(db.DateTime, nullable=False)
    reservation_stop = db.Column(db.DateTime, nullable=False)

    user = relationship('User', back_populates='reservations')
    car = relationship('Cars', back_populates='reservation', uselist=False)
    parking_place = relationship('ParkingPlace', back_populates='reservations')

    def __repr__(self) -> str:
        return (f"Reservations({self.id}, "
                f"{self.user_id}, "
                f"{self.car_id}, "
                f"{self.parking_place_id}, "
                f"{self.reservation_start}, "
                f"{self.reservation_stop})"
                )

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "car_id": self.car_id,
            "parking_place_id": self.parking_place_id,
            "reservation_start": self.reservation_start,
            "reservation_stop": self.reservation_stop
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Reservations:
        obj = Reservations(**dto_dict)
        return obj
