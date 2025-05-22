from fastapi import APIRouter, HTTPException

from app.schemas.event import EventCreate, EventRead
from app.crud.event import create_event, get_event, get_all_event, delete_event
from app.db.session import db_dependency

router = APIRouter(prefix="/events", tags=["Events"])


@router.post("/", response_model=EventCreate)
async def add_event(event: EventCreate, db: db_dependency):
    return create_event(db, event)


@router.get("/getall", response_model=list[EventRead])
async def read_events(db: db_dependency, skip: int = 0, limit: int = 20):
    return get_all_event(db, skip, limit)


@router.get("/{event_id}", response_model=EventRead)
async def read_event(event_id: int, db: db_dependency):
    db_event = get_event(db, event_id)
    if not db_event:
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event


@router.delete("/{event_id}")
async def remove_event(event_id: int, db: db_dependency):
    return delete_event(db, event_id)