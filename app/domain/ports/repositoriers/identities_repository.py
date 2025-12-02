from abc import ABC, abstractclassmethod
from app.domain.entities.identities import Identity
from app.drivers.schemas.identities import CreateIdentity


class IIdentitiesRepository(ABC):

    @abstractclassmethod
    def create_identity(self, identity: CreateIdentity) -> Identity:
        pass

    @abstractclassmethod
    def get_identities(self) -> list[Identity]:
        pass

    @abstractclassmethod
    def update_identity(self, identity_id: str) -> Identity:
        pass