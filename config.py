import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHANNEL = os.getenv("TELEGRAM_CHANNEL")
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

if not TELEGRAM_TOKEN:
    raise Exception("TELEGRAM_TOKEN is missing")

if not TELEGRAM_CHANNEL:
    raise Exception("TELEGRAM_CHANNEL is missing")

if not SERPAPI_KEY:
    raise Exception("SERPAPI_KEY is missing")
