from pydantic import BaseModel, EmailStr


class CreateIdentity(BaseModel):
    email: EmailStr
    username: str
    password: str


class IdentityResponse(BaseModel):
    id: str
    email: EmailStr
    username: str