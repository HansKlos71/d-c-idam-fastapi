from app.drivers.schemas.auth import PasswordAuthenticationRequest, Token
from abc import ABC, abstractmethod

from app.domain.ports.repositories.identities_repository import IIdentitiesRepository


class IAuthenticationService(ABC):
    @abstractmethod
    def authenticate(self, auth_request) -> Token:
        pass


class PasswordAuthenticationService(IAuthenticationService):
    def __init__(self, repository: IIdentitiesRepository):
        self.repository = repository

    def authenticate(
            self,
            auth_request: PasswordAuthenticationRequest
        ) -> Token:

        return Token