from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class CreateIdentity(BaseModel):
    email: EmailStr
    username: str
    password: str
    pin: Optional[str] = Field(None, min_length=4, max_length=4, pattern=r'^\d{4}$')


class UpdateIdentity(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    password: Optional[str] = None
    pin: Optional[str] = Field(None, min_length=4, max_length=4, pattern=r'^\d{4}$')


class IdentityResponse(BaseModel):
    id: str
    email: EmailStr
    username: str