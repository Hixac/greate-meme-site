from uuid import UUID
import structlog
from sqlalchemy.exc import IntegrityError, NoResultFound

from src.core.exceptions import ResourceNotFound
from src.core.database import AsyncSession
from src.core.security import hash_password
from src.api.v1.user.repository import UserRepository
from src.models.user import User

from .schemas import UserResponse


LOGGER = structlog.get_logger(__file__)


class UserService:
    async def create(
        self,
        session: AsyncSession,
        *,
        username: str,
        email: str,
        password: str
    ) -> UserResponse:
        repo = UserRepository.from_session(session)

        try:
            user = await repo.create(User(
                username=username,
                email=email,
                hashed_password=hash_password(password)
            ), flush=True)

            LOGGER.info("user.create.success")
            return UserResponse(email=user.email, username=user.username)
        except IntegrityError as _:
            LOGGER.warning("user.create.constraint_violation")  # only raises if email duplicate
            raise

    async def get(
        self,
        session: AsyncSession,
        id: UUID
    ) -> UserResponse:
        repo = UserRepository.from_session(session)

        try:
            user = await repo.get_or_raise(id)
        except NoResultFound:
            LOGGER.warning("user.get.no_result_found")
            raise ResourceNotFound()

        LOGGER.info("user.get.success")
        return UserResponse(email=user.email, username=user.username)


user_service = UserService()
