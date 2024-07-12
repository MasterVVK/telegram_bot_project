from aiogram import Bot
from aiogram.types import BotCommand

async def set_default_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Start the bot"),
        BotCommand(command="/help", description="Help")
    ]
    await bot.set_my_commands(commands)
