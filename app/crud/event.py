from sqlalchemy.orm import Session
from typing import List, Optional
from fastapi import HTTPException

from app.utils.logger import logger
from app.models.event import Event
from app.schemas.event import EventCreate, EventPatch


def create_event(event: EventCreate, db: Session) -> Event:
    logger.info(f"Creating event: {event}")
    db_event = Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    logger.info(f"Event created with ID: {db_event.id}")
    return db_event


def get_all_event(
    db: Session,
    skip: int = 0,
    limit: int = 20,
) -> List[Event]:
    logger.info(f"Fetching all events with skip={skip}, limit={limit}")
    all_event = db.query(Event).offset(skip).limit(limit).all()
    logger.info(f"Fetched {len(all_event)} events")
    return all_event if all_event else []


def search_events(
    db: Session,
    title: str | None = None,
    city: str | None = None,
    category: str | None = None,
) -> List[Event]:
    logger.info(
        f"Searching events with title={title}, city={city}, category={category}"
    )
    query = db.query(Event)
    if title:
        query = query.filter(Event.title.ilike(f"%{title}%"))
    if city:
        query = query.filter(Event.city.ilike(f"%{city}%"))
    if category:
        query = query.filter(Event.category.ilike(f"%{category}%"))
    results = query.all()
    logger.info(f"Found {len(results)} matching events")
    return results


def read_event_by_id(db: Session, event_id: int) -> Event:
    logger.info(f"Reading event with ID: {event_id}")
    return db.query(Event).filter(Event.id == event_id).first()


def update_event_by_id(db: Session, event_id: int, event_data: EventPatch) -> Event:
    logger.info(f"Updating event with ID: {event_id} with data: {event_data}")
    event = db.query(Event).filter(Event.id == event_id).first()

    if not event:
        raise HTTPException(status_code=404, detail=f"Event {event_id} not found")

    for key, value in event_data.dict(exclude_none=True).items():
        setattr(event, key, value)

    db.commit()
    db.refresh(event)
    logger.info(f"Event with ID: {event_id} updated")
    return event


def delete_event_by_id(db: Session, event_id: int) -> None:
    logger.info(f"Deleting event with ID: {event_id}")
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail=f"Event {event_id} not found.")
    db.delete(event)
    db.commit()
    logger.info(f"Event with ID: {event_id} deleted")
