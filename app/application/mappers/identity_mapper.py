from app.domain.entities.identities import Identity
from app.drivers.schemas.identities import IdentityResponse

class IdentityMapper:

    def identity_to_created_identity_response(self, domain_identity: Identity) -> IdentityResponse:
        identity = domain_identity

        response = IdentityResponse(
            id=identity.id,
            email=identity.email,
            username=identity.username
        )
        return response