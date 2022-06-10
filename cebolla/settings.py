import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

MAIL = os.environ.get("MAIL")
PASSWORD = os.environ.get("PASSWORD")
LOGGER_DIRECTORY = "/var/cebolla.logs"
DATA_LOG = join(LOGGER_DIRECTORY, "data.txt")
VALID_PROCESSING_PERIODS = ["day", "week", "month", "all"]
