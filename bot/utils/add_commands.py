import logging

from aiogram import Bot
from aiogram.types import BotCommand


async def add_bot_commands(bot: Bot):
    commands = [
        BotCommand(command='start', description='Botni ishga tushurish'),
        BotCommand(command='help', description='Yordam olish'),
        BotCommand(command='about', description='Bot haqida ma`lumot'),
        BotCommand(command='e_commerce', description='Mahsulotlarni ko`rish'),
        BotCommand(command='inline_mode', description='Input orqali qidirish funksiyasi')
    ]
    await bot.set_my_commands(commands=commands)
    logging.info('Bot komadalari muvoffaqiyatli o`rnatildi!')
