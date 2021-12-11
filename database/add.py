# (c) @AbirHasan2005

from config import Config
from database.database import db
from pyrogram import Client
from pyrogram.types import Message


async def add_user_to_database(bot: Client, update: Message):
    if not await clinton.is_user_exist(update.from_user.id):
           await clinton.add_user(update.from_user.id)

