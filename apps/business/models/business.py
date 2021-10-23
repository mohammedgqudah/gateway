from sqlalchemy import Column, String, Boolean, Integer

from core.db import Base


class Business(Base):
    __tablename__ = "business"

    sub_domain = Column("sub_domain", String, unique=True)
    name = Column("name", String)
    description = Column("description", String, nullable=True)
    type = Column("type", Integer)
    plan = Column("plan", Integer)

    # whether this business should be available to users
    private = Column("private", Boolean, default=True, server_default="true")

    class Types:
        OTHER = 0

    class Plans:
        TRIAL = 0
        FREE = 1
        STANDARD = 2
        PRO = 3
