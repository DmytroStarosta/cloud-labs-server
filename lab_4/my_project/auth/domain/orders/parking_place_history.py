from __future__ import annotations
from typing import Dict, Any
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from my_project import db
from my_project.auth.domain.i_dto import IDto


class ParkingPlaceHistory(db.Model, IDto):
    __tablename__ = "parking_place_history"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    parking_place_id = db.Column(db.Integer, ForeignKey('parking_place.id'), nullable=False)
    car_id = db.Column(db.Integer, ForeignKey('cars.id'), nullable=False)
    occupied_from = db.Column(db.DateTime, nullable=False)
    occupied_to = db.Column(db.DateTime, nullable=False)

    parking_place = relationship('ParkingPlace', back_populates='histories')
    car = relationship('Cars', back_populates='history_records')

    def __repr__(self) -> str:
        return f"ParkingPlaceHistory({self.id}, {self.parking_place_id}, {self.car_id}, {self.occupied_from}, {self.occupied_to})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "parking_place_id": self.parking_place_id,
            "car_id": self.car_id,
            "occupied_from": self.occupied_from,
            "occupied_to": self.occupied_to
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ParkingPlaceHistory:
        obj = ParkingPlaceHistory(**dto_dict)
        return obj
