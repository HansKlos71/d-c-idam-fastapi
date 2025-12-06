from fastapi import FastAPI, status, Request
from fastapi.exceptions import RequestValidationError
from starlette.responses import JSONResponse

from app.drivers.routers.v1.identities import router as identities_v1_router
from app.drivers.routers.v2.identities import router as identities_v2_router
from app.drivers.routers.v1.auth import router as auth_router

app = FastAPI(
    title="Identity API",
    description="A simple identity management API",
    version="0.1.0"
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "detail": "Incorrect request parameters.",
            "errors": exc.errors() # TODO: prod remove
        }
    )


@app.get("/")
async def root():
    return {
        "AppName": "Identity API",
        "Version": "0.1.0"
    }

app.include_router(identities_v1_router, prefix="/v1/identities", tags=["v1/identities"])
app.include_router(identities_v2_router, prefix="/v2/identities", tags=["v2/identities"])
app.include_router(auth_router, prefix="/v1/auth", tags=["v1/auth"])