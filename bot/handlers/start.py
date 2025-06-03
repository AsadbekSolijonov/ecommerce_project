from aiogram.filters import CommandStart, Command
from aiogram.types import Message, InlineKeyboardButton
from aiogram import Router, html
from aiogram.utils.keyboard import InlineKeyboardBuilder

start_router = Router()


@start_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Salom, {html.bold(message.from_user.full_name)}!\n\n"
                         f"Mahsulotlarni ko'rish uchun /e_commerce tugmasini bosing")


@start_router.message(Command('inline_mode'))
async def command_start_handler(message: Message) -> None:
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text="🔍 So'z izlash",
            switch_inline_query="kitob"  # Bu inputda @bot_username kitob ko'rinishida paydo bo'ladi
        ),
        InlineKeyboardButton(
            text="🔍 Botdan qirish",
            switch_inline_query_current_chat="iphone"  # Bu inputda @bot_username kitob ko'rinishida paydo bo'ladi
        )
    )
    await message.answer(f"Inline Modda qidirish funksiyasini ishlatish uchun tugmani bosing.",
                         reply_markup=builder.as_markup())


@start_router.message(Command('men_uchaman'))
async def can_fly(message: Message):
    await message.answer('Men ham uchaman Abdullajon!')
