from __future__ import annotations
from typing import Dict, Any
from sqlalchemy.orm import relationship
from my_project import db
from my_project.auth.domain.i_dto import IDto


class StatusType(db.Model, IDto):
    __tablename__ = "status_type"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(30), nullable=False)

    parking_places = relationship('ParkingPlace', back_populates='status')

    def __repr__(self) -> str:
        return f"StatusType({self.id}, {self.type})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "type": self.type
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> StatusType:
        obj = StatusType(**dto_dict)
        return obj
