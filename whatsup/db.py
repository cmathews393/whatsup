import os

from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

Base = declarative_base()
echo_on = os.getenv("SQLALCHEMY_ECHO", "False").lower() in ("true", "1", "t")
engine = create_async_engine("sqlite+aiosqlite:///jobs.sqlite", echo=echo_on)
