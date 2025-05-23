from sqlalchemy.orm import Session
from typing import List
from fastapi import HTTPException

from app.models.event import Event

from app.schemas.event import EventCreate, EventPatch


def create_event(event: EventCreate, db: Session) -> Event:
    db_event = Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event


def get_all_event(db: Session, skip: int = 0, limit: int = 20) -> List[Event]:
    all_event = db.query(Event).offset(skip).limit(limit).all()
    return all_event if all_event else []


def read_event_by_id(db: Session, event_id: int) -> Event:
    return db.query(Event).filter(Event.id == event_id).first()


def update_event_by_id(db: Session, event_id: int, event_data: EventPatch) -> Event:
    event = db.query(Event).filter(Event.id == event_id).first()

    if not event:
        raise HTTPException(status_code=404, detail=f"Event {event_id} not found")

    for key, value in event_data.dict(exclude_none=True).items():
        setattr(event, key, value)

    db.commit()
    db.refresh(event)
    return event


def delete_event_by_id(db: Session, event_id: int) -> None:
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail=f"Event {event_id} not found.")
    db.delete(event)
    db.commit()
