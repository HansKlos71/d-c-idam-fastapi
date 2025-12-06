from fastapi import Depends

from app.domain.entities.identities import Identity
from app.drivers.schemas.auth import PasswordAuthenticationRequest, Token, PinAuthenticationRequest
from abc import ABC, abstractmethod
from app.domain.services.generate_token_service import JWTTokenGenerator
from app.domain.ports.repositories.identities_repository import IIdentitiesRepository


class IAuthenticationService(ABC):
    @abstractmethod
    async def authenticate(self, auth_request) -> Token|None:
        pass


class PasswordAuthenticationService(IAuthenticationService):
    def __init__(self, repository: IIdentitiesRepository):
        self.repository = repository

    async def authenticate(
            self,
            auth_request: PasswordAuthenticationRequest,
            tokenizer: JWTTokenGenerator = Depends(JWTTokenGenerator)
        ) -> Token|None:
        identity = await self.repository.password_authentication(auth_request)
        if identity is not None:
            return JWTTokenGenerator().generate_token(identity=identity)
        return None


class PinAuthenticationService(IAuthenticationService):
    def __init__(self, repository: IIdentitiesRepository):
        self.repository = repository

    async def authenticate(
            self,
            auth_request: PinAuthenticationRequest,
            tokenizer: JWTTokenGenerator = Depends(JWTTokenGenerator)
    ) -> Token|None:
        auth_request = auth_request
        identity = await self.repository.pin_authentication(auth_request)
        if identity is not None:
            return JWTTokenGenerator().generate_token(identity=identity)
        return None
