from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from src.core.database import AsyncSession, get_db_session
from .schemas import UserCreate, UserResponse
from .service import user_service


router = APIRouter(prefix="/user", tags=["user"])


@router.post(
    "/",
    status_code=201
)
async def user(
    user_data: UserCreate,
    session: Annotated[AsyncSession, Depends(get_db_session)]
) -> UserResponse:
    user = await user_service.create(
        session,
        username=user_data.username,
        email=user_data.email,
        password=user_data.password
    )

    return user


@router.get(
    "/{id}"
)
async def get(
    id: UUID,
    session: Annotated[AsyncSession, Depends(get_db_session)]
) -> UserResponse:
    user = await user_service.get(
        session,
        id
    )

    return user
