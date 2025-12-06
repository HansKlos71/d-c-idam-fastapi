from app.domain.entities.identities import Identity
from app.drivers.schemas.auth import Token


class JWTTokenGenerator:

    def generate_token(self, identity) -> Token:
        # mocked response
        # TODO: Implement JWT token generation
        username = identity.username
        return Token(
            access_token="access_granted",
            token_type="bearer",
            username=username

        )