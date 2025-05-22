from sqlalchemy import Column, Integer, String, DateTime, Float

from app.db.base import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    date_time = Column(String, nullable=False)
    city = Column(String, nullable=False)
    venue = Column(String)
    category = Column(String)
    price = Column(Float)
