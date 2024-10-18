from fastapi import APIRouter
from .endpoints import hello, devops

api_router = APIRouter()
api_router.include_router(hello.router, tags=["hello"])
api_router.include_router(devops.router, prefix="/devops", tags=["devops"])