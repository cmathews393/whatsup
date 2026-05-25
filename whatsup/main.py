import os
from contextlib import asynccontextmanager
from collections.abc import AsyncGenerator

from apscheduler.executors.asyncio import AsyncIOExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from whatsup.api import router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # Startup code
    jobstore_db = os.getenv("JOBSTORE_DB_URL", "sqlite:///jobs.sqlite")
    jobstores = {"default": SQLAlchemyJobStore(url=jobstore_db)}
    executors = {"default": AsyncIOExecutor()}
    scheduler = AsyncIOScheduler(jobstores=jobstores, executors=executors)
    if not scheduler.running:
        scheduler.start()

    yield  # Control is returned to FastAPI here

    # Shutdown code
    if scheduler.running:
        scheduler.shutdown(wait=False)


app = FastAPI(
    title="Whatsup API",
    description="Backend API for Whatsup",
    version="0.1.0",
    lifespan=lifespan,
)


@app.get("/")
async def root():
    """Redirect root calls to docs."""
    return RedirectResponse(url="/docs")


app.include_router(router)
