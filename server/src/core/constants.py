from enum import StrEnum


ENV_VAR: str = "GMS_ENV"


class Environment(StrEnum):
    test = "test"
    production = "production"
    development = "development"
