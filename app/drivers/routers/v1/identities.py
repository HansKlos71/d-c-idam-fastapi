from fastapi import APIRouter, Depends, HTTPException

from app.domain.ports.email_adapter import IEmailAdapter
from app.domain.services.identity_service import IdentityService
from app.drivers.schemas.identities import CreateIdentity, IdentityResponse, UpdateIdentity
from app.adapters.repositories.InMemoryIdentityRepository import InMemoryIdentityRepository
from app.adapters.emailer_adapter import ConsoleEmailAdapter
from app.application.mappers.identity_mapper import IdentityMapper

router = APIRouter()

def get_identity_service() -> IdentityService:
    return IdentityService(repository=InMemoryIdentityRepository())


def get_email_service() -> IEmailAdapter:
    return ConsoleEmailAdapter()


@router.post("/", response_model=IdentityResponse)
async def create_identity(
        identity: CreateIdentity,
        service: IdentityService = Depends(get_identity_service),
        email_service: ConsoleEmailAdapter = Depends(get_email_service)
):
    new_identity = await service.create_identity(
        identity,
        email_service
    )
    if new_identity is not None:
        return IdentityMapper.map_to_response(new_identity)
    raise HTTPException(
        status_code=400,
        detail="Invalid identity"
    )


@router.get("/")
async def get_identities(service: IdentityService = Depends(get_identity_service)):
    return await service.get_identities()


@router.put("/{identity_id}", response_model=IdentityResponse)
async def update_identity(
        identity_id: str,
        identity: UpdateIdentity,
        service: IdentityService = Depends(get_identity_service)
    ):
    return await service.update_identity(identity_id, identity)
