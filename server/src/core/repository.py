from uuid import UUID

from sqlalchemy import select

from src.core.database import AsyncSession
from src.core.models import RecordModel


class RepositoryBase[T: RecordModel]:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_or_raise(self, id: UUID) -> T:
        statement = select(T).where(T.id == id)

        res = await self.session.execute(statement)
        return res.scalar_one()

    async def create(self, object: T, *, flush: bool = False) -> T:
        self.session.add(object)

        if flush:
            await self.session.flush()

        return object

    @classmethod
    def from_session(cls, session: AsyncSession):
        return cls(session)
