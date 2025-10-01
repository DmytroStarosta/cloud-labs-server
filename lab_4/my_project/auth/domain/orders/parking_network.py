from __future__ import annotations
from typing import Dict, Any
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from my_project import db
from my_project.auth.domain.i_dto import IDto


class ParkingNetwork(db.Model, IDto):
    __tablename__ = "parking_network"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    owner_id = db.Column(db.Integer, ForeignKey('owner.id'), nullable=False)
    parking_amount = db.Column(db.Integer, nullable=False)

    owner = relationship('Owner', back_populates='parking_networks')
    parkings = relationship('Parking', back_populates='parking_network')

    def __repr__(self) -> str:
        return f"ParkingNetwork({self.id}, {self.owner_id}, {self.parking_amount})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "owner_id": self.owner.put_into_dto() if self.owner else None,
            "parking_amount": self.parking_amount
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ParkingNetwork:
        obj = ParkingNetwork(**dto_dict)
        return obj
