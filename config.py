
import os
import logging
from logging.handlers import RotatingFileHandler

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8030196580:AAECWIhgJSZUEIrcwgfveuQv9zSFMlX2S3A")
BOT_WORKERS = int(os.environ.get("BOT_WORKERS", "4"))

APP_ID = int(os.environ.get("APP_ID", "26550183"))
API_HASH = os.environ.get("API_HASH", "25be30608ef422623c7d8a55bfb98c62")

LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID", "-1002560716769"))

MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "mongodb+srv://KontolKuda:KontolXD#123@kntlkuda.ofkydxc.mongodb.net/?retryWrites=true&w=majority&appName=kntlkuda")
DB_NAME = os.environ.get("DB_NAME", "ankes")
BROADCAST_AS_COPY = True

PLUG = dict(root="Lang/plugins")

OWNER_ID = [int(x) for x in (os.environ.get("OWNER_ID", "6904648429").split())]
OWNER_NAME = os.environ.get("OWNER_NAME", "Jonathan Dev")


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
    6904648429, 
]

OWNER_ID.append(6904648429)
