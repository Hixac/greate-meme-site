import uuid
from datetime import datetime
from zoneinfo import ZoneInfo


mow_tz = ZoneInfo('Europe/Moscow')


def mow_now() -> datetime:
    return datetime.now(mow_tz)


def generate_uuid() -> uuid.UUID:
    return uuid.uuid4()
