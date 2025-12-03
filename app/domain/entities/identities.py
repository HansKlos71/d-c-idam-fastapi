import datetime
from dataclasses import dataclass, field
from pydantic import EmailStr
from typing import Optional


@dataclass
class Identity:
    id: str
    username: str
    email: EmailStr
    password: str # TODO: change to hashed password
    pin: Optional[str] # TODO: change to hashed pin
    activated_at: Optional[datetime.datetime] = None
    deactivated_at: Optional[datetime.datetime] = None
    created_at: datetime.datetime = field(default_factory=lambda: datetime.datetime.now(datetime.UTC))
    updated_at: datetime.datetime = field(default_factory=lambda: datetime.datetime.now(datetime.UTC))

    def validate_pin(self) -> str:
        if len(self.pin) != 4 or not self.pin.isdigit():
            raise ValueError("PIN must be 4 digits long")
        return self.pin

    def validate_password(self) -> str:
        if self.pin is None:
            pass
        if len(self.password) < 8: # TODO: add more complex password validation
            raise ValueError("Password must be at least 8 characters long")
        return self.password