from sqlalchemy.orm import Session
from typing import List
from fastapi import HTTPException

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
    return all_event if all_event else []


def delete_event(db: Session, event_id: int) -> None:
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found.")
    db.delete(event)
    db.commit()
    return {"message": f"Event {event_id} deleted successfully."} 