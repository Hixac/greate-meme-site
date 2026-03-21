from datetime import datetime, UTC

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from src.core.config import settings
from .schemas import HealthResponse


router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
async def health():
    http_status = status.HTTP_200_OK
    response = {
        "status": http_status,
        "version": "0.0.1",
        "timestamp": datetime.now(UTC).isoformat(timespec="seconds"),
        "environment": settings.ENV
    }

    return JSONResponse(status_code=http_status, content=response)
