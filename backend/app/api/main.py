from fastapi import APIRouter
from .routes import notes

api_router = APIRouter()
api_router.include_router(notes.router)

