from fastapi import APIRouter, Depends
from app.adapters.repositories.InMemoryIdentityRepository import InMemoryIdentityRepository
from app.domain.services.authentication_service import IAuthenticationService, PasswordAuthenticationService
from app.drivers.schemas.auth import PasswordAuthenticationRequest, Token

router = APIRouter()

def get_password_authentication_service() -> IAuthenticationService:
    return PasswordAuthenticationService(repository=InMemoryIdentityRepository())

def get_pin_authentication_service() -> IAuthenticationService:
    return PasswordAuthenticationService(repository=InMemoryIdentityRepository())


@router.post("/password/authenticate", response_model=Token)
async def login(
        auth_request: PasswordAuthenticationRequest,
        service: IAuthenticationService = Depends(get_password_authentication_service)
    ):
    return service.authenticate(auth_request)

@router.post("/pin/authenticate", reponse_model=Token)
async def pin_login(
        auth_request: PinAuthenticationRequest,
        service: IAuthenticationService = Depends(get_pin_authentication_service)
    ):
    return service.authenticate(auth_request)