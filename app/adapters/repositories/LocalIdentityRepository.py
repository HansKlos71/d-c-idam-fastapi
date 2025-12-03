from app.domain.ports.repositoriers.identities_repository import IIdentitiesRepository
from app.domain.entities.identities import Identity
from app.drivers.schemas.identities import CreateIdentity, IdentityResponse


identities: list[Identity] = []

class LocalIdentityRepository(IIdentitiesRepository):
    def __init__(self):
        pass

    def create_identity(self, identity: CreateIdentity) -> IdentityResponse:
        # build domain entity
        domain_identity = Identity(
            id="1",
            email=identity.email,
            username=identity.username
        )
        # Add identity to the memory list
        identities.append(domain_identity)
        # map to response schema
        response = IdentityResponse(
            id=domain_identity.id,
            email=domain_identity.email,
            username=domain_identity.username
        )
        return response

    def get_identities(self) -> list[Identity]:
        return identities


    def update_identity(self, identity_id: str) -> Identity:
        pass