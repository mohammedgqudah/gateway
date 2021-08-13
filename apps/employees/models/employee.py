from sqlalchemy import Column, String, Boolean, UniqueConstraint, ForeignKey
from sqlalchemy.orm import column_property

from core.db import Base
from apps.business.models import SubDomainRef


class Employee(Base, SubDomainRef):
    email = Column('email', String)
    password = Column('password', String)
    first_name = Column('first_name', String)
    last_name = Column('last_name', String, nullable=True)
    fullname = column_property(first_name + last_name)

    type = Column('type', String)
    is_active = Column('is_active', Boolean, default=True, server_default='true')

    __table_args__ = (
        UniqueConstraint('sub_domain', 'email', name='_sub_domain_staff_email'),
    )

    class Types:
        pass
