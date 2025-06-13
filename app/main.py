from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import microapi

app = FastAPI()

# CORS para Angular en localhost
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O mejor http://localhost:4200
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(microapi.router, prefix="/api")
