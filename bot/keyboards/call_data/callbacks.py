from typing import Optional

from aiogram.filters.callback_data import CallbackData


class CategoryCallback(CallbackData, prefix='cat'):
    action: str
    category_id: Optional[int] = None


class SubcategoryCallback(CallbackData, prefix='sub'):
    action: str
    category_id: int
    subcategory_id: Optional[int] = None


class ProductCallback(CallbackData, prefix='prod'):
    action: str
    subcategory_id: int
    product_id: Optional[int] = None
    page: Optional[int] = None
