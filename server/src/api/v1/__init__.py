from fastapi import APIRouter

from .health.endpoints import router as health_router
from .vk.endpoints import router as vk_router
from .reddit.endpoints import router as reddit_router
from .user.endpoints import router as user_router
from .auth.endpoints import router as auth_router


router = APIRouter(prefix='/v1')
router.include_router(health_router)
router.include_router(vk_router)
router.include_router(user_router)
router.include_router(auth_router)
router.include_router(reddit_router)
