DATA_LOGGER_DIRECTORY="./logs/data.txt"
PROCESSED_IMGS="./logs"
VALID_PROCESSING_PERIODS = ["day", "week", "month", "all"]


import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MAIL = os.environ.get("MAIL")
PASSWORD = os.environ.get("PASSWORD")