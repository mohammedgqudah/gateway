from fastapi import Depends, Request
from fastapi_baseplate.serializers import ObjectId

from core.router import APIRouter
from core.depends import get_business
from core.brokers import CatalogBroker

router = APIRouter()


@router.get('/products')
async def list_products(request: Request, business=Depends(get_business)):
    """List business products."""
    broker = CatalogBroker(request)

    return await broker.list_products(business_id=business.id, params=request.query_params)


@router.get('/products/{product_id}')
async def get_product(request: Request, product_id: ObjectId, business=Depends(get_business)):
    broker = CatalogBroker(request)

    return await broker.get_product(
        business_id=business.id,
        product_id=product_id,
        params=request.query_params
    )


@router.put('/products/{product_id}')
async def update_product(product_id: ObjectId, request: Request, business=Depends(get_business)):
    broker = CatalogBroker(request)

    return await broker.update_product(
        business_id=business.id,
        product_id=product_id,
        params=request.query_params,
        json=await request.json()
    )


@router.post('/products')
async def create_product(request: Request, business=Depends(get_business)):
    broker = CatalogBroker(request)

    return await broker.create_product(
        business_id=business.id,
        params=request.query_params,
        json=await request.json()
    )
