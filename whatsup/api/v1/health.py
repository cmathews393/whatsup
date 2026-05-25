from fastapi import APIRouter

health_router = APIRouter(prefix="/health", tags=["Health"])

@health_router.get("/", tags=["Health"])
async def health():
    return {"healthy": True, "status": 200}
