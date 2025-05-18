from aiogram import Router, F, html
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.handlers.api.response import api_response
from bot.keyboards.call_data.callbacks import (CategoryCallback,
                                               SubcategoryCallback, ProductCallback)
from bot.keyboards.inline.button import (cateogry_builder, subcategories_builder,
                                         products_builder, product_detail_builder, quantity_selector_builder)
from bot.utils.helper.help_time import time_formatter
from bot.keyboards.call_data.callbacks import BuyCallback

category_router = Router()


@category_router.message(Command('category'))
async def show_categories(message: Message):
    categories = api_response.get_categories()
    category_keyboard_datas = [(j['id'], j['name']) for j in categories]

    await message.answer(
        text=f"Asosiy kategoriyalar:",
        reply_markup=cateogry_builder(category_keyboard_datas, 2))


@category_router.callback_query(CategoryCallback.filter())
async def category_handler(call: CallbackQuery, callback_data: CategoryCallback):
    if callback_data.action == 'view':
        category = api_response.get_categories(callback_data.category_id)
        subcategory_keyboard_datas = [(sub['id'], sub['category'], sub['name']) for sub in category['subcategories']]

        await call.message.edit_text(
            text=f"{html.bold(category['name'])} kategoriyasi:",
            reply_markup=subcategories_builder(subcategory_keyboard_datas, 2)
        )

    elif callback_data.action == 'back':
        categories = api_response.get_categories()
        category_keyboard_datas = [(cat['id'], cat['name']) for cat in categories]

        await call.message.edit_text(
            text="Asosiy kategoriyalar:",
            reply_markup=cateogry_builder(category_keyboard_datas, 2)
        )

    await call.answer()


@category_router.callback_query(SubcategoryCallback.filter())
async def show_subcategories(call: CallbackQuery, callback_data: SubcategoryCallback):
    category_id = callback_data.category_id
    subcategory_id = callback_data.subcategory_id

    if callback_data.action == 'view':
        subcategory = api_response.get_subcateogries(subcategory_id)
        products_keyboard_datas = [(p['id'], p['subcategory'], p['name']) for p in subcategory['products']]

        await call.message.edit_text(
            text=f"{html.bold(subcategory['name'])} ketegoriyasi:",
            reply_markup=products_builder(products_keyboard_datas, 2, cat_id=category_id))

    elif callback_data.action == 'back':
        categories = api_response.get_categories(callback_data.category_id)
        subcategory_keyboard_datas = [(s['id'], s['category'], s['name']) for s in categories['subcategories']]

        await call.message.edit_text(
            text=f"{html.bold(categories['name'])} kategoriyasi:",
            reply_markup=subcategories_builder(subcategory_keyboard_datas, 2))

    await call.answer()


@category_router.callback_query(ProductCallback.filter(F.action == 'paginate'))
async def paginate_products(call: CallbackQuery, callback_data: ProductCallback):
    subcategory = api_response.get_subcateogries(callback_data.subcategory_id)
    products_keyboard_datas = [(p['id'], p['subcategory'], p['name']) for p in subcategory['products']]

    await call.message.edit_text(
        text=f"{html.bold(subcategory['name'])} ketegoriyasi:",
        reply_markup=products_builder(
            products_keyboard_datas,
            cols=2,
            cat_id=subcategory['category'],
            page=callback_data.page
        )
    )

    await call.answer()


