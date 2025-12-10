from typing import Dict, Any
import asyncio
import requests

from app.domain.entities.identities import Identity
from app.domain.ports.email_adapter import IEmailAdapter
from app.config.settings import settings


TEMPLATE_ID = settings.MAILERSEND_TEMPLATE_ID
EMAIL_FROM = settings.MAILERSEND_EMAIL_FROM
API_KEY = settings.MAILERSEND_API_KEY
# Keep legacy name used by older modules
MAILER_SEND_API_URL = str(settings.MAILERSEND_BASE_URL)


class ConsoleEmailAdapter(IEmailAdapter):
    async def send_email(self, identity: Identity, from_email: str | None = None, template_id: str | None = None) -> Dict[str, Any]:
        from_email = from_email or EMAIL_FROM or "no-reply@example.com"
        template_id = template_id or TEMPLATE_ID or ""

        payload = {
            "from": {"email": from_email},
            "to": [{"email": identity.email, "name": getattr(identity, "username", "")}],
            "template_id": template_id,
            "identity": {"id": getattr(identity, "id", None), "activation_code": getattr(identity, "activation_code", None)},
        }

        # Keep the API shape similar to MailerSendClient for consumers.
        print("[ConsoleEmailAdapter] sending email payload:")
        print(payload)
        return {"status": "console", "payload": payload}


class MailerSendClient(IEmailAdapter):
    def __init__(self, api_key: str | None = None, base_url: str | None = None, timeout: int = 10) -> None:
        self.api_key = api_key or settings.MAILERSEND_API_KEY
        self.base_url = (base_url or str(settings.MAILERSEND_BASE_URL)).rstrip("/")
        self.timeout = timeout

        if not self.api_key:
            raise RuntimeError(
                "Missing MAILERSEND_API_KEY environment variable; set MAILERSEND_API_KEY in the environment or .env file"
            )

        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        })

    def _url(self, path: str) -> str:
        path = (path or "").lstrip("/")
        return f"{self.base_url}/{path}" if path else self.base_url

    def post(self, path: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        url = self._url(path)
        response = self.session.post(url, json=payload, timeout=self.timeout)
        response.raise_for_status()
        # Some endpoints (or error pages) may return an empty body or non-JSON content.
        # Be defensive: attempt to decode JSON and fall back to returning status/text.
        try:
            return response.json()
        except ValueError:
            # response.text may be large; return concise info for debugging.
            return {"status_code": response.status_code, "text": (response.text or "")}

    async def send_email(self, identity: Identity, from_email: str | None = None, template_id: str | None = None) -> Dict[str, Any]:
        from_email = from_email or EMAIL_FROM
        template_id = template_id or TEMPLATE_ID

        payload = {
            "from": {"email": from_email},
            "to": [{"email": identity.email, "name": getattr(identity, "username", "")}],
            "template_id": template_id,
        }
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(None, lambda: self.post("email", payload))