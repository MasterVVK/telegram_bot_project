from aiogram import types

async def echo_message(message: types.Message):
    await message.answer(message.text)
