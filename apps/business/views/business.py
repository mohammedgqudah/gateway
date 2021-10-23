from fastapi import Depends, status
from fastapi_baseplate.server.response import http_response

from core.depends import get_business
from core.router import APIRouter

from ..serializers import BusinessBase

router = APIRouter()


@router.get("/")
def business_info(business=Depends(get_business)):
    """Get business data as an employee."""
    return http_response(
        data=BusinessBase.from_orm(business).json(),
        status=status.HTTP_200_OK,
    )
