import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from bot.utils import set_bot_commands

load_dotenv()

# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv("BOT_TOKEN")
ADMINS = getenv('ADMINS')

dp = Dispatcher()


async def start_bot(bot: Bot):
    await set_bot_commands(bot)
    for admin in ADMINS:
        await bot.send_message(chat_id=admin, text='Bot ishga tushdi!')


async def stop_bot(bot: Bot):
    logging.info('Stop bot')


async def main() -> None:
    from bot.handlers import start_router, category_router
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_routers(start_router, category_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
