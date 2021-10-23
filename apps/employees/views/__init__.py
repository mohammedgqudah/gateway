from fastapi import Depends

from core.depends import CheckAccessToken
from core.router import APIRouter

from .staff import router as staff_router

router = APIRouter(dependencies=[Depends(CheckAccessToken())])

router.include_router(staff_router)
