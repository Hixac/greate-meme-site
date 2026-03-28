from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.models import RecordModel


class User(RecordModel):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))

    is_deleted: Mapped[bool] = mapped_column(default=False, index=True)
    is_superuser: Mapped[bool] = mapped_column(default=False)
