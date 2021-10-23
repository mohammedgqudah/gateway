from fastapi import Depends, Request
from fastapi_baseplate.serializers import UUID4

from core.router import APIRouter
from core.depends import get_business
from core.brokers import CustomersBroker

router = APIRouter()


@router.get("/")
async def list_customers(request: Request, business=Depends(get_business)):
    broker = CustomersBroker(request)

    return await broker.list_customers(business_id=business.id, params=request.query_params)


@router.get("/{customer_id}")
async def get_customers(request: Request, customer_id: UUID4, business=Depends(get_business)):
    broker = CustomersBroker(request)

    return await broker.get_customer(
        business_id=business.id,
        customer_id=customer_id,
        params=request.query_params,
    )


@router.post("/")
async def create_customer(request: Request, business=Depends(get_business)):
    broker = CustomersBroker(request)

    return await broker.create_customer(
        business_id=business.id,
        params=request.query_params,
        json={
            **await request.json(),
            "sub_domain": business.sub_domain,
        },
    )


@router.put("/{customer_id}")
async def update_customer(request: Request, customer_id: UUID4, business=Depends(get_business)):
    broker = CustomersBroker(request)

    return await broker.update_customer(
        business_id=business.id,
        customer_id=customer_id,
        params=request.query_params,
        json={
            **await request.json(),
            "sub_domain": business.sub_domain,
        },
    )
