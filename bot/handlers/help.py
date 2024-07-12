from aiogram import types

async def help_command(message: types.Message):
    await message.reply("How can I help you?")
