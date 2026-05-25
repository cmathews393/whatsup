import uuid

from whatsup.db import Base
from sqlalchemy import Column, String


from enum import Enum


class CheckType(Enum):
    HTTP = "http"
    PING = "ping"
    TCP = "tcp"
    CRON = "cron"


class HttpMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    HEAD = "HEAD"


class HttpCheckType(Enum):
    SIMPLE = "simple"
    CONTENT = "content"
    RESPONSE_CODE = "response_code"


class Monitor(Base):
    __tablename__ = "monitors"

    id: int = Column(int, primary_key=True, index=True)
    name: str = Column(String, nullable=False)
    url: str = Column(String, nullable=False)
    check_type: CheckType = Column(String, nullable=False)
    http_check_type: HttpCheckType = Column(String, nullable=True)
    expected_response: str = Column(String, nullable=True)
    interval: int = Column(int, nullable=False, default=60)  # Check interval in seconds
    last_checked: int = Column(
        int, nullable=True
    )  # Timestamp of the last check (epoch)
    status: str = Column(String, nullable=True)  # "up" or "down"
    error_message: str = Column(
        String, nullable=True
    )  # Last error message if the monitor is down
