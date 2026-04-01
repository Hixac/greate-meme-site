from typing import Annotated
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class IDSchema(BaseModel):
    id: Annotated[UUID, Field(default_factory=uuid4)]
