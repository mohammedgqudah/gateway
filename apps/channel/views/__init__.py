from fastapi import Depends

from core.router import APIRouter
from core.depends import CheckAccessToken
from .catalog import router as catalog_router

router = APIRouter(prefix='/business/channel/{channel_id}', dependencies=[Depends(CheckAccessToken())])

router.include_router(catalog_router, prefix="/catalog")
