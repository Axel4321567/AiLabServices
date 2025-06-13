from fastapi import APIRouter, Depends
from app.services.microapi_service import MicroApiService

router = APIRouter(prefix="/microapi")

# ───── dependencia sencilla ─────
def get_service() -> MicroApiService:
    return MicroApiService()

@router.get("/ping")
def ping(service: MicroApiService = Depends(get_service)):
    return service.ping()
