from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router, html

start_router = Router()


@start_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Salom, {html.bold(message.from_user.full_name)}!\n\n"
                         f"Mahsulotlarni ko'rish uchun /category tugmasini bosing")


