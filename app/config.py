import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://mattblack:icandoit@localhost:5432/eventsdb"
)
