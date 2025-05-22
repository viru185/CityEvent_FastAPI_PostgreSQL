from fastapi import FastAPI

from app.api.routes_event import router as event_router

app = FastAPI(title='City Event API')

app.include_router(event_router)