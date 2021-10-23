from enum import Enum

from core.serializers import BaseModel
from core.serializers.fields import SubDomainField

from ..models import Business


class Types(int, Enum):
    OTHER = Business.Types.OTHER


class Plans(int, Enum):
    TRIAL = Business.Plans.TRIAL
    FREE = Business.Plans.FREE
    STANDARD = Business.Plans.STANDARD
    PRO = Business.Plans.PRO


class BusinessBase(BaseModel):
    sub_domain: str = SubDomainField(...)
    name: str
    description: str = None

    type: Types
    plan: Plans

    private: bool

    class Config:
        orm_mode = True
        use_enum_values = True
