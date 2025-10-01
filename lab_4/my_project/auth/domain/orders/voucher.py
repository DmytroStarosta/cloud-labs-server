from __future__ import annotations
from typing import Dict, Any
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Voucher(db.Model, IDto):
    __tablename__ = "voucher"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    voucher_type_id = db.Column(db.Integer, ForeignKey('type_of_voucher.id'), nullable=False)
    parking_id = db.Column(db.Integer, ForeignKey('parking.id'), nullable=False)
    issued_time = db.Column(db.DateTime, nullable=False)
    car_id = db.Column(db.Integer, ForeignKey('cars.id'), nullable=False)

    user = relationship('User', back_populates='vouchers')
    car = relationship('Cars', back_populates='vouchers')
    type_of_voucher = relationship('TypeOfVoucher', back_populates='vouchers')
    parking = relationship('Parking', back_populates='vouchers')

    def __repr__(self) -> str:
        return f"Voucher({self.id}, {self.user_id}, {self.voucher_type_id}, {self.parking_id}, {self.issued_time}, {self.car_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "voucher_type_id": self.voucher_type_id,
            "parking_id": self.parking_id,
            "issued_time": self.issued_time,
            "car_id": self.car_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Voucher:
        obj = Voucher(**dto_dict)
        return obj
