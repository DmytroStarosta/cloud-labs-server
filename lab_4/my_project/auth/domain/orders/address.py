from __future__ import annotations
from typing import Dict, Any
from sqlalchemy.orm import relationship
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Address(db.Model, IDto):
    __tablename__ = "address"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    street = db.Column(db.String(100), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    index = db.Column(db.Integer, nullable=False)

    parking = relationship('Parking', back_populates='address', uselist=False)

    def __repr__(self) -> str:
        return f"Address({self.id}, {self.street}, {self.number}, {self.index})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "street": self.street,
            "number": self.number,
            "index": self.index
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Address:
        obj = Address(**dto_dict)
        return obj
