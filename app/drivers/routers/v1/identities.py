from fastapi import APIRouter, Depends
from app.domain.services.identity_service import IdentityService
from app.drivers.schemas.identities import CreateIdentity, IdentityResponse, UpdateIdentity
from app.adapters.repositories.InMemoryIdentityRepository import InMemoryIdentityRepository

router = APIRouter()


def get_identity_service() -> IdentityService:
    return IdentityService(repository=InMemoryIdentityRepository())


@router.post("/", response_model=IdentityResponse)
async def create_identity(identity: CreateIdentity, service: IdentityService = Depends(get_identity_service)):
    return await service.create_identity(identity)


@router.get("/")
async def get_identities(service: IdentityService = Depends(get_identity_service)):
    return await service.get_identities()


@router.put("/{identity_id}", response_model=IdentityResponse)
async def update_identity(identity_id: str, identity: UpdateIdentity , service: IdentityService = Depends(get_identity_service)):
    return await service.update_identity(identity_id, identity)
