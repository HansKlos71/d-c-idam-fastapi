from app.domain.entities.identities import Identity
from app.drivers.schemas.auth import Token


class JWTTokenGenerator:

    def generate_token(self) -> Token:
        # mocked response
        # TODO: Implement JWT token generation
        return Token(
            access_token="access_granted",
            token_type="bearer"
        )