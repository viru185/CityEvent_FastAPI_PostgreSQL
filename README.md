# 🔹 “City Events API” (PostgreSQL, FastAPI)

Goal: Build a public API that provides event data for different cities. Focus on querying, filtering, and handling real-world structured data.

## 📦 Stack

- FastAPI
- PostgreSQL
- SQLAlchemy + Alembic (for DB models and migrations)

## 📊 Dataset

- Use or clean up an open dataset like:
- Events in the UK
- Or generate 300–500 rows using Faker or Mockaroo

## 📁 Data Fields

- Event title
- Description
- Date & Time
- Location (city, venue)
- Category (music, art, tech, etc.)
- Ticket price

## 🔧 API Endpoints

- GET /events/getall – list all events
- GET /events/{id} – get a single event
- GET /events/search?city=London&category=tech – filter events
- POST /events – add new event
- PUT /events/{id} – update event
- DELETE /events/{id} – delete event

## 🧠 Learnings

- Clean schema design
- Filtering with query parameters
- Data sorting and pagination
- Relationships (e.g., one city has many events)

&nbsp;

# FOLDER STRUCTURE

```
city_events_api/
├── app/
│   ├── __init__.py
│   ├── main.py               # FastAPI app instance
│   ├── config.py             # DB and app settings
|   ├── logs/
│   │   └── app.log           # app log file
│   ├── models/
│   │   ├── __init__.py
│   │   └── event.py          # SQLAlchemy Event model
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── event.py          # Pydantic schemas
│   ├── crud/
│   │   ├── __init__.py
│   │   └── event.py          # DB logic (CRUD operations)
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes_event.py   # API route definitions
│   ├── db/
│   │   ├── __init__.py
│   │   ├── session.py        # DB connection
│   │   └── base.py           # Base class for models
│   └── utils/
|       ├── logger.py         # app logger to log the events.
│       └── populate.py       # Script to load fake or real data
├── alembic/                  # DB migrations
│   └── ...
├── alembic.ini
├── requirements.txt
└── README.md
```
