from fastapi import Depends

from app.domain.entities.identities import Identity
from app.drivers.schemas.auth import PasswordAuthenticationRequest, Token
from abc import ABC, abstractmethod
from app.domain.services.generate_token_service import JWTTokenGenerator
from app.domain.ports.repositories.identities_repository import IIdentitiesRepository


class IAuthenticationService(ABC):
    @abstractmethod
    def authenticate(self, auth_request) -> Token|None:
        pass


class PasswordAuthenticationService(IAuthenticationService):
    def __init__(self, repository: IIdentitiesRepository):
        self.repository = repository

    def authenticate(
            self,
            auth_request: PasswordAuthenticationRequest,
            tokenizer: JWTTokenGenerator = Depends(JWTTokenGenerator)
        ) -> Token|None:
        auth_request = auth_request
        tokenizer = JWTTokenGenerator()
        identity = self.repository.password_authentication(auth_request)
        if identity is not None:
            token = tokenizer.generate_token()
            return token
        return None


