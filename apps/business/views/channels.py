from fastapi import Depends, status
from fastapi_baseplate.clients.sqlalchemy.depends import get_db_session
from fastapi_baseplate.server.response import http_response

from apps.channel.models import Channel
from apps.channel.serializers import ChannelOut
from core.depends import get_business
from core.router import APIRouter

router = APIRouter()


@router.get("/")
def list_channels(business=Depends(get_business), session=Depends(get_db_session())):
    channels = session.query(Channel).filter_by(
        business_id=business.id,
    )
    channels = [ChannelOut.from_orm(channel).json() for channel in channels]

    return http_response(
        data=channels,
        status=status.HTTP_200_OK,
    )
