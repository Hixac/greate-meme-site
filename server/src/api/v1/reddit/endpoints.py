from fastapi import APIRouter

from .schemas import RedditPost
from .service import reddit_service


router = APIRouter(prefix="/reddit", tags=["reddit"])


@router.get(
    "/hot",
    response_model=list[RedditPost]
)
async def hot(subreddit: str, count: int = 1, offset: int = 0) -> list[RedditPost]:
    posts = await reddit_service.get_posts_from_hot(subreddit, count=count, offset=offset)
    return posts
