from django.contrib import admin

from backend.apps.products.models import Category, Product, SubCategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'created_at', 'updated_at']
    search_fields = ('name',)


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'created_at', 'updated_at']
    search_fields = ('name',)
    autocomplete_fields = ('category',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'price', 'created_at', 'updated_at']
    search_fields = ('subcategory__name', 'name', 'subcategory__category__name',)
    autocomplete_fields = ('subcategory',)

