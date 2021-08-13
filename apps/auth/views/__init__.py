from core.router import APIRouter

# from .customers_auth import router as customers_router
from .employees_auth import router as employees_router

router = APIRouter(prefix="/auth")

router.include_router(employees_router, prefix="/employees")
