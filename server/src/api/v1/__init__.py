from fastapi import APIRouter

from .health.endpoints import router as health_router
from .vk.endpoints import router as vk_router


router = APIRouter(prefix='/v1')
router.include_router(health_router)
router.include_router(vk_router)
