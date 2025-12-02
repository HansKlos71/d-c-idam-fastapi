from fastapi import FastAPI
from app.drivers.routers.identities import router as identities_router

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# include identities router so main.py remains the single app starter
app.include_router(identities_router, prefix="/identities", tags=["identities"])
