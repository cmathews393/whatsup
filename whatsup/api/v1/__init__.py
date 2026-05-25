from fastapi import APIRouter
from .health import health_router
from .monitors import monitors_router

router = APIRouter(prefix="/v1")

router.include_router(health_router)
router.include_router(monitors_router)
