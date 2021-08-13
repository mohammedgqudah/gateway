from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import declared_attr, relationship


class ChannelRef(object):
    """Add channel reference to mapper using `channel.id`
    """

    @declared_attr
    def channel_id(self):
        return Column(ForeignKey('channel.id', ondelete='CASCADE'))

    @declared_attr
    def channel(self):
        return relationship('Channel', uselist=False)
