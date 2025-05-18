from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.keyboards.call_data.callbacks import CategoryCallback, SubcategoryCallback, ProductCallback


def cateogry_builder(datas, cols):
    builder = InlineKeyboardBuilder()
    for id, text in datas:
        builder.button(text=text, callback_data=CategoryCallback(action='view', category_id=id))
    builder.adjust(cols)
    return builder.as_markup()


def subcategories_builder(datas, cols):
    builder = InlineKeyboardBuilder()
    for sub_id, cat_id, text in datas:
        builder.button(text=text,
                       callback_data=SubcategoryCallback(action='view',
                                                         category_id=cat_id,
                                                         subcategory_id=sub_id))
    builder.button(
        text="↩️ Ortga",
        callback_data=CategoryCallback(action="back")
    )
    builder.adjust(cols)
    return builder.as_markup()


def products_builder(datas, cols, cat_id, page: int = 0):
    builder = InlineKeyboardBuilder()
    start_ofset = page * 5
    end_ofset = start_ofset + 5

    for prod_id, sub_id, text in datas[start_ofset: end_ofset]:
        builder.button(text=text,
                       callback_data=ProductCallback(action='view',
                                                     subcategory_id=sub_id,
                                                     product_id=prod_id,
                                                     page=page))
    builder.button(
        text="↩️ Ortga",
        callback_data=SubcategoryCallback(action='back', category_id=cat_id)
    )

    if page > 0:
        builder.button(
            text='⬅️ Avvalgi', callback_data=ProductCallback(
                action='paginate',
                subcategory_id=datas[0][1],
                prod_id=None,
                page=page - 1)
        )

    if end_ofset < len(datas):
        builder.button(
            text='➡️ Keyingi', callback_data=ProductCallback(
                action='paginate',
                subcategory_id=datas[0][1],
                prod_id=None,
                page=page + 1)
        )

    builder.adjust(cols)
    return builder.as_markup()


def product_detail_builder(sub_id, page: int = 0):
    builder = InlineKeyboardBuilder()
    builder.button(text='🛒 Sotib olish', callback_data='buy')
    builder.button(
        text="↩️ Ortga",
        callback_data=ProductCallback(action='back', subcategory_id=sub_id)
    )
    if page:
        builder.button(
            text="⬇️ Chiqish",
            callback_data=ProductCallback(action='paginate', subcategory_id=sub_id, page=page)
        )
    builder.adjust(2)
    return builder.as_markup()
