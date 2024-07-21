import os
from dotenv import load_dotenv

load_dotenv()

CHAT_GPT_API_KEY = os.getenv("CHAT_GPT_API_KEY")
BOT_APP_ID = os.getenv("BOT_APP_ID")
BOT_APP_PASSWORD = os.getenv("BOT_APP_PASSWORD")