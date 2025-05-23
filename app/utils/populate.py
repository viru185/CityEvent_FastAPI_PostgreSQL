import random

# from rich import print
from pprint import pprint as print
from faker import Faker
from datetime import datetime, timedelta

from app.models.event import Event
from app.schemas.event import EventCreate
from app.db.session import SessionLocal
from app.utils.logger import logger

fake = Faker()


class Populate:

    @staticmethod
    def _fake_event_gen():
        event = {
            "title": fake.catch_phrase(),
            "description": fake.text(max_nb_chars=100),
            "date_time": fake.date_time_this_year(before_now=True, after_now=True),
            # "date_time": fake.date_time_between(start_date="now", end_date="+30d"),
            "city": fake.city(),
            "venue": fake.company(),
            "category": random.choice(
                ["Music", "Tech", "Sport", "Food", "Art", "Dance"]
            ),
            "price": round(random.uniform(0, 500), 2),
        }
        # print(event)
        return event

    @staticmethod
    def _add_fake_data(event_data_lst: list[EventCreate]) -> None:
        logger.info(f"Adding {len(event_data_lst)} fake events to the database.")
        db = SessionLocal()
        try:
            db.add_all([Event(**event) for event in event_data_lst])
            db.commit()
            logger.info("Fake events committed to the database.")
        except Exception as e:
            logger.error(f"Error adding fake events: {e}")
            db.rollback()
            raise
        finally:
            db.close()
            logger.info("Database session closed after populating fake events.")

    @classmethod
    def run(cls, n=50):
        logger.info(f"Populating database with {n} fake events.")
        event_data_lst = [cls._fake_event_gen() for _ in range(n)]
        cls._add_fake_data(event_data_lst)
        print(f"Added {n} fake events to the database.")
        logger.info(f"Successfully added {n} fake events to the database.")


if __name__ == "__main__":
    Populate.run()
