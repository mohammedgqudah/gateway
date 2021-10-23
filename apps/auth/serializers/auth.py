from pydantic import EmailStr, Field

from core.serializers import BaseModel
from core.serializers.fields import SubDomainField


class LoginCredentials(BaseModel):
    sub_domain: str = SubDomainField(...)
    email: EmailStr
    password: str = Field(..., min_length=1)
