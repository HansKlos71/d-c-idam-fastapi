from app.domain.ports.repositories.identities_repository import IIdentitiesRepository
from app.drivers.schemas.identities import CreateIdentity, IdentityResponse, UpdateIdentity
from app.domain.entities.identities import Identity


identities: list[Identity] = []

class InMemoryIdentityRepository(IIdentitiesRepository):

    async def create_identity(self, identity: CreateIdentity) -> IdentityResponse:

        # build domain entity
        domain_identity = Identity(
            id=str(len(identities)+1),
            email=identity.email,
            username=identity.username,
            password=identity.password,
            pin=identity.pin
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

    async def get_identities(self) -> list[Identity]:
        return identities


    async def update_identity(self, identity_id: str, identity: UpdateIdentity) -> Identity:
            identity_to_update = next((x for x in identities if x.id == identity_id), None)

            if identity.email:
                identity_to_update.email = identity.email
            if identity.username:
                identity_to_update.username = identity.username

            # not optimal, so it's temporary for local testing
            for index, identity in enumerate(identities):
                if identity.id == identity_id:
                    identities[index] = identity_to_update
                    break

            return identity_to_update

