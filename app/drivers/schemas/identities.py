from pydantic import BaseModel, EmailStr
from typing import Optional


class CreateIdentity(BaseModel):
    email: EmailStr
    username: str
    password: str
    pin: Optional[str] = None


class UpdateIdentity(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    password: Optional[str] = None


class IdentityResponse(BaseModel):
    id: str
    email: EmailStr
    username: str