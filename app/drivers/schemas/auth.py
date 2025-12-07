from pydantic import BaseModel, Field

class PasswordAuthenticationRequest(BaseModel):
    username: str
    password: str


class PinAuthenticationRequest(BaseModel):
    username: str
    pin: str


class Token(BaseModel):
    access_token: str
    token_type: str
    username: str