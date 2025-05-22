from fastapi import FastAPI
from app.utils.logger import logger

from app.api.routes_event import router as event_router

logger.info("Creating flask app")
app = FastAPI(title='City Event API')

logger.info("Adding routes to app")
app.include_router(event_router)