from dataclasses import dataclass

from pydantic import EmailStr
from fastapi_basis.query.postgres import BaseQuery, BasePaginationQuery

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
