from fastapi import APIRouter, Depends, HTTPException
from app.adapters.repositories.InMemoryIdentityRepository import InMemoryIdentityRepository
from app.domain.services.authentication_service import IAuthenticationService, PasswordAuthenticationService, PinAuthenticationService
from app.drivers.schemas.auth import PasswordAuthenticationRequest, Token, PinAuthenticationRequest

router = APIRouter()

def get_password_authentication_service() -> IAuthenticationService:
    return PasswordAuthenticationService(repository=InMemoryIdentityRepository())

def get_pin_authentication_service() -> IAuthenticationService:
    return PinAuthenticationService(repository=InMemoryIdentityRepository())


@router.post("/password/authenticate", response_model=Token)
async def login(
        auth_request: PasswordAuthenticationRequest,
        service: IAuthenticationService = Depends(get_password_authentication_service)
    ):
    token = await service.authenticate(auth_request)
    if token is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
    return token

@router.post("/pin/authenticate", response_model=Token)
async def pin_login(
        auth_request: PinAuthenticationRequest,
        service: IAuthenticationService = Depends(get_pin_authentication_service)
    ):
    token = await service.authenticate(auth_request)
    if token is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
    return token