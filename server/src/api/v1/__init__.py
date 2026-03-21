from fastapi import APIRouter

from .health.endpoints import router as health_router

router = APIRouter(prefix='/v1')
router.include_router(health_router)
