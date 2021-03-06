from dataclasses import dataclass

from fastapi_baseplate.query.postgres import BasePaginationQuery, BaseQuery
from pydantic import EmailStr

from core.serializers import BaseModel


@dataclass
class EmployeeQuery(BaseQuery, BasePaginationQuery):
    pass


class EmployeeBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str = None

    type: str = None
    is_active: bool

    class Config:
        orm_mode = True


class EmployeeOut(EmployeeBase):
    id: str
