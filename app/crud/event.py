from sqlalchemy.orm import Session
from typing import List

from app.models.event import Event
from app.schemas.event import EventCreate


def create_event(db: Session, event_data: EventCreate) -> Event:
    db_event = Event(**event_data.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def get_event(db: Session, event_id: int) -> Event:
    return db.query(Event).filter(Event.id == event_id).first()


def get_all_event(db: Session, skip: int = 0, limit: int = 20) -> List[Event]:
    all_event = db.query(Event).offset(skip).limit(limit).all()
    print(type(all_event)) #Debugging
    return all_event if all_event else []
