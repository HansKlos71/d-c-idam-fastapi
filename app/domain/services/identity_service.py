from app.domain.entities.identities import Identity
from app.domain.ports.repositoriers.identities_repository import IIdentitiesRepository

class IdentityService:
    def __init__(self):
        pass

    def create_identity(self, identity, repository: IIdentitiesRepository ) -> Identity:
        return repository.create_identity(identity)

    def get_identities(self) -> list[Identity]:
        pass

