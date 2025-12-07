from tkinter import BooleanVar

from app.domain.entities.identities import Identity
from app.domain.ports.emailer_adapter import EmailerAdapter
from app.domain.ports.emailer_adapter import EmailerAdapter

class ActivateIdentityService:
    async def activate_identity(
            self,
            identity: Identity,
            email_adapter: EmailerAdapter
    ) -> bool:
        return await email_adapter.send_email(identity)
