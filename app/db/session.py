from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.utils.logger import logger

from app.config import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    logger.info("Creating new database session")
    db = SessionLocal()
    try:
        yield db
    finally:
        logger.info("Closing database session")
        db.close()
