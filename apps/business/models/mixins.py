from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import declared_attr, relationship


class SubDomainRef(object):
    """Add business reference to mapper using `business.sub_domain`"""

    @declared_attr
    def sub_domain(self):
        return Column(ForeignKey("business.sub_domain", ondelete="CASCADE"))

    @declared_attr
    def business(self):
        return relationship("Business", uselist=False, foreign_keys=[self.sub_domain])


class BusinessRef(object):
    """Add business reference to mapper using `business.id`"""

    @declared_attr
    def business_id(self):
        return Column(ForeignKey("business.id", ondelete="CASCADE"))

    @declared_attr
    def business(self):
        return relationship("Business", uselist=False)
