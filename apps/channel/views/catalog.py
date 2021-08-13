from fastapi import status, Depends, Request
from fastapi_basis.serializers import UUID4

from core.router import APIRouter
from core.depends import get_business
from core.brokers import CatalogBroker
from core.serializers.types import ObjectId

router = APIRouter()


@router.get('/products')
def list_available_products(request: Request, channel_id: UUID4, business=Depends(get_business)):
    broker = CatalogBroker(request)
    return broker.list_available_products(business_id=business.id, channel_id=channel_id, params=request.query_params)


@router.get('/products/{product_id}')
def get_available_product(request: Request, product_id: ObjectId, channel_id: UUID4, business=Depends(get_business)):
    broker = CatalogBroker(request)

    return broker.get_available_product(
        business_id=business.id,
        channel_id=channel_id,
        product_id=product_id,
        params=request.query_params
    )
