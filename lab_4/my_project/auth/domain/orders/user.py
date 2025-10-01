from __future__ import annotations
from typing import Dict, Any
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from my_project import db
from my_project.auth.domain.i_dto import IDto


class User(db.Model, IDto):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_type_id = Column(Integer, ForeignKey('user_type.id'), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)

    user_type = relationship('UserType', back_populates='users')
    user_car_associations = relationship('UserCarId', back_populates='user')
    reservations = relationship('Reservations', back_populates='user')
    vouchers = relationship('Voucher', back_populates='user')

    def __repr__(self) -> str:
        return f"User({self.id}, {self.user_type_id}, {self.name}, '{self.surname}', {self.email})"

    def put_into_dto(self, include_cars=True) -> Dict[str, Any]:
        return {
            "id": self.id,
            "user_type": self.user_type.put_into_dto() if self.user_type else None,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> User:
        obj = User(**dto_dict)
        return obj
