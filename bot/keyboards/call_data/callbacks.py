from typing import Optional

from enum import StrEnum
from typing import Optional
from pydantic import Field
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


class BuyAction(StrEnum):
    BUY = "buy"
    CONFIRM = "confirm"
    CANCEL = "cancel"


class BuyCallback(CallbackData, prefix="buy"):
    action: BuyAction
    product_id: Optional[int] = None
    quantity: Optional[int] = 1
    page: Optional[int] = None
