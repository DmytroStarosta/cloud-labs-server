from __future__ import annotations
from typing import Dict, Any
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Parking(db.Model, IDto):
    __tablename__ = "parking"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location = db.Column(db.String(100), nullable=False)
    parking_network_id = db.Column(db.Integer, ForeignKey('parking_network.id'), nullable=False)
    address_id = db.Column(db.Integer, ForeignKey('address.id'), nullable=False)

    parking_places = relationship('ParkingPlace', back_populates='parking')
    vouchers = relationship('Voucher', back_populates='parking')
    parking_network = relationship('ParkingNetwork', back_populates='parkings')
    address = relationship('Address', back_populates='parking', uselist=False)

    def __repr__(self) -> str:
        return f"Parking({self.id}, {self.location}, {self.parking_network_id}, {self.address_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "location": self.location,
            "parking_network_id": self.parking_network_id,
            "address_id": self.address_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Parking:
        obj = Parking(**dto_dict)
        return obj
