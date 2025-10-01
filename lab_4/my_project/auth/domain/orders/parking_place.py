from __future__ import annotations
from typing import Dict, Any
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from my_project import db
from my_project.auth.domain.i_dto import IDto


class ParkingPlace(db.Model, IDto):
    __tablename__ = "parking_place"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    parking_id = db.Column(db.Integer, ForeignKey('parking.id'), nullable=False)
    status_id = db.Column(db.Integer, ForeignKey('status_type.id'), nullable=False)
    row = db.Column(db.Integer, nullable=False)
    row_place = db.Column(db.Integer, nullable=False)

    parking = relationship('Parking', back_populates='parking_places')
    status = relationship('StatusType', back_populates='parking_places')
    reservations = relationship('Reservations', back_populates='parking_place')
    histories = relationship('ParkingPlaceHistory', back_populates='parking_place')

    def __repr__(self) -> str:
        return f"ParkingPlace({self.id}, {self.parking_id}, {self.status_id}, {self.row}, {self.row_place})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "parking_id": self.parking_id,
            "status_id": self.status_id,
            "row": self.row,
            "row_place": self.row_place
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ParkingPlace:
        obj = ParkingPlace(**dto_dict)
        return obj
