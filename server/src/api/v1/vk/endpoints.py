from fastapi import APIRouter

from .schemas import VKPost
from .service import vk_service


router = APIRouter(prefix="/vk", tags=["vk"])


@router.get(
    "/wall",
    response_model=list[VKPost]
)
async def wall(group: str, count: int = 1, offset: int = 0) -> list[VKPost]:
    posts = await vk_service.get_posts(group, count=count, offset=offset)
    return posts
