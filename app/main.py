from fastapi import FastAPI
from app.api.microapi import router as microapi_router

app = FastAPI(title="Micro-API de ejemplo")

app.include_router(microapi_router)
