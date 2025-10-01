from __future__ import annotations
from typing import Dict, Any
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Cars(db.Model, IDto):
    __tablename__ = "cars"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    car_owner = db.Column(db.String(30), nullable=False)
    car_brand = db.Column(db.String(30), nullable=False)
    car_model = db.Column(db.String(30), nullable=False)
    car_number = db.Column(db.String(30), nullable=False)

    user_car_associations = relationship('UserCarId', back_populates='car')
    reservation = relationship('Reservations', back_populates='car', uselist=False)
    history_records = relationship('ParkingPlaceHistory', back_populates='car')
    vouchers = relationship('Voucher', back_populates='car')

    def __repr__(self) -> str:
        return f"Cars({self.id}, {self.car_owner}, {self.car_brand}, {self.car_model}, {self.car_number})"

    def put_into_dto(self, include_users=True) -> Dict[str, Any]:
        return {
            "id": self.id,
            "car_owner": self.car_owner,
            "car_brand": self.car_brand,
            "car_model": self.car_model,
            "car_number": self.car_number,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Cars:
        obj = Cars(**dto_dict)
        return obj
