from app.domain.ports.repositoriers.identities_repository import IIdentitiesRepository
from app.domain.entities.identities import Identity
from app.drivers.schemas.identities import CreateIdentity, IdentityResponse

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
        # map to response schema
        response = IdentityResponse(
            id=domain_identity.id,
            email=domain_identity.email,
            username=domain_identity.username
        )
        return response

    def get_identities(self) -> list[Identity]:
        pass


    def update_identity(self, identity_id: str) -> Identity:
        pass