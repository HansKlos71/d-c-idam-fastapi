from app.domain.entities.identities import Identity
from app.domain.ports.repositoriers.identities_repository import IIdentitiesRepository


class IdentityService:
    def __init__(self, repository: IIdentitiesRepository):
        self.repository = repository

    def create_identity(self, identity) -> Identity:
        return self.repository.create_identity(identity)

    def get_identities(self) -> list[Identity]:
        return self.repository.get_identities()

