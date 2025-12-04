from abc import ABC, abstractmethod
from app.domain.entities.identities import Identity
from app.drivers.schemas.auth import PasswordAuthenticationRequest
from app.drivers.schemas.identities import CreateIdentity, UpdateIdentity


class IIdentitiesRepository(ABC):

    @abstractmethod
    async def create_identity(self, identity: CreateIdentity) -> Identity:
        pass

    @abstractmethod
    async def get_identities(self) -> list[Identity]:
        pass

    @abstractmethod
    async def update_identity(self, identity_id: str, identity: UpdateIdentity) -> Identity:
        pass

    async def password_authentication(self, auth_request: PasswordAuthenticationRequest) -> Identity:
        pass