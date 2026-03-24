import os
from enum import StrEnum
from pathlib import Path

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


ENV_VAR: str = "GMS_ENV"


class Environment(StrEnum):
    test = "test"
    production = "production"
    development = "development"


env = Environment(os.getenv(ENV_VAR, Environment.development))
if env == Environment.test:
    env_file = ".env.test"
else:
    env_file = ".env"


class Settings(BaseSettings):
    ENV: Environment = env

    def is_environment(self, environments: set[Environment]) -> bool:
        return self.ENV in environments

    def is_test(self) -> bool:
        return self.is_environment({Environment.test})

    APP_NAME: str
    LOG_LEVEL: str
    WWW_AUTHENTICATE_REALM: str = "gms"

    CORS_ORIGINS: list[str] | None = None


    # POSTGRES SETTINGS

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_NAME: str
    POSTGRES_PORT: int
    POSTGRES_HOST: str

    POSTGRES_POOL_SIZE: int = 5
    POSTGRES_SYNC_POOL_SIZE: int = 1  # Specific pool size for sync connection: since we only use it in OAuth2 router, don't waste resources.
    POSTGRES_POOL_RECYCLE_SECONDS: int = 600  # 10 minutes
    POSTGRES_COMMAND_TIMEOUT_SECONDS: float = 30.0

    POSTGRES_SYNC_PREFIX: str = "postgresql://"
    POSTGRES_ASYNC_PREFIX: str = "postgresql+asyncpg://"

    @computed_field
    @property
    def sync_postgres_uri(self) -> str:
        return f"{self.POSTGRES_SYNC_PREFIX}{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_NAME}"

    @computed_field
    @property
    def async_postgres_uri(self) -> str:
        return f"{self.POSTGRES_ASYNC_PREFIX}{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_NAME}"

    # END OF POSTGRES SETTINGS

    VK_SERVICE_KEY: str

    model_config = SettingsConfigDict(
        env_file=Path(__file__).parent.parent.parent.joinpath(env_file)
    )


settings = Settings()
