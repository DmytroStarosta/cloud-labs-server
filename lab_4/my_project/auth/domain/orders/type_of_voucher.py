from __future__ import annotations
from typing import Dict, Any
from sqlalchemy.orm import relationship
from my_project import db
from my_project.auth.domain.i_dto import IDto


class TypeOfVoucher(db.Model, IDto):
    __tablename__ = "type_of_voucher"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(50), nullable=False)

    vouchers = relationship('Voucher', back_populates='type_of_voucher')

    def __repr__(self) -> str:
        return f"TypeOfVoucher({self.id}, {self.type})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "type": self.type
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> TypeOfVoucher:
        obj = TypeOfVoucher(**dto_dict)
        return obj
