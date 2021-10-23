from apps.auth.views import router as auth_router
from apps.business.views import router as business_router
from apps.channel.views import router as channel_router

from .router import APIRouter

router = APIRouter(prefix="/api/v1")

router.include_router(auth_router)
router.include_router(business_router)
router.include_router(channel_router)
