from django.db import models

from backend.apps.products.models.category import TimeStampModel
from backend.apps.products.models.subcategory import SubCategory


class Product(TimeStampModel):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    stock = models.IntegerField()

    def __str__(self):
        return f"{self.id}. {self.name}"
