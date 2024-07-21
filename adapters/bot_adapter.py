from botbuilder.core import BotFrameworkAdapter, BotFrameworkAdapterSettings
from config.config import BOT_APP_ID, BOT_APP_PASSWORD

settings = BotFrameworkAdapterSettings(app_id=BOT_APP_ID, app_password=BOT_APP_PASSWORD)
adapter = BotFrameworkAdapter(settings)