from pydantic import BaseModel, Field

class PasswordAuthenticationRequest(BaseModel):
    username: str
    password: str


class PinAuthenticationRequest(BaseModel):
    username: str
    pin: str = Field(min_length=4, max_length=4, pattern=r'^\d{4}$')


class Token(BaseModel):
    access_token: str
    token_type: str
    username: str