from django.db import models

from backend.apps.products.models.category import TimeStampModel, Category


class SubCategory(TimeStampModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id}. {self.name} ({self.category.name})"
