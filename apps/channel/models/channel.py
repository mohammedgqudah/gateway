from sqlalchemy import Boolean, Column, Integer, String, UniqueConstraint

from apps.business.models import BusinessRef
from core.db import Base


class Channel(Base, BusinessRef):
    __tablename__ = "channel"

    name = Column("name", String)
    type = Column("type", Integer)

    phone = Column("phone", String)
    address = Column("address", String)
    # position = Column('position', String)  # lang/lat/google

    # image = Column('image', String)  # 265 etc...
    is_active = Column("is_active", Boolean, default=True, server_default="true")
    is_default = Column("is_default", Boolean, default=False, server_default="false")

    __table_args__ = (
        UniqueConstraint("business_id", "name"),
        UniqueConstraint("business_id", "is_default"),
    )

    class Types:
        CHANNEL = 0
