from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class UserType(db.Model, IDto):
    __tablename__ = "user_type"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(30), nullable=False)

    users = relationship('User', back_populates='user_type')

    def __repr__(self) -> str:
        return f"UserType({self.id}, {self.type})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "type": self.type
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> UserType:
        obj = UserType(**dto_dict)
        return obj
