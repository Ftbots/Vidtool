from sys import exit
from dotenv import load_dotenv
from logging import basicConfig, error as log_error
from os import environ

basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level="INFO",
)

load_dotenv("config.env", override=True)

BOT_TOKEN = environ.get("BOT_TOKEN", "")
if not BOT_TOKEN:
    log_error("BOT_TOKEN variable is missing! Exiting now")
    exit(1)
