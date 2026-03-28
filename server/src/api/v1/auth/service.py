from src.core.database import AsyncSession
from src.core.security import verify_password
from src.models.user import User
from src.api.v1.user.repository import UserRepository


class AuthService:
    async def login(
        self,
        session: AsyncSession,
        email: str,
        password: str
    ) -> User | None:
        repository = UserRepository.from_session(session)
        user = await repository.get_by_email(email)

        if user is None:
            return None

        if not verify_password(password, user.hashed_password):
            return None

        return user

    async def get_user(self, session: AsyncSession, email: str) -> User | None:
        repository = UserRepository.from_session(session)

        return await repository.get_by_email(email)


auth_service = AuthService()
