from fastapi import APIRouter, Depends
from app.domain.services.identity_service import IdentityService
from app.drivers.schemas.identities import CreateIdentity, IdentityResponse
from app.adapters.repositories.LocalIdentityRepository import LocalIdentityRepository

router = APIRouter()


def get_identity_service() -> IdentityService:
    return IdentityService(repository=LocalIdentityRepository())


@router.post("/", response_model=IdentityResponse)
async def create_identity(identity: CreateIdentity, service: IdentityService = Depends(get_identity_service)):
    return service.create_identity(identity)


@router.get("/")
async def get_identities(service: IdentityService = Depends(get_identity_service)):
    return service.get_identities()


@router.put("/{identity_id}")
async def update_identity(identity_id: str):
    return {"message": f"Identity {identity_id} updated!"}
