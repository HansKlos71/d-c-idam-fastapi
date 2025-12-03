from fastapi import APIRouter, Depends
from app.adapters.repositories.InMemoryIdentityRepository import InMemoryIdentityRepository
from app.domain.services.authentication_service import IAuthenticationService, PasswordAuthenticationService
from app.drivers.schemas.auth import PasswordAuthenticationRequest, Token

router = APIRouter()

def get_password_authentication_service() -> IAuthenticationService:
    return PasswordAuthenticationService(InMemoryIdentityRepository)


@router.post("/password/authenticate", response_model=Token)
async def login(
        auth_request: PasswordAuthenticationRequest,
        service: IAuthenticationService = Depends(get_password_authentication_service)
    ):
    return service.authenticate(auth_request)