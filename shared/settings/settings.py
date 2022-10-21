import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
APIURL = os.environ.get("APIURL")
TELEGRAM_API_URL = os.environ.get("TELEGRAM_API_URL")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
DATA_BASE_URL = os.environ.get("DATA_BASE_URL")

