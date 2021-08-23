from enum import Enum

from fastapi_baseplate.serializers import UUID4
from core.serializers import BaseModel

from ..models import Channel


class Types(int, Enum):
    CHANNEL = Channel.Types.CHANNEL


class ChannelBase(BaseModel):
    name: str
    type: Types

    phone: str
    address: str
    is_active: bool = True
    is_default: bool = False

    class Config:
        orm_mode = True
        use_enum_values = True


class ChannelOut(ChannelBase):
    id: UUID4
