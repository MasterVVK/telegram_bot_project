from aiogram import types
from aiogram.dispatcher import Dispatcher

async def start_command(message: types.Message):
    await message.reply("Hello! I'm a Telegram bot.")
