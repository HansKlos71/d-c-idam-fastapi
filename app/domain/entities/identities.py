from dataclasses import dataclass
from pydantic import EmailStr


@dataclass
class Identity:
    id: str
    username: str
    email: EmailStr

