from pyrogram import Client, __version__, filters
from info import API_ID, API_HASH, SESSION
import os, math, logging, pytz
from datetime import date, datetime 
from pytz import timezone
import logging.config
from plugins import web_server
from pyrogram.errors import BadRequest, Unauthorized
from typing import Union, Optional, AsyncGenerator
import pytz
import aiohttp
from aiohttp import web
from utils import temp
from pyrogram.raw.all import layer
from pyrogram import types
from Script import script 
import aiohttp


logging.config.fileConfig("logging.conf")
logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)

class Bot(user):
    def __init__(self):
        super().__init__(
            name="user-bot",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION,
            workers=50,
            plugins={"root": "userbot"},
            sleep_threshold=5,
        )
    async def start(self):
        await super().start()
        me = await self.get_me()
        temp.ME = me.id
        temp.U_NAME = me.username
        temp.B_NAME = me.first_name
        self.username = '@' + me.username
        self.f_channel = F_SUB
        logging.info(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
        app = web.AppRunner(await web_server())
        await app.setup()
        await web.TCPSite(app, "0.0.0.0", 8080).start()
        logger.info("Running...")
        print(f"{me.first_name} | @{me.username} started...")


if __name__ == "__main__":
   app = Bot()
   app.run()
