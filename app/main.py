from fastapi import FastAPI
from app.utils.logger import logger

from app.api.routes_event import router as event_router

logger.info("Starting City Event API application")

app = FastAPI(title='City Event API')

logger.info("Including event router")
app.include_router(event_router)