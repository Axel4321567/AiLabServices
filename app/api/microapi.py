from typing import List
from fastapi import APIRouter
from app.models.schemas import Metric
from app.services.microapi_service import MicroApiService

router = APIRouter()
micro_service = MicroApiService()

@router.get("/metrics", response_model=List[Metric])
def get_metrics():
    return micro_service.get_metrics()

@router.get("/metrics/getAll", response_model=str)
def get_all_metrics():
    return micro_service.get_all_metrics()
  
