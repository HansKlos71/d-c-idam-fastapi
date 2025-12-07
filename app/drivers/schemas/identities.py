from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class CreateIdentity(BaseModel):
    email: EmailStr = Field(min_length=6, max_length=128)
    username: str = Field(min_length=4, max_length=128)
    password: str = Field(min_length=8, max_length=128)
    pin: Optional[str] = Field(None, min_length=4, max_length=4, pattern=r'^\d{4}$')


class UpdateIdentity(BaseModel):
    email: Optional[EmailStr] = Field(None, min_length=6, max_length=128)
    username: Optional[str] = Field(None, min_length=4, max_length=128)
    password: Optional[str] = Field(None,min_length=8, max_length=128)
    pin: Optional[str] = Field(None, min_length=4, max_length=4, pattern=r'^\d{4}$')


class IdentityResponse(BaseModel):
    id: str
    email: EmailStr
    username: str