from pydantic import BaseModel

class PasswordAuthenticationRequest(BaseModel):
    username: str
    password: str


class Token:
    access_token: str
    token_type: str