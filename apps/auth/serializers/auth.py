from pydantic import Field, EmailStr

from core.serializers import BaseModel
from core.serializers.fields import SubDomainField


class LoginData(BaseModel):
    sub_domain: str = SubDomainField(...)
    email: EmailStr
    password: str = Field(..., min_length=1)
