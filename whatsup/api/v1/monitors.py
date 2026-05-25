from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy import text
from whatsup.db import engine


class MonitorBase(BaseModel):
    id: int
    name: str
    url: str
    status: str | None = None

    class Config:
        orm_mode = True


class MonitorCreate(BaseModel):
    name: str
    url: str
    check_type: str
    http_check_type: str | None = None
    expected_response: str | None = None
    interval: int


class MonitorUpdate(BaseModel):
    name: str | None = None
    url: str | None = None
    check_type: str | None = None
    http_check_type: str | None = None
    expected_response: str | None = None
    interval: int | None = None


class MonitorsResponse(BaseModel):
    monitors: list[MonitorBase]


monitors_router = APIRouter(prefix="/monitors", tags=["Monitors"])


@monitors_router.get("/", response_model=MonitorsResponse)
async def list_monitors():
    async with engine.connect() as session:
        result = await session.execute(
            text("SELECT id, name, url, status FROM monitors")
        )
        monitors = await result.fetchall()

    return MonitorsResponse(
        monitors=[MonitorBase.model_validate(monitor) for monitor in monitors],
    )
