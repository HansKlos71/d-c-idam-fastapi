from app.domain.entities.identities import Identity
from app.drivers.schemas.identities import IdentityResponse

class IdentityMapper:

    @staticmethod
    def map_to_response(domain_identity: Identity) -> IdentityResponse:
        return IdentityResponse(
            id=domain_identity.id,
            email=domain_identity.email,
            username=domain_identity.username
        )