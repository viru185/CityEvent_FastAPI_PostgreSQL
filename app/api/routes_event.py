from fastapi import APIRouter, HTTPException
from fastapi import Depends, status
from typing import Annotated
from sqlalchemy.orm import Session
from app.utils.logger import logger

from app.schemas.event import EventCreate, EventRead, EventPatch
from app.db.session import get_db
from app.crud.event import (
    create_event,
    get_all_event,
    read_event_by_id,
    update_event_by_id,
    delete_event_by_id,
    search_events as crud_search_events,
)

router = APIRouter(prefix="/events", tags=["Events"])
db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/", response_model=EventCreate, status_code=status.HTTP_201_CREATED)
async def add_event(event: EventCreate, db: db_dependency) -> EventRead:
    """
    Create a new event.

    Args:
        event (EventCreate): The event data to create.
        db (Session): Database session dependency.

    Returns:
        EventRead: The created event object.

    Raises:
        HTTPException: If event creation fails.
    """
    logger.info(f"Creating event: {event}")
    return create_event(event=event, db=db)


@router.get("/", response_model=list[EventRead])
async def read_events(
    db: db_dependency,
    skip: int = 0,
    limit: int = 20,
) -> list[EventRead]:
    """
    Retrieve a list of all events with optional pagination.

    Args:
        db (Session): Database session dependency.
        skip (int, optional): Number of records to skip. Defaults to 0.
        limit (int, optional): Maximum number of records to return. Defaults to 20.

    Returns:
        list[EventRead]: List of event objects.
    """
    logger.info(f"Fetching events: skip={skip}, limit={limit}")
    return get_all_event(skip=skip, limit=limit, db=db)


@router.get("/search", response_model=list[EventRead])
async def search_events(
    db: db_dependency,
    title: str | None = None,
    city: str | None = None,
    category: str | None = None,
) -> list[EventRead]:
    """
    Search for events based on title, city, or category.

    Args:
        title (str, optional): Title of the event to search for.
        city (str, optional): City of the event to search for.
        category (str, optional): Category of the event to search for.
        db (Session): Database session dependency.

    Returns:
        list[EventRead]: List of matching event objects.
    """
    logger.info(
        f"Searching events with title={title}, city={city}, category={category}"
    )
    return crud_search_events(db=db, title=title, city=city, category=category)


@router.get("/{event_id}", response_model=EventRead)
async def read_event(event_id: int, db: db_dependency) -> EventRead:
    """
    Retrieve a single event by its unique ID.

    Args:
        event_id (int): The ID of the event to retrieve.
        db (Session): Database session dependency.

    Returns:
        EventRead: The event object if found.

    Raises:
        HTTPException: If the event is not found.
    """
    logger.info(f"Fetching event with id={event_id}")
    db_event = read_event_by_id(event_id=event_id, db=db)
    if not db_event:
        logger.warning(f"Event not found: id={event_id}")
        raise HTTPException(status_code=404, detail="Event not found")
    return db_event


@router.patch("/{event_id}", response_model=EventPatch)
async def update_event(
    event_id: int, event_data: EventPatch, db: db_dependency
) -> EventRead:
    """
    Update an existing event by its ID.

    Args:
        event_id (int): The ID of the event to update.
        event_data (EventPatch): The updated event data.
        db (Session): Database session dependency.

    Returns:
        EventRead: The updated event object.

    Raises:
        HTTPException: If the event is not found.
    """
    logger.info(f"Updating event id={event_id} with data={event_data}")
    return update_event_by_id(event_id=event_id, event_data=event_data, db=db)


@router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_event(event_id: int, db: db_dependency) -> None:
    """
    Delete an event by its unique ID.

    Args:
        event_id (int): The ID of the event to delete.
        db (Session): Database session dependency.

    Returns:
        None

    Raises:
        HTTPException: If the event is not found.
    """
    logger.info(f"Deleting event id={event_id}")
    delete_event_by_id(event_id=event_id, db=db)
