from app.domain.entities.identities import Identity
from app.drivers.schemas.auth import PasswordAuthenticationRequest, Token
from abc import ABC, abstractmethod

from app.domain.ports.repositories.identities_repository import IIdentitiesRepository

class Tokenizer:
    def generate_token(self, identity: Identity) -> Token:
        active_token = Token()
        active_token.access_token, active_token.token_type = "access_granted", "bearer"
        return active_token


class IAuthenticationService(ABC):
    @abstractmethod
    def authenticate(self, auth_request) -> Token|None:
        pass


class PasswordAuthenticationService(IAuthenticationService):
    def __init__(self, repository: IIdentitiesRepository):
        self.repository = repository

    def authenticate(
            self,
            auth_request: PasswordAuthenticationRequest
        ) -> Token|None:

        identity = self.repository.password_authentication(auth_request)
        if identity is not None:
            token = Tokenizer().generate_token(identity)
            return token
        return None


