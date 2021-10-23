from fastapi import Depends

from core.depends import CheckAccessToken
from core.router import APIRouter

from .business import router as business_router
from .catalog import router as catalog_router
from .channels import router as channels_router
from .customers import router as customers_router

router = APIRouter(prefix="/business", dependencies=[Depends(CheckAccessToken())])

router.include_router(business_router)
router.include_router(customers_router, prefix="/customers")
router.include_router(catalog_router, prefix="/catalog")
router.include_router(channels_router, prefix="/channels")