@category_router.callback_query(ProductCallback.filter())
async def show_products(call: CallbackQuery, callback_data: ProductCallback):
    subcategory_id = callback_data.subcategory_id
    product_id = callback_data.product_id

    if callback_data.action == 'view':
        product = api_response.get_product(product_id)
        product_name = f"🛍 Mahsulot: {product['name']}"
        product_desc = f"📝 Batavsil: {product['description'][:300]}..."
        product_price = f"💳 Narxi: {float(product['price']):,.0f} so'm"
        product_stock = product['stock']
        product_stock = f"📦 {product_stock} ta {product['name']} bor." if product_stock else '❌ Hozircha mavjud emas!'
        mark = '💾' if time_formatter(product['created_at']) == time_formatter(product['updated_at']) else '🔄'
        product_time = f"{mark} ⏳ {time_formatter(product['updated_at'])}"
        product_image = product['image']

        product_detail = (f"{html.bold(product_name)}\n\n"
                          f"{html.italic(product_desc)}\n\n"
                          f"{html.bold(product_price)}\n"
                          f"{html.bold(product_stock)}\n\n"
                          f"{html.bold(product_time)}")
        await call.message.edit_text(
            text=product_detail,
            reply_markup=product_detail_builder(subcategory_id, product_id, page=callback_data.page))

    elif callback_data.action == 'back':
        subcategory = api_response.get_subcateogries(subcategory_id)
        category_id = subcategory['category']
        products = [(p['id'], p['subcategory'], p['name']) for p in subcategory['products']]

        await call.message.edit_text(
            text=f"{html.bold(subcategory['name'])} ketegoriyasi:",
            reply_markup=products_builder(products, 2, cat_id=category_id))

    await call.answer()


@category_router.callback_query(BuyCallback.filter(F.action == "buy"))
async def buy_product_handler(call: CallbackQuery, callback_data: BuyCallback):
    product = api_response.get_product(callback_data.product_id)
    omborda = product['stock'] - callback_data.quantity
    text = (
        f"🛍 Mahsulot: {product['name']}\n"
        f"💰 Narxi: {float(product['price']):,.0f} so'm\n"
        f"🏪 Omborda: {f'{omborda} ta qoldi' if omborda else 'Qolmadi'}\n"
        f"📦 Miqdori: {callback_data.quantity} ta\n"
        f"💳 Jami: {float(product['price']) * callback_data.quantity:,.0f} so'm\n\n"
        f"Miqdorni tanlang:"
    )
    if product['stock'] < callback_data.quantity:
        return await call.answer('⚠️ Mahsulot soni cheklangan!', show_alert=True)

    await call.message.edit_text(
        text=text,
        reply_markup=quantity_selector_builder(callback_data.product_id, callback_data.quantity, callback_data.page)
    )

    await call.answer()


@category_router.callback_query(BuyCallback.filter(F.action == "confirm"))
async def confirm_purchase_handler(call: CallbackQuery, callback_data: BuyCallback):
    product = api_response.get_product(callback_data.product_id)
    total_price = float(product['price']) * callback_data.quantity

    # Bu yerda haqiqiy sotib olish logikasi bo'lishi kerak
    # Misol uchun, APIga so'rov yuborish yoki ma'lumotlar bazasiga yozish

    await call.message.edit_text(
        text=(
            f"✅ Sotib olish muvaffaqiyatli yakunlandi!\n\n"
            f"🛍 Mahsulot: {product['name']}\n"
            f"📦 Miqdori: {callback_data.quantity} ta\n"
            f"💳 Jami: {total_price:,.0f} so'm\n\n"
            f"Tez orada operatorlarimiz siz bilan bog'lanishadi."
        ),
        reply_markup=InlineKeyboardBuilder().button(
            text="🏠 Bosh menyu",
            callback_data=CategoryCallback(action="back")
        ).as_markup()
    )
    await call.answer()


@category_router.callback_query(BuyCallback.filter(F.action == "cancel"))
async def cancel_purchase_handler(call: CallbackQuery, callback_data: BuyCallback):
    product = api_response.get_product(callback_data.product_id)

    await call.message.edit_text(
        text=f"Sotib olish bekor qilindi: {product['name']}",
        reply_markup=product_detail_builder(
            sub_id=product['subcategory'],
            product_id=callback_data.product_id,
            page=callback_data.page
        )
    )
    await call.answer()


@category_router.message()
async def clear_message_in_chat(message: Message) -> None:
    await message.delete()
