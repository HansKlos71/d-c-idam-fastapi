from fastapi import HTTPException

from app.domain.entities.identities import Identity
from app.domain.ports.repositories.identities_repository import IIdentitiesRepository
from app.domain.ports.emailer_adapter import EmailAdapter
from app.drivers.schemas.identities import CreateIdentity, UpdateIdentity


class IdentityService:
    def __init__(self, repository: IIdentitiesRepository):
        self.repository = repository

    async def create_identity(
            self,
            identity: CreateIdentity,
            email_adapter: EmailAdapter # TODO inject via DI
    ) -> Identity|None:
        new_identity = await self.repository.create_identity(identity)
        if new_identity is not None:
            await email_adapter.send_email(new_identity)
            return new_identity
        return None

    async def get_identities(self) -> list[Identity]:
        return await self.repository.get_identities()

    async def update_identity(self, identity_id: str, identity: UpdateIdentity) -> Identity:
        return await self.repository.update_identity(identity_id, identity)