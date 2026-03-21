from typing import TypedDict
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from src.core.database import AsyncEngine, SyncEngine, AsyncSessionMaker, SyncSessionMaker
from src.core.database import create_sync_engine, create_async_engine, create_sync_sessionmaker, create_async_sessionmaker
from src.core.config import settings
from src.core.exception_handlers import add_exception_handlers
from src.core.logger import structlog  # pyright: ignore[reportPrivateLocalImportUsage]


LOGGER = structlog.get_logger(__file__)


class State(TypedDict):
    async_engine: AsyncEngine
    async_sessionmaker: AsyncSessionMaker
    sync_engine: SyncEngine
    sync_sessionmaker: SyncSessionMaker


@asynccontextmanager
async def lifespan(api: FastAPI) -> AsyncIterator[State]:  # pyright: ignore[reportUnusedParameter]
    LOGGER.info("Starting manyS API")

    async_engine = create_async_engine("app")
    async_sessionmaker = create_async_sessionmaker(async_engine)

    sync_engine = create_sync_engine("app")
    sync_sessionmaker = create_sync_sessionmaker(sync_engine)

    yield {
        "async_engine": async_engine,
        "async_sessionmaker": async_sessionmaker,
        "sync_engine": sync_engine,
        "sync_sessionmaker": sync_sessionmaker,
    }

    await async_engine.dispose()
    sync_engine.dispose()

    LOGGER.info("manyS API stopped")


def create_application(router: APIRouter) -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.include_router(router)

    if not settings.is_test():
        pass
    if settings.CORS_ORIGINS is not None:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=settings.CORS_ORIGINS,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    add_exception_handlers(app)

    return app
