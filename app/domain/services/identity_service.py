from app.domain.entities.identities import Identity
from app.domain.ports.repositories.identities_repository import IIdentitiesRepository
from app.drivers.schemas.identities import CreateIdentity, UpdateIdentity


class IdentityService:
    def __init__(self, repository: IIdentitiesRepository):
        self.repository = repository

    async def create_identity(self, identity: CreateIdentity) -> Identity:
        return await self.repository.create_identity(identity)

    async def get_identities(self) -> list[Identity]:
        return await self.repository.get_identities()

    async def update_identity(self, identity_id: str, identity: UpdateIdentity) -> Identity:
        return await self.repository.update_identity(identity_id, identity)