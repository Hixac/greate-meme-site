from pydantic import BaseModel, EmailStr, SecretStr


class AuthLoginSchema(BaseModel):
    email: EmailStr
    password: SecretStr


class AuthRegisterSchema(BaseModel):
    username: str
    email: EmailStr
    password: SecretStr
