from app.domain.entities.identities import Identity
from app.domain.ports.email_adapter import IEmailAdapter

class ActivateIdentityService:
    async def activate_identity(
            self,
            identity: Identity,
            email_adapter: IEmailAdapter
    ) -> bool:
        return await email_adapter.send_email(identity)
