from sqlalchemy import Boolean, Column, String, UniqueConstraint
from sqlalchemy.orm import column_property

from apps.business.models import SubDomainRef
from core.db import Base


class Employee(Base, SubDomainRef):
    email = Column("email", String)
    password = Column("password", String)
    first_name = Column("first_name", String)
    last_name = Column("last_name", String, nullable=True)
    fullname = column_property(first_name + last_name)

    type = Column("type", String)
    is_active = Column("is_active", Boolean, default=True, server_default="true")

    __table_args__ = (UniqueConstraint("sub_domain", "email", name="unique_email"),)

    class Types:
        pass
