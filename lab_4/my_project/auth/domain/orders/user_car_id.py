from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class UserCarId(db.Model, IDto):
    __tablename__ = "user_car_id"

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), primary_key=True)

    user = relationship('User', back_populates='user_car_associations')
    car = relationship('Cars', back_populates='user_car_associations')

    def __repr__(self) -> str:
        return f"UserCarId({self.user_id}, {self.car_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "user_id": self.user.put_into_dto() if self.user else None,
            "car_id": self.car.put_into_dto() if self.car else None
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> UserCarId:
        obj = UserCarId(**dto_dict)
        return obj
