from app.domain.entities.identities import Identity


class EmailAdapter:
    async def send_email(
            self,
            identity: Identity,
    ):
        print("Sending email:")
        print(f"Receiver: {identity.email}")
        print(f"Subject: Please activate your account")
        print(f"Click the following link to activate your account: {identity.activation_code}")

