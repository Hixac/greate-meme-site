from typing import Any
from pprint import pprint

import httpx
import asyncpraw

from src.core.config import settings
from .schemas import RedditPost, RedditPublisher


class RedditService:
    def __init__(self) -> None:
        self.praw = asyncpraw.Reddit(
            client_id=settings.REDDIT_CLIENT_ID,
            client_secret=settings.REDDIT_CLIENT_SECRET,
            user_agent=settings.REDDIT_USER_AGENT
        )

    def _scrape_gallery(self, post: Any) -> list[str]:  # ну и залупа ебаная
        pics: list[str] = []

        if hasattr(post, "crosspost_parent_list"):
            for metadata in post.crosspost_parent_list[0]["media_metadata"].values():
                pics.append(metadata["s"]["u"])
        elif hasattr(post, "media_metadata"):
            for metadata in post.media_metadata.values():
                pics.append(metadata["s"]["u"])

        return pics

    async def get_posts_from_hot(self, sub_name: str, count: int, offset: int) -> list[RedditPost]:
        subreddit = await self.praw.subreddit(sub_name)
        post_generator = subreddit.hot(limit=offset+count)

        for _ in range(offset):  # мб фиксится?
            _ = anext(post_generator)

        urls: list[str] = []
        posts: list[RedditPost] = []
        async for post in post_generator:
            url = httpx.URL(post.url)
            if "gallery" in url.path.split("/"):
                urls = self._scrape_gallery(post)
            elif url.path.find(".") != -1:
                urls.append(post.url)

            posts.append(RedditPost(
                upvotes=post.score,
                timestamp=post.created_utc,
                is_pinned=post.stickied,
                text=post.selftext,
                photos_url=urls,
                publisher=RedditPublisher(
                    photo_url="",
                    name=subreddit.display_name
                )
            ))

        return posts


reddit_service = RedditService()
