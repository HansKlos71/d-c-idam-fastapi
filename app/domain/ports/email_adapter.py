from abc import ABC, abstractmethod


class  IEmailAdapter(ABC):

    @abstractmethod
    async def send_email(self, identity):
        pass