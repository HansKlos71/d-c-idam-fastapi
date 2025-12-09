import secrets
from app.domain.ports.repositories.identities_repository import IIdentitiesRepository
from app.drivers.schemas.auth import PasswordAuthenticationRequest, PinAuthenticationRequest
from app.drivers.schemas.identities import CreateIdentity, UpdateIdentity
from app.domain.entities.identities import Identity


identities: list[Identity] = []

class InMemoryIdentityRepository(IIdentitiesRepository):

    async def create_identity(self, identity: CreateIdentity) -> Identity:
        # build domain entity
        domain_identity = Identity(
            id=str(len(identities)+1),
            email=identity.email,
            username=identity.username,
            password=identity.password,
            pin=identity.pin
        )

        # Generate a random activation code and ensure uniqueness in-memory
        code = secrets.token_urlsafe(16)
        domain_identity.activation_code = code

        # Add identity to the memory list
        identities.append(domain_identity)

        return domain_identity

    async def get_identities(self) -> list[Identity]:
        return identities


    async def update_identity(self, identity_id: str, identity: UpdateIdentity) -> Identity:
            identity_to_update = next((x for x in identities if x.id == identity_id), None)
            if identity_to_update is None:
                raise ValueError(f"Identity with id '{identity_id}' not found")

            if identity.email:
                identity_to_update.email = identity.email
            if identity.username:
                identity_to_update.username = identity.username

            # not optimal, so it's temporary for local testing
            for index, identity_item in enumerate(identities):
                if identity_item.id == identity_id:
                    identities[index] = identity_to_update
                    break

            return identity_to_update

    async def password_authentication(self, auth_request: PasswordAuthenticationRequest) -> Identity|None:
        for identity in identities:
            if identity.username == auth_request.username:
                if identity.validate_password() == auth_request.password:
                    print(f"Debugger: The identity fetched from the repository {identity}")
                    return identity
                break
        return None


    async def pin_authentication(self, auth_request: PinAuthenticationRequest) -> Identity|None:
        for identity in identities:
            if identity.username == auth_request.username:
                if identity.pin == auth_request.pin:
                    print(f"Debugger: The identity fetched from the repository {identity}")
                    return identity
                break
        return None