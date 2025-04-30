
import os
import logging
from logging.handlers import RotatingFileHandler

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7542158043:AAFV5QFhYlJJtNMS2Dg2rqOzgkMDuahEGjo")
BOT_WORKERS = int(os.environ.get("BOT_WORKERS", "4"))

APP_ID = int(os.environ.get("APP_ID", "13686467"))
API_HASH = os.environ.get("API_HASH", "8383797c9f1daf9dd16e04a75204d4be")

LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID", "-1002189344080"))

MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "mongodb+srv://sedekgaming123:<db_password>@cluster0.8vx3q4a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "antigikes")
BROADCAST_AS_COPY = True

PLUG = dict(root="Lang/plugins")

OWNER_ID = [int(x) for x in (os.environ.get("OWNER_ID", "6144669103").split())]
OWNER_NAME = os.environ.get("OWNER_NAME", "lang")


LOG_FILE_NAME = "Lang_logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

CREATOR = [
    6144669103, 
]

OWNER_ID.append(6144669103)
