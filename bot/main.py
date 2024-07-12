import json
from aiogram import Bot, Dispatcher, executor
from bot.handlers import start, help, echo
with open('config.json', 'r') as file:
    config = json.load(file)

but = Bot(token=config['bot_token'])
dp= Dispatcher(bot)

dp.register_message_handler(start.start_command, commands=["start"])
dp.register_message_handler(help.help_command, commands="help")
dp.register_message_handler(echo.echo_message)

if __name__ == '__main__':
    from bot.utils.set_bot_commands import set_default_commands
    executor.start_polling(dp, on_startup=set_default_commands)
