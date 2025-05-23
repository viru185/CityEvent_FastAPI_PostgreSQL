from app.db.init_db import init_db
from app.utils.populate import Populate
from app.utils.logger import logger

if __name__ == "__main__":
    logger.info("Starting database seeding process.")
    init_db()
    Populate.run(n=50)
    logger.info("Database seeding process completed.")
