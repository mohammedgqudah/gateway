from fastapi import status, Depends, Request
from fastapi_basis.serializers import UUID4

from core.router import APIRouter
from core.depends import get_business
from core.brokers import CustomersBroker

router = APIRouter()


@router.get('/')
async def list_customers(request: Request, business=Depends(get_business)):
    broker = CustomersBroker(request)

    return await broker.list_customers(business_id=business.id, params=request.query_params)


@router.get('/{customer_id}')
async def get_customers(request: Request, customer_id: UUID4, business=Depends(get_business)):
    broker = CustomersBroker(request)

    return await broker.get_customer(
        business_id=business.id,
        customer_id=customer_id,
        params=request.query_params
    )
