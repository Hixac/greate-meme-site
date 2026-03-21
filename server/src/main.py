from fastapi import FastAPI

from src.core.setup import create_application
from src.api import router


app: FastAPI = create_application(router)
