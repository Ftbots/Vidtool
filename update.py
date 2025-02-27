from sys import exit
from logging import (
    FileHandler,
    StreamHandler,
    INFO,
    basicConfig,
    error as log_error,
    info as log_info,
    getLogger,
    ERROR,
)
from os import path, environ, remove
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

getLogger("pymongo").setLevel(ERROR)

if path.exists("log.txt"):
    with open("log.txt", "r+") as f:
        f.truncate(0)

if path.exists("rlog.txt"):
    remove("rlog.txt")

basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[FileHandler("log.txt"), StreamHandler()],
    level=INFO,
)

BOT_TOKEN = environ.get("BOT_TOKEN", "")
if len(BOT_TOKEN) == 0:
    log_error("BOT_TOKEN variable is missing! Exiting now")
    exit(1)

BOT_ID = BOT_TOKEN.split(":", 1)[0]

DATABASE_URL = environ.get("DATABASE_URL", "")

if DATABASE_URL:  # Check if DATABASE_URL is not None and not empty
    try:
        conn = MongoClient(DATABASE_URL, server_api=ServerApi("1"))
        db = conn.mltb
        config_dict = db.settings.config.find_one({"_id": BOT_ID})
        if config_dict:
            environ["UPSTREAM_REPO"] = config_dict.get("UPSTREAM_REPO", "") # Use .get to avoid KeyError
            environ["UPSTREAM_BRANCH"] = config_dict.get("UPSTREAM_BRANCH", "master")  #Provide default value
        conn.close()
    except Exception as e:
        log_error(f"Database ERROR: {e}")
    finally:
        if 'conn' in locals():
            conn.close()
