import os
from dotenv import load_dotenv

load_dotenv()

# datasets url
DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://mattblack:icandoit@localhost:5432/eventsdb"
)

# app constants
# Constants path used in the project

LOGS_FILE = "app/logs/app.log"
LOGS_DIR = "app/logs"

# config related to logging
LOG_LEVEL = "INFO"
LOG_TO_FILE = True
LOG_TO_CONSOLE = True