from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class EventBase(BaseModel):
    title: str
    description: Optional[str] = None
    date_time: datetime
    city: str
    venue: Optional[str] = None
    category: Optional[str] = None
    price: Optional[int] = 0.0


class EventCreate(EventBase):
    pass


class EventRead(EventBase):
    id: int

    class config:
        orm_mode = True
