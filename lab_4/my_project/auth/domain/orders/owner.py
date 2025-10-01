from __future__ import annotations
from typing import Dict, Any
from sqlalchemy.orm import relationship
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Owner(db.Model, IDto):
    __tablename__ = "owner"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    parking_networks = relationship('ParkingNetwork', back_populates='owner')

    def __repr__(self) -> str:
        return f"Owner({self.id}, {self.name}, {self.surname}, {self.age})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "age": self.age
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Owner:
        obj = Owner(**dto_dict)
        return obj
