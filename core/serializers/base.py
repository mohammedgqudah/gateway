from datetime import datetime
from uuid import UUID

from fastapi.encoders import jsonable_encoder
from pydantic import BaseConfig as PBaseConfig
from pydantic import BaseModel as PBaseModel


class BaseConfig(PBaseConfig):
    json_encoders = {
        datetime: lambda dt: dt.isoformat(),
        UUID: str,
    }


class BaseModel(PBaseModel):
    def json(self, *args, **kwargs):
        return jsonable_encoder(self)

    class Config(BaseConfig):
        pass
