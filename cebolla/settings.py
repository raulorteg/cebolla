import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

SENSOR_NAMES = {"sensor1": "Cactus", "sensor2": "Plant", "sensor3":"Basilicum"}
MAIL = os.environ.get("MAIL")
PASSWORD = os.environ.get("PASSWORD")
LOGGER_DIRECTORY = "/var/log/cebolla"
DATA_LOG = join(LOGGER_DIRECTORY, "data.txt")
VALID_PROCESSING_PERIODS = ["day", "week", "month", "all"]

if not os.path.exists(LOGGER_DIRECTORY):
    os.mkdir(LOGGER_DIRECTORY)
