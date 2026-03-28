from datetime import datetime
from typing import override
from uuid import UUID

from sqlalchemy import TIMESTAMP, Uuid, inspect
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.core.utilities import mow_now, generate_uuid


class Model(DeclarativeBase):
    __abstract__ = True


class TimestampedModel(Model):
    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), nullable=False, default=mow_now, index=True
    )
    modified_at: Mapped[datetime | None] = mapped_column(
        TIMESTAMP(timezone=True), onupdate=mow_now, nullable=True, default=None
    )
    deleted_at: Mapped[datetime | None] = mapped_column(
        TIMESTAMP(timezone=True), nullable=True, default=None, index=True
    )

    def set_modified_at(self) -> None:
        self.modified_at = mow_now()

    def set_deleted_at(self) -> None:
        self.deleted_at = mow_now()


class IDModel(Model):
    __abstract__ = True

    id: Mapped[UUID] = mapped_column(Uuid, primary_key=True, default=generate_uuid)

    @override
    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, self.__class__) and self.id == __value.id

    @override
    def __hash__(self) -> int:
        return self.id.int

    @override
    def __repr__(self) -> str:
        # We do this complex thing because we might be outside a session with
        # an expired object; typically when Sentry tries to serialize the object for
        # error reporting.
        # But basically, we want to show the ID if we have it.
        insp = inspect(self)
        if insp.identity is not None:
            id_value = insp.identity[0]
            return f"{self.__class__.__name__}(id={id_value!r})"
        return f"{self.__class__.__name__}(id=None)"

    @classmethod
    def generate_id(cls) -> UUID:
        return generate_uuid()


class RecordModel(IDModel, TimestampedModel):
    __abstract__ = True
