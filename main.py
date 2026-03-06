import os
import threading
from flask import Flask
from config import Config
from pyrogram import Client, idle
import asyncio, logging
import tgcrypto
from pyromod import listen
from logging.handlers import RotatingFileHandler

# ---------------- FLASK SERVER ---------------- #

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is Running!"

def run():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

# ---------------- LOGGING ---------------- #

LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("log.txt", maxBytes=5000000, backupCount=10),
        logging.StreamHandler(),
    ],
)

AUTH_USERS = [int(chat) for chat in Config.AUTH_USERS.split(",") if chat != '']

prefixes = ["/", "~", "?", "!"]

plugins = dict(root="plugins")

# ---------------- BOT ---------------- #

if __name__ == "__main__":

    keep_alive()   # important for Render

    bot = Client(
        "StarkBot",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        sleep_threshold=20,
        plugins=plugins,
        workers=50
    )

    async def main():
        await bot.start()
        bot_info = await bot.get_me()
        LOGGER.info(f"<--- @{bot_info.username} Started (c) STARKBOT --->")
        await idle()

    asyncio.get_event_loop().run_until_complete(main())
    LOGGER.info("<---Bot Stopped-->")
