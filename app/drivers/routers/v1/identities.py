from fastapi import APIRouter, Depends, HTTPException
from app.domain.services.identity_service import IdentityService
from app.drivers.schemas.identities import CreateIdentity, IdentityResponse, UpdateIdentity
from app.adapters.repositories.InMemoryIdentityRepository import InMemoryIdentityRepository

router = APIRouter()


def get_identity_service() -> IdentityService:
    return IdentityService(repository=InMemoryIdentityRepository())


@router.post("/", response_model=IdentityResponse)
async def create_identity(identity: CreateIdentity, service: IdentityService = Depends(get_identity_service)):
    new_identity = await service.create_identity(identity)
    if new_identity is not None:
        return new_identity
    raise HTTPException(
        status_code=400,
        detail="Invalid identity"
    )


@router.get("/")
async def get_identities(service: IdentityService = Depends(get_identity_service)):
    return await service.get_identities()


@router.put("/{identity_id}", response_model=IdentityResponse)
async def update_identity(identity_id: str, identity: UpdateIdentity , service: IdentityService = Depends(get_identity_service)):
    return await service.update_identity(identity_id, identity)
