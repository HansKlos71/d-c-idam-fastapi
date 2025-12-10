from abc import ABC, abstractmethod


class  IEmailAdapter(ABC):

    @abstractmethod
    async def send_email(
            self,
            identity,
            from_email: str,
            template_id: str
    ):
        pass