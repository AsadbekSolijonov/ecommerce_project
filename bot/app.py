import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

load_dotenv()

# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv("BOT_TOKEN")
ADMINS = getenv('ADMINS').split(',')
PROVIDER_TOKEN = getenv('PROVIDER_TOKEN')
WEB_URL = getenv('WEB_URL')
dp = Dispatcher()


async def main() -> None:
    from bot.handlers import start_router, category_router
    from bot.utils import add_bot_commands
    from bot.utils.notify_admins import start_bot_notify, stop_bot_notify

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_routers(start_router, category_router)
    await add_bot_commands(bot)
    dp.startup.register(start_bot_notify)
    dp.shutdown.register(stop_bot_notify)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
