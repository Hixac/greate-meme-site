from pydantic import BaseModel, EmailStr


class AuthLoginSchema(BaseModel):
    email: EmailStr
    password: str


class AuthRegisterSchema(BaseModel):
    username: str
    email: EmailStr
    password: str
